""" 
Método destrutor - o método destrutor sempre é executado quando uma instância
(objeto) é destruída. Destrutores em Python não são tão necessários quando tem C++
porque o Python tem um coletor de lixo que lida com o gerenciamento de memória
automaticamente. Para declarar o método destrutor da classe, criamos um método 
com o nome __del__
"""

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro("Zeus", "branco", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

criar_cachorro()

# As variaveis morrem com o del. O nome "Zeus" deixou de existir