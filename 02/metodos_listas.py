#en python tenemos varios metrodos para tratar las listas

lista = [100, 22, 433, 44, 554, 56, 90, 12]
print(lista)

#ordenar la lista de menor a mayor 
lista.sort()
print(lista)
#ordenar la lista de mayor a menor
lista.sort(reverse=True)
print(lista)

#podemos usar metodo min y max para encontrar el minimo y el maximo de la lista sin importar el oreden

print(min(lista))
print(max(lista))

#podemos saber si un elemento esta en la lista con el metodo in

print(100 in lista)#esto nos regresa un valor booleano

#podemos saber el inice de un elemento en la lista con el metodo index

print(lista.index(100)) 
"""
esto nos regresa el indice del primer elemento que coincida en la lista
si no exixste ningun elemento que coincida en nuestra lista nos dara error
"""




