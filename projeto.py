import os

from colorama import init, Fore

from cidades import ler_cidades  # Está em outro arquivo

init(autoreset=True)

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") # Escrever só se for cls, se não for, usara clear

def pausar():
    input(f"{Fore.BLUE}Digite ENTER para continuar...")

def exibir_menu():
    print(F"{Fore.GREEN}-----MENU-----")
    print(f"{Fore.GREEN}1. Listar Cidades")
    print(f"{Fore.GREEN}2. Adicionar cidade")
    print(f"{Fore.GREEN}3. Buscar cidade")
    print(f"{Fore.GREEN}4. Atualizar cidade")
    print(f"{Fore.GREEN}5. Excluir cidade")
    print(f"{Fore.GREEN}0. Sair")
    
def processar_opcao(opcao):
    if opcao == "1":
        print("Mostrar Cidades")
        cidades = ler_cidades()
        for cidade in cidades:
            print(f"{Fore.GREEN}{cidade}")

def executar_sistema():
    exibir_menu()
    opcao = input("Digite a opção desejada: ")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    executar_sistema()

executar_sistema()