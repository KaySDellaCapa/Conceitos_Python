""" 
Tuplas são estruturas de dados muito parecidas com as listas, a principal
diferença é que tuplas são imutaveis, enquanto listas são mutaveis.
Podemos criar tuplas através da classe tuple, ou colocando valores
separados por vírgula de parenteses
"""
# EXEMPLO: 

frutas = ("Laranja", "Pera", "Uva",) # Boa prática por virgula no final

letras = tuple("Python")

numeros = tuple([1,2,3,4]) # Tupla com lista, não podem ser modificaveis

pais = ("Brasil",) # Boa prática por virgula no final

##### QUANDO SE É UMA SEQUENCIA COMO LISTA, TEM ACESSO

frutas[0]
frutas[2]
frutas[-1]
frutas[-3]
