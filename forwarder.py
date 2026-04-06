import socket

def forward_query(data):
    upstream_dns = ("8.8.8.8", 53)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.settimeout(2)
        sock.sendto(data, upstream_dns)
        response, _ = sock.recvfrom(4096)
        return response
    except:
        return None
    finally:
        sock.close()
