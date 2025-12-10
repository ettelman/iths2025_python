import requests

url = "https://jsonplaceholder.typicode.com/users"

for i in range(1,31):
    u = url + str(i)
    response = requests.get(u)

    if response.status_code == 200:
        print(response.json())