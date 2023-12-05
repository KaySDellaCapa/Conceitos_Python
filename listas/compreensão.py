""" 
Compreensão de lsitas - oferece uma sintaxe mais curta quando você 
deseja: criar uma nova lista com base nos valores de uma lista existe
(filtro) ou gerar uma nova lista aplicando alguma modificação nos 
elementos de uma lista existente
"""
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

    print(pares)

# COMPREENSION

numeros_2 = [1, 30, 21, 2, 9, 65, 34]
pares_2 = [numero for numero in numeros if numero % 2 == 0]
# Ele retorna o valor ao invés de adicionar como o .append

# MODIFICANDO AO QUADRADO

numeros_3 = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

    print(quadrado)

# COMPREENSION

numeros_3 = [1, 30, 21, 2, 9, 65, 34]
quadrado_2 = [numero ** 2 for numero in numeros]
# Antes de retornar, ao final do laço, tem todos os números ao quadrado

print(quadrado_2)