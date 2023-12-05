# Poliformismo se comporta de varias maneiras diferentes, porem chamando o mesmo método


class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar() #Implementação "Voando..."

class Avestruz(Passaro):
    def voar(self):
        print("Não voa!")

class Aviao(Passaro): # Se voa, não precisa criar classe decolar, apenas implemente
    def voar(self):
        print("Avião está decolando...") # Esse é o voar do avião

def plano_de_voo(obj):
    obj.voar() # Para simplesmente chamar o obj voar

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(Aviao())