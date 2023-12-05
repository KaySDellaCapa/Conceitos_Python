# Manipulando Listas

# criando a lista
nomes = ["Ana", "João", "Pedro", "Giovanna"]
print(f"listas de nomes: {nomes}")

# Se for add precisa escrever o print depois ou o escrever novamente
#nomes.append("Kayque")
#print(nomes) 

# Aqui pode haver uma repetição para mais nomes
# O {cont} serve para fazer uma contagem na lista
# precisa começar a contar do 1 até o 4, pois a contagem original começa do zero e acaba no três

# nomes com FOR
for cont in range(1, 3):
    novo_nome = input(f"Digite o nome {cont}: ")
    nomes.append(novo_nome)
print(f"Lista com nome adicionado: {nomes}")

# Quantidade de nomes com WHILE
resp = "Sim"
while resp == "Sim":
    novo_nome = input(f"Digite o nome: ")
    nomes.append(novo_nome)
    resp = input ("Deseja escrever mais um nome? S / N: ")
print(f"Lista com nome adicionado: {nomes}")

# Listando elementos pela lista
#print(nomes[0])

# Removendo o último elemento da lista
nomes.pop()
print(f"Removendo o último: {nomes}")

# Removendo um elemento qualquer
nomes.remove("Ana") #Esse nome será removido
print(f"Removendo o elemento: {nomes}")

# Verificando a existencia de um elemento
nome_pesquisado = input("Digite um nome para pesquisar")
if nome_pesquisado in nomes:
    print('Nome cadastrado')
else:
    print("Não encontrado")
    