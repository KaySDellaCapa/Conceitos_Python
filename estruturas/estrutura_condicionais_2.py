"""
if aninhado - podemos criar estruturas condicionais aninhadas, para isso
basta adicionar estruturas if/elif/else dentro do bloco de código de 
estruturas if/elif/else
"""
conta_normal = True
conta_universitaria = False
# Se ambos forem FALSE, então irá direto para o ELSE

saldo = 2000
saque = 500 # Se o saque superar 2500 vai ir para o ELSE
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel reaizar o saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheu o tipo de conta")