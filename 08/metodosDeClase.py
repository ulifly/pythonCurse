"""
Los métodos de clase en Python son métodos que se definen en una clase 
y se utilizan para realizar operaciones en el ámbito de la clase, 
en lugar de en una instancia específica de la clase. 

Estos métodos se crean utilizando el decorador @classmethod y deben 
tener como primer parámetro la referencia a la clase, que se suele llamar cls 
"""

class Circulo:
    pi = 3.14159265

    @classmethod # Decorador para indicar que es un método de clase
    def area(cls, radio):
        return cls.pi * radio ** 2
    
resultado = Circulo.area(5)
print(resultado) 