import json

with open('test.json') as file:
    data = json.load(file)

print(data)

data2 = {
    "username": "admin",
    "active": False
}

json_string = json.dumps(data2)
print(json_string)

with open("data.json", 'w') as file2:
    json.dump(data2, file2)