# Estrutura condicional ternaria

saldo = 2000
saque = 500 # Se for maior que 2000, irá dar falha

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")