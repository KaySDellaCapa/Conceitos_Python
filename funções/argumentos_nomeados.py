""" 
Argumentos nomeados - Funções também podem ser chamadas usando argumentos
nomeados da forma chave = valor
"""

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC1234")