"""
La función zip() en Python se utiliza para combinar elementos 
de dos o más iterables en un nuevo iterable. 
Toma como argumento dos o más objetos iterables y devuelve 
un nuevo iterable cuyos elementos son tuplas que contienen 
un elemento de cada uno de los iteradores originales.
"""

paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]

paises_y_poblaciones = zip(paises, poblaciones)
print(paises_y_poblaciones) #este es un objeto zip no imprimira la lista sino el objeto 
res = tuple(paises_y_poblaciones)#convertimos el zip en tupla para poder imprimirlo
print(res)

#se puede hacer en una sola linea

peliculas = ["Titanic", "Forest Gump", "Avengers"]
oscares = [ 5, 3, 1]

lista_combinada = tuple(zip(peliculas, oscares))
print(lista_combinada)


"""
La función zip() es especialmente útil en bucles for
para acceder a los elementos de dos o más iterables simultáneamente.
"""
for pelicula, oscar in zip(peliculas, oscares):
    print(f"{pelicula} tiene {oscar} oscar")

#si alguno de los iterables es más largo que el otro, estos elementos seran omitidos
    
marca_carros = ["Ford", "BMW", "Fiat", "Renault", "Ferrari", "Porshe"]
modelos_carros = ["Mustang", "X5", "500", "Kwid"]

automoviles = tuple(zip(marca_carros, modelos_carros))
print(automoviles)