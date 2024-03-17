##podemos pasar parametros a las funciones y que en vez de tuplas utilice diccionarios con **

def funcion(**kwargs): #**kwargs es un diccionario que contiene los parametros que se le pasan a la funcion
    print(kwargs)#no es obligatorio que se llame kwargs, puede ser cualquier nombre pero por convencion se llama kwargs
    print(type(kwargs)) #de preferencia seguimos la convencion para que sepamos que es un diccionario

funcion(nombre="Juan", apellido="Perez", edad=30)