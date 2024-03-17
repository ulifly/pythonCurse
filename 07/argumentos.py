"""
podemos recibir varios argumentos en una funcion por ejemplo una coleccion de datos
como una lista, tupla, diccionario, etc.
"""
calificaciones = [8, 10, 9, 9 ,8]

def promedio(args):
    return sum(args) / len(args)#la funcion sum recibe una lista y devuelve la suma de todos los elementos de la lista
                                #la funcion len recibe una lista y devuelve el numero de elementos de la lista
resultado = promedio(calificaciones)
print(resultado)

"""
sin embargo tambien podemos recibir un numero indeterminado de argumentos aunque no sean colecciones
para esto tenemos que poner un asterisco antes del nombre de la variable.
y podemos recibir un numero indeterminado de argumentos en una funcion 
"""

def promedio2(*argumentos):#el asterisco antes del nombre de la variable indica que podemos recibir un numero indeterminado de argumentos
    print(type(argumentos))#el tipo de dato que retorna es una tupla, por lo tanto podemos recorrerla con un ciclo for
    return sum(argumentos) / len(argumentos)

resultado = promedio2(8, 10, 9, 9, 8) #como podemos notar aqui son datos de tipo entero y no una coleccion
print(resultado)

"""
tambien podemos recibir argumentos ademas de los argumentos con asterisco
es decir una cantidad de argumentos definida y los argumentos que convertira en una tupla

"""

def combinados(c1, c2, *args): #por convencion se utiliza args
    print(c1)
    print(c2)
    print(args)

combinados(1, 2, 3, 4, 5, 6) #los argumentos con el asterisco se convertiran en una tupa

"""
tambien podemos agregar parametos por defecto
"""

def combinados2(c1, c2, *args, default=10):
    print(c1)
    print(c2)
    print(args)
    print(default)

combinados2(1, 2, 3, 4, 5, 6) #los argumentos con el asterisco se convertiran en una tupa

"""
podemos tambien agregar argumentos con el nombre
"""

