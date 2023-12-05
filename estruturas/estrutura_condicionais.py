"""
ESTRUTURAS CONDINCIONAIS
Permite um desvio de fluxo de controle, quando determinadas expressoes
lógicas são atendidas

IF - para criar uma estrutura condicional simples, composta por um único
desvio, podemos utilizar a palavra reservada if. O comando irá testar a 
expressão lógica, e em caso de retorno verdadeiro, as ações presentes no bloco
de código do if serão executadas

IF/ELSE - para criar uma estrutura condicional com dois desvios, podemos
utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica
testada no if for verdadeira, então o bloco de código do if será executada
caso contrario o bloco de código do else será executada

ELIF - Em alguns cenarios queremos mais de dois desvios, para isso
podemos utilizar a palavra reservada elif. O elif é composto por uma nova
expressão lógica, que será testada e caso retorne verdadeiro o bloco
de código do elif, será executado. Não existe um número máximo de elifs
porém evite criar grandes estruturas, pois aumenta e complexidade do
código.
"""

MAIOR_IDADE = 18
IDADE_ESPECIAL = 15

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
else:
    print("Nada disso, amigo")

if idade >= MAIOR_IDADE:
    print("Maior de idade")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas")
else:
    print("Na-na-ni-na-não")
