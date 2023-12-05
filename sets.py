# Manipulando conjuntos - SETS
# Não permite outro elemento com o mesmo nome

usuarios = {"Ana", "Maria"}
usuarios.add("Felipe")
print(usuarios)

usuario_digitado = input("Digite seu usuario: ")

if usuario_digitado in usuarios:
    print(f"Usuario cadastrado!")
else:
    print(f"Não encontrado")

novos_usuarios = {'Giovanna', 'Kayque', 'Maicom'}

print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios) # Este junta uma variavel com outra
print(todos_usuarios)

usuarios_comuns = usuarios.intersection(novos_usuarios) # Este dá uma interseção
print(f"Inteseção: {usuarios_comuns}")

usuarios_diferentes = usuarios.difference(novos_usuarios) #para ver os usuarios diferentes
print(f"Diferenças: {usuarios_diferentes}")