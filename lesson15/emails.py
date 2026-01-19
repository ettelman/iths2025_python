import re
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.iths.se/kontakt/"
response = requests.get(url)


html = response.text
soup = BeautifulSoup(html, 'html.parser')
page_txt = soup.get_text()

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
found_emails = re.findall(email_pattern, page_txt)

emails = set(found_emails)
print(emails)

with open("emails.txt", 'w', encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

data = []

for email in emails:
    entry = {
        "email": email
    }
    data.append(entry)

with open("emails.json", "w", encoding="utf-8") as f:
    json.dump(data, f)