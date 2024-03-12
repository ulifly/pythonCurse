#metodo split sirve para convertir un string en una lista de palabras
lenguajes = "Python Java C++ C#" 
lenguajes_lista = lenguajes.split() 
print(lenguajes_lista)

"""
el metodo split toma en ceunta los espacios para separara cada elemento de la lista
sin embargo podemos pasarle como argumento algun caracter que los separa para que
el metodo lo tome en cuenta como en el sig ejemplo
"""
carros = "Mustang-Kwid-Beattle-Meriva"
carros_lista = carros.split("-")#aqui le decimos que tmo en ceunta el - en vez de el espacio
print(carros_lista)


#metodo join sirve para unir una lista de strings en un solo string
frutas = ["manzana","pera","uva"]
frutas_string = " ".join(frutas)#recive el caracter que queramos usar como separador ene ste caso espacio
print(frutas_string)
print(type(frutas_string))


#metodo replace sirve para reemplazar un string por otro string
#metodo upper sirve para convertir un string en mayusculas

#metodo strip sirve para quitar los espacios en blanco al inicio y al final de un string
