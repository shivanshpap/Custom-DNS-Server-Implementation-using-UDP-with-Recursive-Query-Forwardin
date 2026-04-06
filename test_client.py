import socket
import threading
import time
from dnslib import DNSRecord

SERVER = ("127.0.0.1", 8053)


def send_query(domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.settimeout(2)
        query = DNSRecord.question(domain)
        sock.sendto(query.pack(), SERVER)

        data, _ = sock.recvfrom(4096)
        return DNSRecord.parse(data)

    except:
        return None

    finally:
        sock.close()


def interactive():
    while True:
        domain = input("\nEnter domain (or exit): ")

        if domain == "exit":
            break

        response = send_query(domain)

        if response and response.rr:
            for ans in response.rr:
                print("IP:", ans.rdata)
        else:
            print("No result / Error")


def perf_test(n=100):
    domains = [
        "google.com", "youtube.com", "facebook.com",
        "example.com", "github.com", "local.test",
        "invalid_domain", "notreal.xyz"
    ]

    success = 0
    failure = 0
    lock = threading.Lock()

    def worker(domain):
        nonlocal success, failure
        r = send_query(domain)

        with lock:
            if r and r.header.rcode == 0:
                success += 1
            else:
                failure += 1

    print(f"\nRunning {n} concurrent queries...\n")

    threads = []
    start = time.time()

    for i in range(n):
        t = threading.Thread(target=worker, args=(domains[i % len(domains)],))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()

    total_time = end - start
    throughput = n / total_time

    print("----- RESULTS -----")
    print(f"Total Queries : {n}")
    print(f"Success       : {success}")
    print(f"Failure       : {failure}")
    print(f"Time Taken    : {total_time:.2f} sec")
    print(f"Throughput    : {throughput:.2f} queries/sec")


print("1. Interactive Mode")
print("2. Performance Test")
print("3. Both")

choice = input("Enter choice: ")

if choice == "1":
    interactive()
elif choice == "2":
    perf_test()
elif choice == "3":
    interactive()
    perf_test()
