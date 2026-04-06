# Custom DNS Server Implementation using UDP with Recursive Query Forwarding

## 📌 Project Overview
This project implements a lightweight DNS server using UDP that resolves predefined domain names locally and supports recursive query forwarding. The server parses DNS requests, validates domain names, and efficiently handles multiple client queries using multithreading. If a domain is not found in local records, the query is forwarded to an upstream DNS server (Google DNS - 8.8.8.8), ensuring reliable and complete domain resolution.

This project demonstrates core networking concepts such as socket programming, DNS protocol handling, concurrency, and input validation.

---

## ✅ Features
- UDP-based DNS server
- Local domain resolution
- Recursive query forwarding
- DNS packet parsing using dnslib
- Input validation for security
- Multi-threaded request handling
- Performance testing with concurrent queries

---

## 📂 Project Structure
```
server.py        # Main DNS server
forwarder.py     # Handles forwarding to upstream DNS
records.py       # Stores predefined domain-IP mappings
test_client.py   # Client for testing and performance
README.md
```

---

## ⚙️ Requirements
- Python 3.x
- dnslib

Install dependency:
```
pip install dnslib
```

---

## 🚀 Setup Instructions

Clone the repository:
```
git clone https://github.com/shivanshpap/Custom-DNS-Server-Implementation-using-UDP-with-Recursive-Query-Forwarding.git
```

Navigate to project folder:
```
cd Custom-DNS-Server-Implementation-using-UDP-with-Recursive-Query-Forwarding
```

Run the DNS server:
```
python server.py
```

Server runs on:
```
0.0.0.0:8053
```

---

## 🧪 Usage

Run the client:
```
python test_client.py
```

Options:
- Interactive Mode → Enter domain names manually
- Performance Test → Runs multiple concurrent queries
- Both → Runs both modes

---

## 🌐 Local Records

- google.com → 142.250.183.14
- youtube.com → 142.250.183.46
- facebook.com → 157.240.22.35
- example.com → 93.184.216.34
- github.com → 140.82.113.4
- local.test → 127.0.0.1

---

## 🔁 Working

1. Client sends DNS query
2. Server parses the request
3. If domain exists locally → returns IP
4. Otherwise → forwards request to upstream DNS
5. Sends response back to client

---

## 🔐 Security
- Domain validation using regex
- Invalid or malformed queries are rejected

---

## 📊 Performance
- Handles concurrent queries using threading
- Includes built-in performance testing
- Measures throughput (queries per second)

---

## 📌 Conclusion
This project provides a practical implementation of a DNS server, covering UDP communication, DNS resolution, query forwarding, concurrency, and security validation.

---
