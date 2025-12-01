# for variabel in iterable:
#     pass

ports = [21,22,80, 443, 8080]

for port in ports:
    print(f"Porten {port} är öppen")

credentials = ("admin", "bobbo", "marcus")
for user in credentials:
    print(f"Bruteforcar mot {user}")

password = "admin123"
for char in password:
    print(char)

logins = [("admin", "admin123"), ("root", "root123"), ("guest", "guest123")]
for username, password in logins:
    print(f"Bruteforcar med username {username} och lösenord {password}")

services = {"SSH": 22, "HTTP": 80, "HTTPS": 443}

for key in services:
    print(key)

for value in services.values():
    print(value)

for key, value in services.items():
    print(f"{key} -> {value}")

for i in range(101):
    print(i)

for i in range(2, 12, 2):
    print(i)

users = ["admin", "guest", "bobbo"]
passwords = ["1234", "winter2025", "test"]

for user in users:
    for password in passwords:
        print(f"Testing {user} : {password}")

ports = [21,22,80, 443, 8080]

for port in ports:
    if port == 80:
        print("Port 80 är blockerad")
        break
    print(f"Skannar port {port}")

for port in ports:
    if port == 80:
        continue
    print(f"Skannar port {port}")

