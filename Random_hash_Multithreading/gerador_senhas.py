import random
import string

print('-'*60)
tamanho = int(input("Qual o tamanho de senha que deseja: ")) # Por segurança, 16 

chars = string.ascii_letters + string.digits + '!@#$%¨&*()-=+.,;?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
print('-'*60)
# Random.Choice retorna lista com caracteres randomicos, pega cada um do chars
# e gera uma nova letra, número, simbolo aleatório
# Gira até 16 caracteres