"""
Função range é uma função built-in do Python, ela é usada para produzir
uma sequência de números inteiros a partir de um inicio (inclusivo) para
um fim (exclusivo). Se usarmos range(i, j) sera produzido:

i, i+1, i+2, i+3,..., j-1

Ela recebe 3 argumentos: stop, start e step
"""

for numero in range(0, 11):
    print(numero, end=" ")

for numero_2 in range(0, 51, 5):
    print(numero, end=" ")