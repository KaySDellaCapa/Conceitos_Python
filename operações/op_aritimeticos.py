# Adição
print(1 + 1)

# Subtração
print(10 - 2)

# Multiplicação
print(4 * 3)

# Deivisão
print(12 / 3)

# Divisão inteira
print(12 // 3)

# Módulo - REAÇÃO DA DIVISÃO (quantos 3 cabe dentro de 10)
print(10 % 3)

# Exponenciação
print(2 ** 3)

# PRECEDENCIA

print(10 - 5 * 2)
# 0

print((10 - 5) * 2)
# 10

print(10 ** 2 * 2)
# 200

print (10 **(2*2))
# 10000

print(10 / 2 * 4)
# 20.0

# TESTE

produto_1 = 30
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 / produto_2)
print(produto_1 ** produto_2)

# ORDEM DE EXECUÇÃO

y = (10 / 2) * (25 + 2) - (2 ** 2) # Executa da esquerda para a direita
print(y)