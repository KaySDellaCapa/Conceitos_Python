""" 
ABC -
Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo
que fornece a base para definir as classes abstratas, e o nome do módulo é ABC.
O ABC funciona decorando métodos da classe base como abstratas e, em seguida, 
registrando classes concretas como implementações de base abstrata. Um método
se torna abstrato quando decorado com: @abstractmethod
"""
from abc import ABC, abstractmethod

class Controle_remoto(ABC): # extensão de ABC
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass

class Controle_tv(Controle_remoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")
        
class Controle_ar_condicionado(Controle_remoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")


controle = Controle_tv()
controle.ligar()
controle.desligar()

controle = Controle_ar_condicionado()
controle.ligar()
controle.desligar()