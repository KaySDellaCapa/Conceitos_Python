""" 
Herança simples - Quando uma classe filha herda apenas uma classe pai, ela é
chamada de herança simples
"""
class A:
    pass

class B(A):
    pass 

""" 
Herança múltipla - Quando uma classe filha herda de várias classes pai, ela é
chamada de herança múltipla (não são todas as linguagens que implementam)
"""
class A:
    pass

class B:
    pass

class C(A, B):
    pass