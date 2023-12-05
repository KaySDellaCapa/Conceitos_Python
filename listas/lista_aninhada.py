"""" 
Lista aninhada - podem armazenar todos os tipos de objetos Python,
portanto podems ter listas que armazenam outras listas. Com isso 
podemmos criar estruturas bidimensionais (tabelas), e acessar
informando os índices de linha e coluna.
"""

matriz = [
    [1, "a", 2],
    ["b", 3, 4]
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0,0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"