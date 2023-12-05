""" 
Fatiamento - além de acessar elementos diretamente, podemos extrair um
conjunto de valores de uma sequência. Para isso, basta passar o indice
inicial e\ou final para acessar o conjunto. Podemos ainda informar quantas
posições o cursos deve "pular" no acesso.
"""
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"] # ANDA DE 2 EM 2
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # NOME AO CONTRARIO
