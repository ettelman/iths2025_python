import requests

def delete_user(id):
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.delete(url)
    print(f"Status code: {response.status_code}")

delete_user(7)

#query("SELECT * FROM users WHERE deleted_at IS NULL")



