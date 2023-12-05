""" 
Escopo local e escopo global - Python trabalha com escopo local e globar, dentro
do bloco da função o escopo é local. Portanto ali feitas em objetos imutaveis
serão perdidas quando o método terminar de ser executado. Para usar objetos 
globais utilizamos a palavra-chave global, que informa ao interpretador que a
variavel que está sendo manipulada no escopo local é global.
Essa NÃO é uma boa prática e deve ser evitada
"""

# ESCOPO GLOBAL
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)