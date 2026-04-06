import socket
import threading
import re
from dnslib import DNSRecord, RR, QTYPE, A, RCODE
from records import records
from forwarder import forward_query

HOST = "0.0.0.0"
PORT = 8053

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("DNS Server running on port 8053...\n")


def is_valid_domain(domain):
    if not domain or len(domain) > 253:
        return False

    pattern = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$")

    labels = domain.split(".")
    for label in labels:
        if not pattern.match(label):
            return False

    return True


def handle_request(data, addr):
    try:
        request = DNSRecord.parse(data)
    except:
        print("Invalid DNS packet received")
        return

    domain = str(request.q.qname).rstrip(".")
    qtype = QTYPE[request.q.qtype]

    print(f"{addr} -> {domain} ({qtype})")

    if not is_valid_domain(domain):
        print("Blocked invalid domain")
        reply = request.reply()
        reply.header.rcode = RCODE.FORMERR
        server.sendto(reply.pack(), addr)
        return

    if qtype == "A" and domain in records:
        ip = records[domain]
        reply = request.reply()
        reply.add_answer(RR(domain, QTYPE.A, rdata=A(ip), ttl=60))
        server.sendto(reply.pack(), addr)
        print(f"Resolved locally: {domain} -> {ip}")

    else:
        response = forward_query(data)

        if response:
            server.sendto(response, addr)
            print(f"Forwarded: {domain}")
        else:
            reply = request.reply()
            reply.header.rcode = RCODE.SERVFAIL
            server.sendto(reply.pack(), addr)


while True:
    data, addr = server.recvfrom(4096)
    threading.Thread(target=handle_request, args=(data, addr)).start()
