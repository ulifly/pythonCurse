"""
La función super() en Python se utiliza para llamar a métodos de la clase 
padre (superclase) desde una subclase. 
Esto es especialmente útil cuando se trabaja con herencia, 
ya que permite acceder a los métodos y atributos de la superclase dentro 
de la subclase y extender o modificar su comportamiento.

Al utilizar super(), se puede invocar un método de la clase padre 
desde la clase hija sin tener que hacer referencia explícita al nombre 
de la clase padre. Esto facilita la escritura de código más flexible y mantenible, 
ya que evita la duplicación de código y permite que las subclases 
aprovechen la funcionalidad de las superclases
"""
class Animal:
    def hablar(self):
        print("Hola")

class Perro(Animal):
    def hablar(self):
        print("Guau")
        super().hablar()

scooby = Perro()

scooby.hablar()


