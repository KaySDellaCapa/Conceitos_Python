""" 
.issubset verifica se um conjunto pertence a outro.
"""

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_a.issubset(conjunto_a) # False