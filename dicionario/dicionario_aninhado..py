""" 
Dicinários podem armazenar qualquer tipo de objeto Python, como valor
desde que a chave para esse valor seja um objeto imutavel como
(string e numeros)
"""
contato = {
    "ksdellacapa@gmail.com": {"nome": "Kayque", "telefone": "1111-1111"}
}

print(contato["ksdellacapa@gmail.com"]["telefone"])