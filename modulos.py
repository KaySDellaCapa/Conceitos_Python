# Calculadora

import random
import operacoes
from colorama import Fore, init
init(autoreset=True) # Esse autoreset é para a for não continuar depois da mensagem


def exibir_menu():
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - NÚMERO ALEATÓRIO")
    print("0 PARA SAIR")

# APÓS A IMPORTAÇÃO DA FUNÇÃO, É PRECISO DEFINIR ELA COM "OPERACAO.", IGUAL FEITO NESSES

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = operacoes.soma(a, b) # Modulando a função def aqui, a invocando
        print("Resultado:", resultado)
    elif opcao == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = operacoes.subtracao(a, b)
        print("Resultado:", resultado)
    elif opcao == "3":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = operacoes.multiplicacao(a, b)
        print(f"Resultado:", resultado)
    elif opcao == "4":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if b != 0:
            resultado = operacoes.divisao(a, b)
            print("Resultado:", resultado)
        else:
            print("Não divisivel por zero")
    elif opcao == "5":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = random.randint(a, b)
        print("Resultado:", resultado)
    elif opcao == "0":
        print(Fore.BLUE + "Saindo...")
        break
    else:
        print(Fore.RED + "Opção invalida, tente de novo")
        # Aqui foi importada uma cor
        