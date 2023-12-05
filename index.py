nome = input("Digite seu nome: ")
Trabalho = input("Seu trabalho é de: ")
salário = int (input("Recebe quantos por mês: "))
idade = int (input("Digite sua idade: "))
ano = 2023 - idade

message = f"Olá {nome}! Sua idade é de {idade} anos, o que siginfica que você nasceu em {ano}.Você trabalha de {Trabalho}, recebendo {salário}"

print(message)