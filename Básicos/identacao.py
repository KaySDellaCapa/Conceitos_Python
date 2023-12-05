"""
Identar um código é uma forma de matner o código fonte mais legivel
e manutenivel. Mas em Python ela exerce um segundo papel, através da
identação o interpretador consegue determinar onde um bloco de comando
incia e onde ele termina.

As linguagens de programação costumar utilizar caracteres ou palavras 
reservadas para terminar o inicio e fim do bloco. Em Java e C por exemplo
se utiliza chaves.

Existe uma convenção em Python que define as boas práticas de código.
Nesse documento é indicado utilizar 4 espaços em branco por nivel de 
indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em 
branco.

"""

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")
        print("Obrigado por preferir nosso banco")
    else:
        print("Recusado")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(700) # Esse é o valor de VALOR em DEF SACAR