# Crie um programa que solicite uma lista de números int
# e retorne a soma de todos os elementos da lista

#lista = ["Ana", "Pedro", "Hugo"]

#tuplas = (10, 90, 50)

#sets = {11, 34, 5}

#dicionarios = {"nome": "Fernando"}

# ISSO AQUI É UMA CONSTRUÇÃO DE LISTA

lista_numeros = []

resposta = "s" # Para reafirmar que s é TRUE

while resposta == "s":
    numero = input("Digite um número: ")
    lista_numeros.append(numero)
    resposta = input("Deseja continuar? s/n: ")
    print(lista_numeros)

# ISSO AQUI É UMA CONSTRUÇÃO DE DICIONARIO (com função de lista)

lista_clientes = []

resposta2 = "s"

while resposta2 == "s":
    nome = input("Digite um nome: ")
    estado = input("Digite seu estado: ")

    cliente = {
        "nome": nome,
        "estado": estado
    }

    lista_clientes.append(cliente)
    resposta2 = input("Deseja continuar? [s/n]: ")

    print(lista_clientes)