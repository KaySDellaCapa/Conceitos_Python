import os
import time

with open("Segurança_informacao_Python/multiplos_txt/host.txt") as file:
    dump = file.read().splitlines() # Vai ler. O split organiza

    for ip in dump:
        print('verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2{}'.format(ip)) # Com apenas 2 pacotes o disparo é mais rápido
        print('-' * 60)
        time.sleep(5)