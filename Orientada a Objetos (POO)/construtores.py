""" 
Método construtor - o método construtor sempre é executado quando uma nova instance
da classe é criada. Nesse método incializamos o estado do nosso objeto. Para 
declarar o método construtor da classe, criamos um método com nome __init__
"""
# Exemplo:

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


        