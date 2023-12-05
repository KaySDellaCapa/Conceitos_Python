""" 
.discard elimina os valores
"""

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45) # Não discarta pois não existe

numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}