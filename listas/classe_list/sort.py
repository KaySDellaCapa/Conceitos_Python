""" .sort pode embaralhar e passar o argumento REVERSE e KEY """

linguagens = ["Python", "Js", "C", "Java", "C#"]
linguagens.sort()

linguagens = ["Python", "Js", "C", "Java", "C#"]
linguagens.sort(reverse=True)

linguagens = ["Python", "Js", "C", "Java", "C#"]
linguagens.sort(key=lambda x: len(x)) # Ordem crescente

linguagens = ["Python", "Js", "C", "Java", "C#"]
linguagens.sort(key=lambda x: len(x), reverse=True) # Ordem decrescente