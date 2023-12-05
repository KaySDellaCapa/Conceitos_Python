""" 
Temos 3 formas de interpolar variáveis em strings, a primeira é 
usando o sinal %, a segunda é utilizando o método format e a última é
utilizando o f strings

A primeira forma não é atualmente recomendada e seu uso em Python 3
é raro
"""

nome = "Kayque"
idade = 20
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade:": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") # O 10 dá espaço