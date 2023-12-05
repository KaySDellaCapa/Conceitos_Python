""" 
Função enumarate - é necessario saber qual p índice do objeto dentro do
laço for. Para isso podemos usar a função enumerate
"""
carros = {"gol", "celta", "palio"}

for i, carro in enumerate(carros):
    print(f"O carro {i} é {carro}")