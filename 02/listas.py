#en python podemos usar listas, las listas son una estructura de datos que nos permiten almacenar varios valores en una sola variable


#podemos definir una lista con []
lista = [1,2,3,4,5]

#también podemos definir una lista vacía de la siguiente manera
lista_vacia = []

#podemos definir una lista de esta otra forma

lista_vacia2 = list()

"""
#las listas en python son como los arreglos en otros lenguajes de programación 
de igual forma sus elementos están en indices y el primer indice es 0 
"""
#                   0        1      2          3         4        
lista_cursos = ["Python", "Java", "C++", "JavaScript", "PHP"]

#podemos acceder a los elementos de la lista con indices
primer_curso = lista_cursos[0]
segundo_curso = lista_cursos[1]
print(primer_curso)
print(segundo_curso)

#también podemos usar los indices negativos para acceder a los elementos de la lista desde atrás

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)
penultimo_curso = lista_cursos[-2]
print(penultimo_curso)

#podemos modificar los elementos de la lista
print(lista_cursos)
lista_cursos[4] = "Ruby"
print(lista_cursos)