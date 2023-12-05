import ctypes

print('#' * 60)
pasta = input("Digite o caminho e a pasta a ser ocultada (c:/exemplo/exemplo): ")

# Definindo o atributo do objeto
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('Desenvolvimento de ferramentas 2/ocultar.txt', atributo_ocultar)

if retorno:
    print("Arquivo ocultado...")
else:
    print("Arquivo não ocultado")
    
print('#' * 60)