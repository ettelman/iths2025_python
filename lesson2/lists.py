ips = ["10.3.10.11", "10.3.10.22", "10.3.10.10"]
ports = [22, 80, 443]
scan_result = ["10.3.10.11", 22, "open", True]
services = [["ssh", 22], ["http", 80]]

print(ports[1])
print(services[1][1])

a = ports
ports[1] = 8080
print(ports)
print(a)

print(scan_result[-1])
# print(scan_result[10])

ports = [22, 80, 443, 8080]
ports[1:3] = [5555, 4444]
print(ports)

ports = [22, 80, 443]
ports_copy = ports.copy()
ports[1:3] = [5555, 4444]
print(ports)
print(ports_copy)

ports = [22, 80, 443]
ports.append(8080)
print(ports)

ports = [22, 80, 443]
ports.insert(1, 8080)
print(ports)

cves = ["CVE-2023-1235", "CVE-2024-4324", "CVE-2025-5435"]
cves.remove("CVE-2024-4324")
print(cves)

ports = [22, 80, 443]
removed = ports.pop()
print(ports)
print(removed)

ports = [22, 80, 443]
del ports[0]
print(ports)

ports = [22, 80, 443]
ports.clear()
print(ports)

ports = [22, 80, 443, 8080]
print(ports[::-1])
print(ports[1:3])
print(ports[::2])

ports = [22, 80, 443, 8080, 22]
print(ports.count(22))

ports = [445, 8080, 80, 443, 22]
ports.sort()
print(ports)

ports.sort(reverse=True)
print(ports)

services = ["sftp", "ssh", "telnet", "https"]
services.sort(key=len)
print(services)

services.reverse()
print(services)

print(len(services))

ports = [445, 8080, 80, 443, 22]
print(sum(ports))
print(min(ports))
print(max(ports))

print(23 in ports)

log = "User=admin 10.3.10.11 22"
log1 = "User=admin 10.3.10.11 22"
log2 = "User=admin 10.3.10.11 22"
log3 = "User=admin 10.3.10.11 22"
log4 = "User=admin 10.3.10.11 22"
parts = log.split()
print(parts)

ports = [445, 8080, 80]
ports2 = [443, 22]

all_ports = ports + ports2
print(all_ports)