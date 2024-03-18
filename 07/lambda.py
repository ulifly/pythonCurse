"""
las funciones lambda son funciones anonimas, es decir, que no tienen nombre
son utiles cuando se necesita una funcion que solo se usa una vez
por ejemplo, cuando se necesita una funcion que suma dos numeros y no se necesita
ninguna otra funcion que realice esa tarea, se puede crear una funcion lambda
que realice esa tarea y luego se puede llamar a esa funcion lambda desde cualquier
lugar del codigo.
podemos crear una funcion lambda con la palabra lambda y luego los parametros que
necesitemos, y luego el cuerpo de la funcion, que en este caso es una expresion
que se va a ejecutar.
la funcion lambda se estructura escribeindo la pabala reservada lambda los parametros dos puntos 
y el cuerpo de la funcion.
"""
#  variable =         lambda  <parametros> : <cuerpo de la funcion>
celcius_a_farenheit = lambda     c         :        c * 1.8 + 32  #la funcion lambda tine return implicito

#y la mandamos a llamar con la variable

print(celcius_a_farenheit(34))

