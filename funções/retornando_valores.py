"""  
Retornando valores - para retornar um valor, utilizamos a palvra reservada
return. Toda função Python retorna None por padrão. Diferente de outras linguagens
em Python return pode retornar mais de um valor
"""

def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor    = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 34])) # 64
print(retornar_antecessor_e_sucessor(10)) # (9, 11)