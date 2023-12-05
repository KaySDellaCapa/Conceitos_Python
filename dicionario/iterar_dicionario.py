""" 
Iterar dicionários - A forma mais comum para percorrer os dados de um
dicionario é utilizando o comando for
"""

contato = {
    "ksdellacapa@gmail.com": {"nome": "Kayque", "telefone": "1111-1111"}
}

for chave, valor in contato.items(): # Items retorna uma lista de tuplas
    print(chave,valor)