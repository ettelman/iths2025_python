import requests
from bs4 import BeautifulSoup
import lxml

url = "https://webscraper.io/test-sites/e-commerce/static"
response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, 'lxml')

title = soup.title
print(title)
print(title.name)
print(title.string)

parent = title.parent
print(parent.name)

body = soup.body

# for desc in body.descendants:
#     print(desc)


nav_tag = soup.find('nav', {"id": "navbar"})
div_tag = soup.find('div', class_="container")

para_tag = soup.find('p')

all_para = soup.find_all('p')

div_tag.has_attr('data-info')

items = soup.select('div#main ul.items > li.items')

# print(para_tag.string)
# print(div_tag.get_text())

link = soup.find('a')
href = link.get('href')
print(href)

div = soup.find('div', class_="wrapper")

paragraph = div.find('p')
print(paragraph.string)
