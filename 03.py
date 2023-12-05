tempo = float(input("Digite o tempo (horas): "))
velocidade = float(input("Digite a velocidade média: "))

distancia = tempo * velocidade
litros_usados = distancia / 12

print (f"Velocidade média: {velocidade:.2} km/h")
print(f"Tempo gasto na viagem: {tempo:.2f} horas")
print (f"Distância percorrida: {distancia:.2f} km")
print(f"Litros utilizados: {litros_usados:.2f}")