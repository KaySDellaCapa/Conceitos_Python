"""
Função enumarate - Às vezes é necessario saber qual o índice do objeto
dentro do laço for. Para isso podemos usar a função enumerate.
"""
carros = ["gol", "celta", "palio"]

for i, carro in enumerate(carros):
    print(f"{i}: {carro}")