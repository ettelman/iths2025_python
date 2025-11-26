open_ports = set()
open_ports = {22, 80, 443}

open_ports = {22, 80, 443, 22}
print(open_ports)

open_ports = set([22, 80, 443, 22])
print(open_ports)

open_ports.add(8080)
print(open_ports)

open_ports.update([5555, 4444])
print(open_ports)

open_ports.remove(5555)
print(open_ports)

open_ports.discard(4434)
print(open_ports)

removed = open_ports.pop()
print(removed)
print(open_ports)

open_ports.clear()
print(open_ports)

