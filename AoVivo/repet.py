# Exiba a tabuada desse número em intervalo determinado
# Inicio e fim da tabuada

numero = int(input("Digite um número: "))
inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

for contador in range (inicio, fim+1): # Pode por str dependendo até onde quer ir. 0 +1 é para ir até 10
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")