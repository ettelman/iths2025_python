# enumerate(iterable, start=x)

services = ["ssh", "ftp", "smb"]
for index, service in enumerate(services):
    print(f"{index} - {service}")

users = [("admin", "root"), ("bobbo", "editor"), ("marcus", "hacker")]
for index, (username, role) in enumerate(users):
    print(f"{index}: {username} is role {role}")

network = [
    ["router", "switch", "server1"],
    ["server2", "firewall", "proxy"],
    ["client1", "client2", "client3"]
]

for i, row in enumerate(network):
    for j, device in enumerate(row):
        print(f"Device{i}{j} = {device}")

print("")
print("")

hosts = ["winterfell", "essos", "castelblack"]
status = ["online", "offline", "online"]
ips = ["10.3.10.11", "10.3.10.12", "10.3.10.22"]

for host, state, ip in zip(hosts, status, ips):
    print(f"{host} is {state} @ {ip}")

allowed_hosts = ["10.3.10.11", "10.3.10.12", "10.3.10.22"]

print("10.3.10.11" in allowed_hosts)
print("10.3.10.13" in allowed_hosts)

