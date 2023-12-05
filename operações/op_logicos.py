"""
São operadores utilizados em conjunto com operadores de comparação, para
montar expressão lógica. Quando um operador de comparação é utilizado, 
o resultado retornado é um booleano, dessa fora podemos combinar operadores
de comparação com operadores lógicos, exemplo:
op_comparacao + op_logico + op_comparacao...N... 

"""

saldo = 1000
saque = 200
limite = 100

resultado = saldo >= saque and saque <= limite # Tudo precisa ser TRUE para dar TRUE
print(resultado)
# False

# OPERADORES DE NEGAÇÃO

contatos_emergencia = [] # Lista vazia em Python é considerado False

not 1000 > 1500
# True

not contatos_emergencia
# True

not "saque 1500;" # String com valor
# False

not "" # String com vazia é False
# True

# PARENTESES
# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True
exp_2 =(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# True

print(exp)
print(exp_2)