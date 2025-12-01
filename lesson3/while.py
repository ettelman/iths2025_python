# while True:
#     pass

x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("Koden kördes normalt")


x = 0
while x < 5:
    print(x)
    if x == 3:
        break
    x += 1
else:
    print("Koden kördes normalt")

# while True:
#     break

# command = ""
# while command != "exit":
#     command = input("Ange ett kommando: ")
#     print(command)

password = input("Ange lösenord:")
while len(password) < 8:
    print("Lösenordet är för kort")
    password = input("Försök igen: ")

print("Lösenordet är OK")