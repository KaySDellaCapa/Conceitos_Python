""" 
Atributos do objeto -
Todos os objetos nascem com o mesmo número de atributos de classe e de 
instância. Atributos de instância são diferentes para cada objeto (cada objeto
tem uma cópia), já os atributos de classe são compartilhados entre os objetos.
"""
# Exemplo:

class Estudante:
    escola = "DIO" # Vai ser lido abaixo

    def __init__(self, nome, numero_matricula): # O construtor
        self.nome = nome
        self.numero_matricula = numero_matricula

    def __str__(self):
        return f"{self.nome} ({self.numero_matricula}) - {self.escola}"
    
def mostrar_valores(*objs):
    for objs in objs:
        print(objs)
    
aluno_1 = Estudante("Kayque", 56461)
aluno_2 = Estudante("Giovanna", 17323)

print(aluno_1)
print(aluno_2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Alura" # Muda dos dois pois reflete no Estudante, que ambos tem
aluno_1.numero_matricula = 12311
aluno_2.numero_matricula = 33344
mostrar_valores(aluno_1, aluno_2) # Com modificação