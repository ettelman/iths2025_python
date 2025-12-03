# def function_name(param)
#   kodblock
#   return result

def greet_user(username):
    return f"Welcome {username}"

print(greet_user("Admin"))

def add_ports(p1, p2):
    return p1 + p2

print(add_ports(22, 80))

def scan_host(host="127.0.0.1"):
    print(f"Scanning {host}")

scan_host()
scan_host("10.3.10.11")

def connect(protocol, port):
    print(f"Connecting via {protocol} to port: {port}")

connect("ssh", 22)
connect(port=443, protocol="https")

def add(a, b):
    return a + b

def sum_double(a, b):
    result = add(a, b)
    return result * 2

print(sum_double(3, 5))

def classify_port(port):
    if port < 1024:
        return "System port"
    elif port < 49152:
        return "Registred port"
    else:
        return "Dynamic port"

print(classify_port(22))
print(classify_port(8080))
print(classify_port(55000))


def check_access(username, password):
    if username == "root" and password == "abc123":
        return "lkhjfgs897234lkjg98324lknfsd9823"
    else:
        return "Access denied"

def port_scan(open_ports, closed_ports):
    return open_ports, closed_ports

result = port_scan(22, 80)
print(result)

def calc(in_bytes, out_bytes):
    return in_bytes + out_bytes

network_data = (2048, 4096)
result = calc(*network_data)
print(result)



def port_scan(open_ports, closed_ports):
    return open_ports, closed_ports

open_ports, closed_ports = port_scan(22, 80)
print(open_ports)
print(closed_ports)

def hash_lengths(*hashes):
    for i in hashes:
        print(f"{i} is {len(i)} long")


h1 = "5f4dcc3b5aa765d61d8327deb882cf99"
h2 = "098f6bcd4621d373cade4e832627b4f6"
h3 = "21232f297a57a5a743894a0e4a801fc3"

hash_lengths(h1, h2, h3)


