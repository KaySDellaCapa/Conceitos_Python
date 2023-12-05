"""
Operadores de Identidade são operadores utilizados para comparar se os dois objetos testados 
ocupam a mesma posição na memória
"""

curso = "Curso de Python"
nome_curso = curso # Recebe a variavel curso, e mesmo valor
saldo, limite = 200, 200

curso is nome_curso
# True

curso is not nome_curso
# False

saldo is limite
# True

# TESTE

saldo_2 = 1000 # Se as duas tiverem os mesmo valor sai como a mesma região de memoria
limite_2 = 500

print(saldo_2 is limite_2)
print(saldo_2 is not limite_2)