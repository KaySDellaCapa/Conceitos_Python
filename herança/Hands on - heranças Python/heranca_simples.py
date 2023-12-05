class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor") # Funciona em todos
    
    def __str__(self):
        return self.cor # Implementação

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # Chama a implementação da classe
        # O que quer chamar da classe
        # Super pode ser chamado antes ou depois. Ele apenas extende o comportamento
        self.carregado = carregado
    def esta_carregado(self):
        print(f'{"Sim," if self.carregado else "Não"} estou carregado') # Não funciona em todos pois é uma func do caminhão

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "gfd-8712", 8, True) # False de não estar carregado
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print(moto)
print(carro)