def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r") # Dentro tem um arquivo agora guardado. "r" de read
    conteudo = arquivo.read() # Aqui já tem o conteudo do arquivo
    arquivo.close() # É importante fechar o arquivo após abrir
    print(conteudo)

def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "w") #Metodo WRITE
    arquivo.write(conteudo)
    arquivo.close()

def adicionar_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "a") # 'a' de APPEND
    arquivo.write(conteudo)
    arquivo.close()

def ler_linha_arquivo(nome_arquivo):
    for linha in open(nome_arquivo, "r"):
        print(linha.strip()) # Strip limpa linhas vazias

ler_arquivo("cidades.txt")
escrever_arquivo("cidades.txt", "carapicuiba\n") # Aqui adicionou, como o append. \n é quebra de linha
# ELE SUBSTITUI TODO O ARQUIVO, POR ISS TOMAR CUIDADO
ler_arquivo("cidades.txt")
adicionar_arquivo("cidades.txt", "sobral")
ler_arquivo("cidades.txt")
ler_linha_arquivo("cidades.txt")