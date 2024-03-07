#podemos asignar a variables los datos de una tupla

numeros = (1,2,3,4)
uno, dos, tres, cuatro = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

#si la tupla contiene mas variables que las que se están asignando nos dará un error

#pero podemos asignar a las variables sobrantes a una lista con el operador *

numeros_2 = (1, 2, 3, 4, 6, 7, 8, 9, 10)
uno, dos, *resto_valores= numeros_2
print(uno)
print(dos)
print(resto_valores)

#podemos omitir el resto de valores con *_

uno, dos, *_ = numeros_2
print(uno)
print(dos)

