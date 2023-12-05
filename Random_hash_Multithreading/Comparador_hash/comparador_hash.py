import hashlib

arquivo1 = 'Random_hash_Multithreading/Comparador_hash/a.txt'
arquivo2 = 'Random_hash_Multithreading/Comparador_hash/b.txt'


hash1 = hashlib.new('ripemd160') #Passa uma string para receber o algoritmo que vamos usar
hash1.update(open(arquivo1, 'rb').read()) # Faz a comparação do hash. 'rb é modo leitura binario

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb'). read())

if hash1.digest() != hash2.digest():
    print('#'*60)
    print(" "*60)
    print(f"O arquivo === {arquivo1} === é diferente do arquivo === {arquivo2}")
    print("O hash do arquivo a.txt é: ", hash1.digest) # Resume e mostra em hexadecimal
    print("O hash do arquivo b.txt é: ", hash2.digest)
    print(" "*60)
    print('#'*60)
else:
    print('#'*60)
    print(" "*60)
    print(f"\nO arquivo === {arquivo1} === é igual o arquivo === {arquivo2} ")
    print("O hash do arquivo a.txt é: ", hash1.digest) # Resume e mostra em hexadecimal
    print("O hash do arquivo b.txt é: ", hash2.digest)
    print(" "*60)
    print('#'*60)