import ipaddress

# Endereço
ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 256)

# Rede
ip2 = '192.168.0.0/24'

rede = ipaddress.ip_network(ip2, strict=False) # Aceita qualquer rede que escrever

for ip2 in rede:
    print(ip2) # Todos os ips da /24 printados