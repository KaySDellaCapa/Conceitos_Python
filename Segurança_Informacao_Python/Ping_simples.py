import os #Importa módulo ou biblioteca que integra os programas e recursos da IDE

print("-" * 60)

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print("-" * 60)

os.system('ping -n 6{}'.format(ip_ou_host)) # Trás todos os comandos ligados ao sistema
# As chaves vão ter o ip escrito, e o format vai formatar ip_host, para poder caber nas chaves

print("-" * 60)

