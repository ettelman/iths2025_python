import random
import string

latency = [53, 55, 25, 66]
print(f"Highest ping {max(latency)}")
print(f"Lowest ping {min(latency)}")

distros = ["Arch", "Ubuntu", "Debian", "NixOS"]
print(min(distros))
print(max(distros))

print(random.randint(1, 1024))
print("")
latency = [53, 55, 25, 66]
print(random.choice(latency))

random.shuffle(latency)
print(latency)

chars = string.ascii_letters + string.digits + "!@#$%&"
password = "".join(random.choice(chars) for _ in range(12))
print(password)

password = ""
for i in range(12):
    random_char = random.choice(chars)
    password += random_char
print(password)