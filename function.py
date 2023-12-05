# FUNÇÕES EM PYTHON

def mensagem ():
    print("Olá, Mundo")

mensagem()


def calcular_desconto(preco): #Ela é uma função pura, precisa armazenar o valor numa variavel
    preco_final = preco * 0.8
    return preco_final

valor_pagar = calcular_desconto(100) # Aqui está chamando o valor
print(valor_pagar)


def soma(a,b):
    return a + b

total = soma(4, 90)
print(total)


valores = [100, 30, 45, 33.99]
print("--- VALORES COM DESCONTO ---")
for valor in valores:
    valor_desconto = calcular_desconto(valor) # Está sendo armazenado o desconto da variavel VALOR
    print(f"{valor_desconto:.2f}")
# Percorre toda a lista, item por item, passando por calcular_desconto, armazenando no valor_desconto
# e mostrando na tela