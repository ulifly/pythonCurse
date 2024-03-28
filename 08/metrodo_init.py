"""
En Python, el método __init__ es un método especial que se utiliza para 
inicializar los atributos de un objeto cuando se crea una instancia de una clase. 
Este método se llama automáticamente después de crear el objeto 
y se le pasan los parámetros que se hayan especificado al instanciar la clase. 
Si no se pasan todos los parámetros, los que falten recibirán un valor por defecto, 
al igual que en cualquier otra función. 
El primer parámetro del método __init__ debe ser self, 
que es una referencia al objeto que se está creando.
"""

class dinosaurio:

    def __init__(self, especie, tipo, ):
        self.especie = especie
        self.tipo = tipo

triceratops = dinosaurio("Triceratops", "Terrestre")
pterodactilo = dinosaurio("Pterodactilo", "Terrestre")

print(triceratops.__dict__)
