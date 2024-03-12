"""
los diccionarios en python son colecciones de datos como las listas o las tuplas 
con la difrencia de que los diccionarios tienen un orden especifico 
y no se accede a los datos por su posicion, sino por su llave
la llave puede ser cualquier objeto inmutable de pyton, como un
string, un entero, un flotante o una tupla
un diccionario puede contener cualquier tipo de dato
los diccionarios se definen con llaves {} o con el metodo dict()

"""

nuevoDiccionario = {
    "nombre": "Tony", 
    "apellido": "Stark", 
    "edad": 45
    }

diccionario2 = dict(
    nombre="Peter", 
    apellido="Parker", 
    edad=25
    )

print(nuevoDiccionario)
print(diccionario2)

#el equivalente a un json en python es un diccionario
#podemos utilizar classes como llaves tambien

#para acceder a los valores de un diccionario usamos []

nombre2 = diccionario2 ["nombre"]
print(nombre2)

#podemos agregar nuevos valores al diccionario

nuevoDiccionario["Heroe"] = "USA"
print(nuevoDiccionario)

#podemos modificar los valores de un diccionario

nuevoDiccionario["Heroe"] = "Ironman"
print(nuevoDiccionario)

#podemos eliminar valores del diccionario con pop

nuevoDiccionario.pop("edad")
print(nuevoDiccionario)

#podemos eliminar los datos del diccionario por completo con el metodo clear

nuevoDiccionario.clear()
print(nuevoDiccionario)

#podemos obtener la cantidad de elementos del diccionario con len

print(len(diccionario2))

#podemos obtener todas las llaves del diccionario con keys()

print(diccionario2.keys())

#podemos obtener todos los valores del diccionario con values()

print(diccionario2.values())

#podemos obtener todos los elementos del diccionario con items()
print(diccionario2.items())

"""
podemos usar el metodo get para obtener un valor del diccionario 
en vez del usar corchetes, pues si usamos corchetes y no existe el valor
nos dara error, pero con get podemos obtener un valor que no exista
si no existe el valor devuelve None
"""

#la siguiente linea dara error
#calificaciones = diccionario2["calificaciones"]

calificaciones = diccionario2.get("calificaciones")

print(calificaciones)

#podemos pasar un valor por defecto al metodo get

calificaciones = diccionario2.get("calificaciones", "No existe")
print(calificaciones)

#podemos iterar sobre una lista con for para generar un diccionario

#esta es una lista de nombres
usuarios = { 'Eduardo', 'Maria', 'Juan', 'Jose' }

diccionariox = { usuario:position + 1 for position, usuario in enumerate(usuarios) }

print(diccionariox)