import requests
from bs4 import BeautifulSoup
import lxml

url = "https://ettelman.github.io"
response = requests.get(url)

print(response.content)
