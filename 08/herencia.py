"""
La herencia en Python es un mecanismo que permite a una clase heredar 
los atributos y métodos de otra clase. 
Esto significa que una clase hija puede aprovechar y reutilizar el código de una clase padre, 
evitando así la duplicación de código y facilitando la organización 
y estructura del programa.

Para implementar la herencia en Python, se utiliza la sintaxis class ClaseHija(ClasePadre):
donde ClaseHija es la clase que hereda y ClasePadre es la clase de la cual 
se heredan los atributos y métodos. 
La clase hija puede agregar nuevos atributos y métodos, o incluso sobrescribir los existentes.
"""

class mascota: #clase padre
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")

class perro(mascota): #clase hija
    def ladra(self):
        print("Ladra")

firulais = perro()
firulais.comer()
firulais.dormir()
firulais.ladra()
print(firulais.__dict__)

class gato(mascota): #clase hija
    def maulla(self):
        print("Maulla")

felix = gato()
felix.comer()
felix.dormir()
felix.maulla()