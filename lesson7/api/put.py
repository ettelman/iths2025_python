import requests

def update_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    payload = {"email":"updatetome@test.se"}

    response = requests.put(url, json=payload)
    print(f"Status code: {response.status_code}")
    print(response.json())

update_user(1)
