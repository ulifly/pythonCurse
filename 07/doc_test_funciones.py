"""
en python podemos haer la documentacion y testeo de funciones 
de una forma muy sencilla y util
lo hacemos de la siguiente forma, depues de definir la funcion
agregamos el comentario con la estructura
    explicacion de la funcion

    argumentos

    valor que retorna

y despues podemos acceder a esta documentacion con el nombre de la funcion y help
por ejemplo:
"""

def suma(a,b):
    """
    funcion que suma dos numeros
    :param a: primer numero
    :param b: segundo numero
    :return: la suma de los dos numeros
    """
    return a + b

print(help(suma))#aqui llamamos a la documentacion de la funcion suma

"""
ademas podemos hacer testing de nustras funciones desde la misma documentacion
esto peniendo >>> y despues escribimos el nombre de la funcion y los argumentos a probar
y en el siguiente salto de linea el valor esperado
por ejemplo:
"""

def resta(a, b):
    """
    funcion que resta dos numeros
    :param a: primer numero
    :param b: segundo numero
    :return: la resta de los dos numeros

    >>> resta(2, 1)
    1
    >>> resta(5, 3)
    5

    """
    return a - b

#y podemos probar la funcion desde la consola con -m doctest nombrearchivo
#aqui nos dara un error por que la seguna expresion esperaba 5 y recibe 2
