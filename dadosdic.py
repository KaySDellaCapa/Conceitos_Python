# Manipulando dicionarios

# Com cada elemente em um linha fica mais facil de ler

cliente = {"nome":  "Kayque", 
           "cidade": "Raposo",
           "ano_nasc": 2003,
           "ativo": False

} # Chave e valor. É o que dá poder grande a ele.
        
print(cliente["nome"]) # Aqui pode pedir para ler coisas especificas

cliente["ano_nasc"] = 1988 # Aqui estou atualizando um dado
print(cliente)

del cliente ["cidade"] # Caso queira excluir um dado do dic, no caso a cidade
print(cliente)

if "ano_nasc" and "nome" in cliente:
    print("Dados encontrados")
else:
    print("Dados indisponiveis")

# Lista de valores
for valor in cliente.values(): # Neste lista todos os valores no dicionario 
    print(valor)

# Lista de chaves
for chave in cliente.items(): # Neste interou pela chave / valor
    print(chave)