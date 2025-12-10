import requests

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        return response.json()
    else:
        print("No data found")


def get_user(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        print(response.headers)
        return response.json()
    else:
        print("No data found")

# users = get_users()

print(get_user(5))
# print(users)


# headers = {
#     "Authorization": "Bearer 2345987tklfgjsh97843y5jkndfvg78",
#     "Custom-header": "hej"
# }
# token = "2345987tklfgjsh97843y5jkndfvg78"
# url = "https://jsonplaceholder.typicode.com/users/"
# response = requests.get(url, headers=headers)
# response = requests.get(url, params={"token": token})