empty_dict = {}
user = {
    "username": "admin",
    "role": "root",
    "active": True
}
print(user["username"])
print(user["active"])
# print(user["email"])
print(user.get("email", "Not found"))
user["username"] = "bobbo"
print (user["username"])
user["email"] = "bobbo@bobbo.se"
print (user)


# del user["email"]
# print (user)

key, value = user.popitem()
print(f"Borttaget {key} - {value}")
# user.clear()
# print(user)

print(user.keys())
print(user.values())
print(user.items())

user.update({"username": "marcus", "role":"user"})
print(user)

info = {"user": "root"}
info.setdefault("role", "admin")
print(info.setdefault("role", "admin"))

