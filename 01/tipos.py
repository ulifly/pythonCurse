#tipos de datos en python



#String
"""
en python podemos usar comillas simples o comillas dobles para dafinir un string
ademas podemos integrarar comillas al string siempre y caundo sean diferentes a las usadas
para definir el strig, es decir si definimos el string con comillas simples podremos introducir comillas dobles 
al string como en el siguiente ejemplo:
"""
este_es_un_string = '"este es un ejemplo de un string con comillas"'
este_es_otro_string = "'este es otro ejemplo '"
print(este_es_un_string)
print(este_es_otro_string)

# en python tambien podemos hacer strings con saltos de linea usando triples comillas muy similar a los comentarios multilinea

string_multilinea = """ este es un ejemplo de un string
que tiene saltos de linea
asi podemos ejemplificar como
es posible hacer esto
"""

print(string_multilinea)

#Int

"""
en python podemos definir una variable pasandole un numero entero y realizar operaciones con el
podriamos hacer inclusi division y de un numero entero nos daia de resultado un numero flotante
"""

numero_entero = 23 + 4

print(numero_entero)

numero_entero_resultante_flotante = 56 / 3

print(numero_entero_resultante_flotante)

"""
sin embargo podemos forzar a que el resultado de la division
sea un numero entero pasandole el operador // envez de /
"""
numero_entero_resultante_flotante2 = 56 // 3

print(numero_entero_resultante_flotante2)

#Float

numero_flotante = 3.14
print(numero_flotante)

#Bool

"""
los valores booleanos como en cualquier lenguaje de programacion
nos regresan solo 2 resultados verdadero o falso

"""

dato_booleano = True
print(dato_booleano)


#type, podemos saber que tipo de dato tenemos en una variable con la funcion type

print(type(dato_booleano))
print(type(numero_flotante))
print(type(numero_entero))