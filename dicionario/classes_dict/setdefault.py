""" .setdefault serve para uma verificação do dicionario, ou add """

contato = {"nome": "Kayque", "Telefone": "1111-1111"}

contato.setdefault("nome", "Giovanna") # Kayque # Não altera pois a chave já existe
print(contato) # {"nome": "Kayque", "Telefone": "1111-1111"}

contato.setdefault("idade", 28) # 28
print(contato) # {"nome": "Kayque", "Telefone": "1111-1111", "idade": 28}
# ADD A IDADE
# O valor so adiciona caso ele não exista