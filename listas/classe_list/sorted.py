""" .sorted serve para ordenar iteraveis para padronizar """

linguagens = ["Python", "Js", "C", "Java", "C#"]

sorted(linguagens, key=lambda x: len(x))
sorted(linguagens, key=lambda x: len(x), reverse=True)