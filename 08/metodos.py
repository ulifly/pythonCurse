"""
podemos usar metodos para inicializar instancias de clase
asi mantenern un standar en la creacion de objetos
"""

class Dragon:
    def inicializar(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age


tiamat = Dragon()
tiamat.inicializar('Tiamat', 'Rojo', 300)

print(tiamat.__dict__)

"""
esta no es la mejor forma de hacerlo pero sirve para comprende python
la mejor forma de hacer esto es usar el metodo __init__
"""