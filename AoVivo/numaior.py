# Solicite dois números e exiba o maior

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}")
elif numero1 == numero2:
    print("Tem o mesmo valor")
else:
    print(f"O número {numero2} é maior que o número {numero1}")