import requests

from bs4 import BeautifulSoup

response = requests.get("https://clock.onlinealarmkur.com/pt/")

content = response.content

site = BeautifulSoup(content, "html.parser")

hora = site.find("div", attrs = {"class": "clock-xl"})

print(hora.text)
