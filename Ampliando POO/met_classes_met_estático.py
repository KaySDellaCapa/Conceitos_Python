""" 
Métodos de classe -
Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao
estado da classe, pois recebem um parâmetro que aponta para a classe e não
para a instância do objeto.

Métodos estáticos -
Um método estático não recebe um prineiro argumento explícito. Ele também é um
método vinculado à classe e não ao objeto da classe. Este método não pode acessar
ou modificar o estado da classe. Ele está presente em uma classe porque faz
sentido que o método esteja presente na classe.
"""
""" 
Métodos de classe x Métodos estáticos -
* um método de classe recebe um primeiro parâmetro que aponta para a classe,
enquanto um método estático não.
* um método de classe pode acessar ou modificar o estado da classe, enquanto
um método estático não pode acessa-lo ou modificá-lo.
"""
""" 
Quando utilizar método de classe ou estático -
* geralmente usamos o método de classe para criar métodos de fábrica.
* geralmente usamos métodos estáticos para criar funções utilitárias.
"""