"""
Comando while - é usado para repetir um bloco de código várias vezes.
Faz sentido usar o while quando não sabemos o número exato de vezes que
nosso bloco de código deve ser executado
"""

opcao = "1"

while opcao != "0":
    opcao = input("[1] sacar \n[2] extrato \n[0] sair \n: ")

    if opcao == "1":
        print("Sacando...")
    elif opcao == "2":
        print("Exibindo extrato...")
    elif opcao == "0":
        print("Adeus...")
        break
    else:
        print("Escolha algo válido")

# PARA NUMEROS IMPARES

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")