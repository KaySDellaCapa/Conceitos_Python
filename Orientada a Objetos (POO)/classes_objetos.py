""" 
Classes e objetos - uma classe define as características e comportamentos de um
objeto. Porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los
e eles possuem as características e comportamentos que foram definidos nas classes
"""

# Exemplo:

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado =  acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

# Objeto:

cao_1 = Cachorro("chappie", "amarelo", False) # Constroi a classe e não está acordado
cao_2 = Cachorro("Aladim", "branco e preto") # Está acordado, True

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)