"""
La herencia múltiple en Python se refiere a la capacidad de una clase hija de heredar 
de múltiples clases padres. A diferencia de otros lenguajes de programación, 
como Java y C#, Python permite la herencia múltiple, 
lo que significa que una clase puede heredar atributos y métodos de varias clases.

Sin embargo, la herencia múltiple puede plantear un problema 
cuando varias clases padres tienen los mismos atributos o métodos. 
En estos casos, Python dará prioridad a las clases más a la izquierda 
en el momento de la declaración de la subclase.

"""

class Mascota:
    def comer(self):
        print("Comiendo")
    def dormir(self):
        print("Durmiendo")

class Felino:
    def cazar(self):
        print("Cazando")

class Gato(Mascota, Felino):#se separan con coma las clases de las que hereda
    def maulla(self):
        print("Maullando")

felix = Gato()
felix.comer()
felix.dormir()
felix.maulla()
felix.cazar()
print(felix.__dict__)