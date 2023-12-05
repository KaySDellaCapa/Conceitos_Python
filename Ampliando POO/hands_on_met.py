class Pessoa:
    def __init__(self, nome=None, idade=None): # Valor padrão para o calculo
        self.nome = nome
        self.idade = idade
    
    # Método de fábrica para calcular idade automaticamente
    @classmethod # Transforma em método de classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade) #cls é referencia para a classe
    
    @staticmethod # Método estatico
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("Kayque", 20)
# print(p.nome, p.idade)

p2 = Pessoa().criar_apartir_data_nascimento(2003, 5, 20, "Kayque")
print(p2.idade, p2.nome)

print(Pessoa.e_maior_idade(18)) # True
print(Pessoa.e_maior_idade(8)) # False
