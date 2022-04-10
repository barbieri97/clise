"""
Esse módulo le o arquivo de configuração e salva os dados
em variaveis a serem utilizadas por outros módulos
"""

from json import loads

with open('/home/barbieri/projetos/env_clise/clise/config.json', 'r', encoding='utf-8') as file:
    string_data = file.read()

data = loads(string_data)
EMAIL = data['email']
PASSWORD = data['password']
SERVER = data['server']
PORT = data['port']
