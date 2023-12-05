class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # O arugmento nro_patas está dentro de **kw
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return self.__class__.__name__ # Exibe o nome da classe

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "ave"

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        print("Oi, estou falando")

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        print(Ornitorrinco.__mro__) # Trás a ordem de resolução, se não acha em um sobre para outro
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
  

gato = Gato(nro_patas=4, cor_pelo="preto") # É preciso passar o nome por causa do **kw
print(gato)

ornitorrinco = Ornitorrinco(nro_patas =4, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)
print(ornitorrinco.falar())