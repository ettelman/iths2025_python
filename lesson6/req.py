import requests

r = requests.get("http://dn.se")
# print(r.text)
print(r.status_code)

html = r.text

if "<title>" in html:
    start = html.find("<title>") + 7
    end = html.find("</title>")
    title = html[start:end].strip()
    print(title)