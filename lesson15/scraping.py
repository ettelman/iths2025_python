import time
import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-agent': 'Mozilla/5.0 (Linux; Android 15; SM-S931B Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36'}

url = "http://dn.se"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success")
else:
    print(f"Fail: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

headings = soup.find_all("h1")
anchors = soup.find_all("a")

# time.sleep(1)

data = [
    ['a']
]
for anchor in anchors:
    data.append(anchor)

with open("output.csv", 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

