import requests
from bs4 import BeautifulSoup

url = "http://dn.se"
response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print(f"Fail: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all("a")

for heading in headings:
    print(heading.get_text())