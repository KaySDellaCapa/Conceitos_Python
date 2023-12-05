"""
A classe String do Python é famosa por ser rica em metódos e possuir uma
interface muito fácil de trabalhar.
Em algumas linguagens manipular sequências de caracteres não é um 
trabalho trivial, porém em Python é muito simples
"""

curso = "pYthon"

print(curso.upper())
# PYTHON

print(curso.lower())
# python

print(curso.title())
# Python

print(curso.strip())
# "Python"

print(curso.lstrip())
# "Python   "

print(curso.rstrip())
# "   Python"

print(curso.center(10, "#"))
# "##Python##"

print(".".join(curso))
# "P.y.t.h.o.n"