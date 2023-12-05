def ler_cidades():
    cidades = []
    for linha in open("cidades.txt", "r"):
        cidades.append(linha.strip()) #deixar todos os nomes em minusculos
    return cidades