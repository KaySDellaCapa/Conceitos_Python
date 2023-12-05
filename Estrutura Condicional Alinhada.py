#anos_experiencia= int(input("Digite os anos de experiência: "))

#if anos_experiencia == 0:
 #   nivel="Estagiario"
#elif anos_experiencia <= 3:
 #   nivel = "Junior"
#elif anos_experiencia <= 8:
 #   nivel = "Pleno"
#else:
#    nivel = "Sênior"

#print(f"Você é um desenvolvedor do nivel: {nivel}")

nota = float(input("Digite sua nota: "))
frequencia = float(input("Digite a frequência: "))

if nota >= 5 and frequencia >= 75:
    situacao = "aprovação"
elif nota >= 5 or frequencia >= 75:
    situacao = "recuperação"
else:
    situacao = "reprovação"

print(f"A situação que o aluno(a) se encontra é de: {situacao}")