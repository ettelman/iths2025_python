x = 5
if 0 < x < 10:
    print("X är emellan 0 och 10")

# age = int(input("Ange ålder: "))

# if 18 <= age <= 65:
#     print("Du är vuxen som jobbar")
# else:
#     print("Du är pensionär eller barn")

username = "admin"
password = "pass123"

if username == "admin" and password == "pass1231":
    print("Du är inloggad")
else:
    print("Fel användarnamn eller lösenord")


a = 5
b = 6
c = 5

print(a == b == c)
(a == b) and (b == c)

x = ["apple", "banana", "cherry"]

y = x

print(x is y) 
print(x == y) 