# Salvando dados de uma pessoa


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property # Para ler o nome
    def nome(self):
        return self._nome
    
    @property # Definir idade
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nascimento
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2023 - self._ano_nascimento
    
pessoa = Pessoa("Kayque", 2003)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}") # Não é muito cara do PY