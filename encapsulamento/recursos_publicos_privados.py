""" 
Modificadores de acesso - 
Em linguagens como Java e C++, existem palavras
reservadas para definir o nivel de acesso ao atributos e métodos da classe.
Em Python não temos palavras reservadas, porém usamos convenções no nome do
recurso, para definir se a variável é pública ou privada
"""

""" 
Definições -
Público: Pode ser acessado fora da classe
Privado: Pode ser acessado pela classe
"""

""" 
Público/Privado -
Todos os recursos são públicos a menos que o nome inicie com underline. Ou seja,
o interpretador Python não irá garantir a proteção do recurso, mas por ser uma 
convenção amplamente adotada na comunidade, quando encontramos uma variável
e/ou método com nome iniciado por underline, sabemos que não deveríamos 
manipular o seu valor diretamente, ou invocar o método fora do escopo da 
classe.
"""

# Exemplo:

class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
    
    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass