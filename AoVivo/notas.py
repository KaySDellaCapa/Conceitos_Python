# Solicite notas e frequencia de um aluno. Determina sua situação

media = float(input("Digite a média do aluno: "))
freq = float(input("Digite a frêquencia: "))

if media >= 5 and freq >= 75:
    print("Aluno aprovado")
elif media < 5 and freq < 75:
    print("Aluno reprovado")
else:
    print("Aluno em recuperação")