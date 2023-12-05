
#num = int(input("Digite um número: "))                           #O "i" acumula o valor.
#for i in range(1, 11):                                              
 #   resultado = num * i
  #  print(f"{num} x {i} = {resultado}")




senha = input("Digite sua senha: ")

while senha != "123":
    print("Senha incorreta. Tente novamente.")      #para tentar novamente até acertar
    senha = input("Digite sua senha: ")

print("Acesso permitido")