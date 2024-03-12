#podemos eliminar elementos de un diccionario con el metodo del

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

del diccionario["c"]

print(diccionario)

#podemos eliminar un diccionario con el metodo pop recibiendo el elemento que estamos eliminando

elementoEliminado = diccionario.pop("a")
print(elementoEliminado)
print(diccionario)

#podemos eliminar todos los elementos de un diccionario con el metodo clear

diccionario.clear()
print(diccionario)


