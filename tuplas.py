# Manipulando Tuplas

cores = ("Vermelha", "Azul", "Amarelo", "Verde") #Pode usar com ou sem ()
print(f"Meu carro é {cores[2]}")

qtd = len(cores) #feito para contar
print(f"Tenho {qtd} de opçoes de cores")

# Dá pra pedir pro usuario escrever uma cor
cor = input("Digite uma cor: ")

qtd_cor = cores.count(cor) # A cor escolhida vai acumular aqui e contar uma quantidade
print(f"Temos {qtd_cor} variações de {cor}")

# Com estrutura if
if cor in cores: 
    print(f"A cor {cor} existe na loja")
else:
    print(f"A cor {cor} não existe na loja")

aluno = ("Leonidas", 10, 5)
nome, nota1, nota2 = aluno
media = (nota1+nota2) / 2
print(f"O aluno {nome}, com suas notas {nota1}, {nota2}, com media de {media}")
