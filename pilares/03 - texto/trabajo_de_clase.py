"""
- Usando *Fstring*, escribir un programa que pregunte el nombre 
  del usuario y  después de que el usuario lo introduzca muestre por 
  pantalla 'nombre' tiene 'n' letras donde 'nombre' es el nombre del usuario 
  y 'n'es el número de letras que tiene el nombre. 
"""

# usuario = input('ingresa tu nombre de usuario: ')
# no_letras = len(usuario)
# print(f'{usuario} tiene {no_letras} letras')

"""
- Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
  donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
  (por ejemplo +34-913724710-50). Escribir un programa que pida al usuario 
  un número de teléfono con este formato y muestre por pantalla el número de teléfono 
  sin el prefijo ni la extensión.
"""

# numero_telefonicio = input( 'ingrese en numero telefonico en el formato prefijo-número-extension: ')
# numero_telefonicio = numero_telefonicio[4:13]
# print(numero_telefonicio)


"""
- Escribir un programa que pida al usuario que introduzca una frase  
  y muestre por pantalla la frase invertida.

"""

# frase = input('ingrese una frase, la vamos a invertir: ')
# print(frase[::-1])

"""
- Escribir un programa que pregunte el nombre del usuario en la consola y 
  un número entero (a parte) e imprima por pantalla en líneas distintas 
  el nombre del usuario tantas veces como el valor del número introducido.
"""

# nombre_rep = input('dame tu nombre: ')
# repeticiones= int(input('dame el numero: '))

# contador = 1
# while contador <= repeticiones:
#     print(nombre_rep)
#     contador += 1
  

"""
- Escribir un programa que pregunte el nombre completo del usuario en la consola 
  y después muestre por pantalla el nombre completo del usuario tres veces, 
  una con todas las letras minúsculas, otra con todas las letras mayúsculas 
  y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
  El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

# nombre_amod = input('escribe tu nombre completo: ')
# print(f'en Minusculas: {nombre_amod.lower()}')
# print(f'en Msyculas: {nombre_amod.upper()}')
# print(f'capitalizado: {nombre_amod.title()}')

"""
- Escribe un programa que le pida al usuario que escriba una frase 
  y le devuelva solamente las tres primeras letras “a” contenidas en la frase 
  pero en mayúsculas “A”.
"""

# letras_a = ''
# frase = input('escribe una frase: ')
# for letra_a in frase:
#     if letra_a.lower() == 'a':
#       letras_a += 'A'

# print(letras_a)

"""
- Escribe un programa que le asigne a una variable un poema o texto corto 
  con el espaciado adecuado y luego la imprima.
"""

# poema = '''
# Espero curarme de ti

#     Espero curarme de ti en unos días. Debo dejar de fumarte, de beberte, de pensarte. 
#     Es posible. Siguiendo las prescripciones de la moral en turno. 
#     Me receto tiempo, abstinencia, soledad.

#     ¿Te parece bien que te quiera nada más una semana? No es mucho, ni es poco, es bastante. 
#     En una semana se puede reunir todas las palabras de amor que se han pronunciado sobre la tierra y se les puede prender fuego. 
#     Te voy a calentar con esa hoguera del amor quemado. Y también el silencio. 
#     Porque las mejores palabras del amor están entre dos gentes que no se dicen nada.

#     Hay que quemar también ese otro lenguaje lateral y subversivo del que ama. 
#     (Tú sabes cómo te digo que te quiero cuando digo: «qué calor hace», «dame agua», «¿sabes manejar?», «se hizo de noche»... 
#     Entre las gentes, a un lado de tus gentes y las mías, te he dicho «ya es tarde», y tú sabías que decía «te quiero»).

#     Una semana más para reunir todo el amor del tiempo. Para dártelo. 
#     Para que hagas con él lo que quieras: guardarlo, acariciarlo, tirarlo a la basura. 
#     No sirve, es cierto. Sólo quiero una semana para entender las cosas. 
#     Porque esto es muy parecido a estar saliendo de un manicomio para entrar a un panteón.

# '''
# print(poema)

"""
- Usando slicing, escribe un programa que imprima una frase palabra por palabra. 
  Ejemplo:
        mifrase = "Esta es mi frase completa"
        print(f"{mifrase[0:4]}\n{mifrase[5:7]}...")
"""

# mifrase = 'yo solo se que no se nada'
# print(mifrase[0:2])
# print(mifrase[3:7])
# print(mifrase[8:10])
# print(mifrase[11:14])
# print(mifrase[15:17])
# print(mifrase[18:20])
# print(mifrase[21:25])

"""
- Sin revisar estos apuntes, define brevemente a modo de comentarios: 
  Qué es Fstring, los métodos len() y replace().
"""

# Fstring es una forma de concatenar cadenas de caracteres utilizando los corchetes para incluir 
# operaciones o variables de python.

# len() es un método que devuelve la longitud de una cadena de caracteres.

# replace() es un método que permite reemplazar una cadena de caracteres por otra cadena de caracteres.

