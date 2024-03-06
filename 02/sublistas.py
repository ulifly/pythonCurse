#en python podemos generar sublistas a partir de una lista

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java"]
print(lista_cursos)

#en el siguiente ejemplo, generamos una sublista desde el indice 1 hasta el indice 3, nota el ultimo indice no es tomado en cuenta
sublista = lista_cursos[1:3]
print(sublista)

#podemos generar una sublista desde el indice x y salirnos del rango de la lista, esto no dará error y nos devolverá los datos hasta el ultimo elemento disponible

fuera_de_rango = lista_cursos[1:100]
print(fuera_de_rango)

#también podemos generar una sublista desde el indice 0 hasta el final de la lista

hasta_el_final = lista_cursos[2:]
print(hasta_el_final)

#podemos generar una sublista desde el inicio hasta el indice x

desde_el_inicio = lista_cursos[:2]
print(desde_el_inicio)

#podemos generar una sublista con intervalos pasándole un tercer parámetro

lista_intervalos = lista_cursos[1:4:2]
print(lista_intervalos)

#podemos generar una sublista invertida con el tercer parámetro negativo

lista_invertida = lista_cursos[::-1]
print(lista_invertida)
print(lista_cursos)
