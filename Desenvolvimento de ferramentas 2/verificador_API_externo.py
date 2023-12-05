import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/177.140.228.189/json?token=d47daaf9b08a2b'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
city = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrganização: {0}'.format(org, regiao, pais, city, ip))