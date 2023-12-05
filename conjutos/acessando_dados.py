""" 
Acessando os Dados - conjuntos em Python não suportam indexação e nem
fatiamento, caso queira acessar os seus valores é necessário converter o
conjunto para lista
"""
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0]) # Apenas ao transformar em lista é possivel ver indice