""" .get é uma forma de acessar valores dentro dicionario """

contato = {
    "ksdellacapa@gmail.com": {"nome": "Kayque", "telefone": "1111-1111"}
}

contato["chave"] # KeyError

contato.get("chave") # None
contato.get("chave", {}) # {}
contato.get("ksdellacapa@gmail.com", {}) # "ksdellacapa@gmail.com": 
# {"nome": "Kayque", "telefone": "1111-1111"}