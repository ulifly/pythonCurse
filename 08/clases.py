"""
Una clase en Python es una estructura que permite definir un nuevo tipo de objeto. 
Una clase puede contener variables, conocidas como atributos, 
y funciones, conocidas como métodos, que definen el comportamiento del objeto. 
Para crear una instancia de una clase, se utiliza la sintaxis nombre_clase().
para definir una clase se utiliza la palabra clave class.
"""
class Gato:
    sonido = "miau"
    color = ''
    edad = 0            #estos son atributos de la clase
    nombre = ''
    raza = ''

    def maullar(self): # este es un metodo de la clase Gato()
        print(f'{self.nombre} maulla {self.sonido}') 


michi1 = Gato()# esta es una instancia de la clase Gato()
michi1.nombre = "michi"
michi1.edad = 2             #estos son atributos de la instancia
michi1.color = "negro"


print(michi1.__dict__) #para ver los atributos de la instancia

michi1.maullar()#para llamar al metodo de la clases