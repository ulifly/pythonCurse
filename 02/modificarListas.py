#podemos modificar las listas como añadir elementos, eliminar elementos, modificar elementos

lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java Script", "c#"]
print(lista_cursos)

#podemos conocer la longitud de la lista con len

print(len(lista_cursos))

#añadir elementos a la lista con append
lista_cursos.append("C++")
print(lista_cursos)
print(len(lista_cursos))

#añadir elementos a la lista con insert, podemos usar este método para añadir elementos en una posición determinada y recorre el resto de los elementos

lista_cursos.insert(2, "PHP")
print(lista_cursos)
print(len(lista_cursos))

#podemos añadir elementos a la lista con extend, este método añade una lista completa a la lista original

lista_cursos2 = ["C", "pygame", "rust"]
lista_cursos.extend(lista_cursos2)
print(lista_cursos)
