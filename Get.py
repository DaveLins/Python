# Importar lib requests
import requests

# Importar lib json
import json

# Varíavel cotacoes, método get, passando a url API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# Transformando varíavel cotacoes para um json
cotacoes = cotacoes.json()

# Puxando os valores desejados
cotacoes_dolar = cotacoes["USDBRL"]["bid"] # Dentro do parãmetro USDBRL, pegar "bid"

print(cotacoes_dolar)