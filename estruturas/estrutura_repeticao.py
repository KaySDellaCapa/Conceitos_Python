"""
O que são estruturas de repetição? - são estruturas utilizadas para repetir
um trecho de código, um determinado número de vezes.
Esse número pode ser conhecido previamente ou determinado através de
uma lógica
"""
# Receba um número do telcado e exiba os 2 números seguintes
# Jeito básico

a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)

"""
Comando for - O comando é usado para percorrer um objeto iterável.
Faz sentido usar for quando sabemos o número exato de vezer que nosso
bloco de código deve ser executado, ou quando desejams percorrer um
objeto iterável
"""
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # Isso é uma quebra de linha
    print("Executando final do laço")
