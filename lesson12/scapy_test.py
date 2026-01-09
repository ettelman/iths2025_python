from scapy.all import *

# pkts = sniff(filter="tcp", count=10)
# pkts.summary()

# ans, unans = sr(IP(dst="8.8.8.8")/ICMP(), timeout=2)
# ans.summary()

domain = "www.example.com"

dns_request = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(
    rd=1,
    qd=DNSQR(qname=domain)
)

response = sr1(dns_request, timeout=2)

if response and response.haslayer(DNS):
    for i in range(response[DNS].ancount):
        print(response[DNS].an[i].rdata)
else:
    print("No answer from server")