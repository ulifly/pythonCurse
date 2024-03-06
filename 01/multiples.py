# podemos obtener multiples variables en una sola linea

nombre, apellido, edad = "Ulises", "Desentis", 28

"""
es recomendable solo obtener multiples variables si estas estan relacionadas entre si 
y que no sean muchas o el codigo se volvera dificil de leer y de mantener

"""

# podemos imprimir multiples variables en una sola linea 
print(nombre, apellido, edad)

# podemos utilizar la funcion sep para elegir un separador a la hora de imprimir multiples variables
print(nombre, apellido, edad, sep="-")

