# Importar lib requests
import requests

# Importar lib json
import json

# Varíavel info, passando o que vai ser criado no banco de dados
info = '{"Nome": "David"}'

# Varíavel req, método post, passando a url e a data com a varíavel info
req = requests.post("https://nubia-d01b9-default-rtdb.firebaseio.com/.json", data = info )

print(req.json())