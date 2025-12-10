import requests

def create_user():
    url = "https://jsonplaceholder.typicode.com/users"
    payload = {
        "name":"testuser",
        "email":"test@test.se"
    }

    response = requests.post(url, json=payload)
    print(f"Status code: {response.status_code}")
    print(response.json())

create_user()

# response.json()
# response.text
# reponse.headers