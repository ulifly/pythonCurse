"""
La sobreescritura de métodos en Python se refiere a la capacidad de una clase hija 
de proporcionar su propia implementación de un método que ya está definido en la clase padre. 
Esto permite modificar o extender el comportamiento del método en la clase hija 
sin afectar a la clase padre.

Para que se produzca la sobreescritura de un método, 
es necesario que tanto la clase padre como la clase hija tengan un método con el mismo nombre. 
Cuando se llama al método en una instancia de la clase hija, 
Python ejecutará la implementación del método de la clase hija 
en lugar de la implementación del método de la clase padre.
"""
class Animal:
    def hablar(self):
        print("Hola")

class Perro(Animal):
    def hablar(self):
        print("Guau")


class Gato(Animal):
    def hablar(self):
        print("Miau")

felix = Gato()
felix.hablar()

firulais = Perro()
firulais.hablar()