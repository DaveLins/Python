# Serve para deletar algo

# Importar lib requests
import requests

# Importar lib json
import json

# Varíavel req, método delete, passando a url
req = requests.delete("https://nubia-d01b9-default-rtdb.firebaseio.com/-MkxleW6B8rSarEmKILI.json")

print(req.json())