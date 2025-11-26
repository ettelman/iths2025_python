empty_tumple = ()
ports = (22, 80, 443)
target = ("10.3.10.11", 22, True)
scan_result = (("10.3.10.11", 22), ("10.3.10.22", 443))

single = (42) # int
single = (42,) # tuple

credentials = "admin", "pass123", "192.168.1.1"
print(credentials)

print(credentials[1])
print(credentials[:2])

# credentials[1] = "hejsan"

targets = ("10.3.10.11", "10.3.10.22")
tmp = list(targets)
tmp.append("10.3.10.23")
targets = tuple(tmp)
print(targets)

ip, port, status = ("10.3.10.11", 22, True)
print(f"{ip}:{port} open={status}")

scan = ("10.3.10.11", 22, 80, 443, 8080)
ip, *open_ports = scan
print(ip)
print(open_ports)

ports = (22, 80, 443, 22)
print(ports.count(22))

print(ports.index(22))

def port_status():
    return ip, port, status