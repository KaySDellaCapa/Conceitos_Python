""" 
Args e kwargs - podemos combinar parametros obrigatórios com args e kwargs.
Quando esses são definidos, o método recebe os valores como tupla e dicionario
respectivamente
"""

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n". join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.item()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better than ugly", autor="Tim Peters", ano=1999)

