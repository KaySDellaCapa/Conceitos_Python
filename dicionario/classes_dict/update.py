""" .update serve para atualizar o dicionario com outro dicionario"""

contato = {
    "ksdellacapa@gmail.com": {"nome": "Kayque", "telefone": "1111-1111"}
}

contato.update({"ksdellacapa@gmail.com": {"nome": "Kay"}})
print(contato)

contato.update({"ksdellacapa@gmail.com": {"nome": "Giovanna", "telefone": "2222-222"}})
print(contato)