# Importar lib requests
import requests

# Importar lib json
import json

# Importar lib bs4
from bs4 import BeautifulSoup

response = requests.get("https://github.com/login")

content = response.content

site = BeautifulSoup(content, "html.parser")

tok = site.find("input", attrs = {"name": "authenticity_token"})


#Varíavel info, passando o que vai ser criado no banco de dados
info = {

    "authenticity_token": tok["value"],
    "login": "e-mail aqui", 
    "password": "senha aqui"

}

# Varíavel req, método post, passando a url e a data com a varíavel info
req = requests.post("https://github.com/login", data = info)

print(req.headers)
