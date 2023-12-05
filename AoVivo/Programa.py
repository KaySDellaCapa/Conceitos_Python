# Crie um programa que exiba um menu com 5 opções para o usuario
# A última deve ser 0 para sair do programa.
# Cada opção deve revelar informações importantes

# contador = 1

# while contador < 51:
   # print(f"{contador} - Teste While")
    # contador += contador # Contador agora vale 1


opcao = None # Variavel vazia

while opcao != 0: # Enquanto a opção não for zero, vai reproduzir tudo
# Tudo está dentro do WHILE
    print("MENU:")
    print("1 - OPÇÃO 1")
    print("2 - OPÇÃO 2")
    print("3 - OPÇÃO 3")
    print("4 - OPÇÃO 4")
    print("5 - OPÇÃO 5")
    print("0 - SAIR")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Executando opção 1")
    elif opcao == 2:
        print("Executando opção 2")
    elif opcao == 3:
        print("Executando opção 3")
    elif opcao == 4:
        print("Executando opção 4")
    elif opcao == 5:
        print("Executando opção 5")
    elif opcao == 0:
        print("saindo...")
    else:
        print("Digite algo válido")