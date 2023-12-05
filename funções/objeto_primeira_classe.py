""" 
Objetos de primeira classe - em Python tudo é objeto, dessa forma, funções 
também são objetos o que as torna objetos de primeira classe. Com isso podemos
atribuir funções a variaveis, passa-las como parâmetro para funções, usá-las como
valores em estruturas de dados (listas, tuplas, dicionaiorios, etc) e usar como
valor de retorno para uma função (closures)
"""

def somar(a, b):
    return a + b

def exibir_resultados(a,b, funcao):
    resultado = funcao(a, b)
    print(f"O valor da soma entre {a} e {b} é {resultado}")

exibir_resultados(10, 10, somar)