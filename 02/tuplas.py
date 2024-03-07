"""
Las tuplas en python son como listas pero con una diferencia, 
las tuplas no se pueden modificar, es decir, no se pueden agregar ni eliminar elementos.
esto es una ventaja a nivel de ejecucion pues al ser datos de solo lectura
se almacenan en memoria en un espacio read only lo cual lo hace mucho mas rapido
"""
#las tuplas se declaran con parentesis

tupla1 = (1,2,3,4,5)

#se puede acceder a los elementos de una tupla igual que a una lista

cursos = ("Python", "Django", "Flask", "Ruby on Rails", "Java", "C++", "C#", "PHP", "Swift", "Kotlin", "Java Script")
primercurso= cursos[0]
print(primercurso)
ultimocurso = cursos[-1]
print(ultimocurso)

# al igual que en las listas se pueden generar sub tuplas apartir de otras tuplas

primerosCursos = cursos[0:3]
print(primerosCursos)

#tambien se pueden crear listas a partir de tuplas y viceversa para eso usamos la funcion list() o tuple()

cursos_lista = list(cursos)
print(cursos_lista)
print(type(cursos_lista))

cursos_tupla = tuple(cursos_lista)
print(cursos_tupla)
print(type(cursos_tupla))








