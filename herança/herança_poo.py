""" 
O que é herança? - em programação herança é a capacidade de uma classe filha 
derivar ou herdar as características e comportamentos da classe pai (base)
"""

""" 
Benefícios da herança -
* Representa bem os relacionamentos do mundo real.
* Fornece reutilização de código, não precisamos escrever o mesmo código repetida
vezes. Além disso, permite adicionar mais recursos a uma classe sem modifica.
* É da natureza transitiva, o que significa que, se a subclasse B herdar da 
classe A, todas as subclasses de B herdarão automaticamente da classe A.
"""

# Sintaxe da herança:

class A:
    pass

class B(A):
    pass 