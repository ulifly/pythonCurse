"""
Utilizando la condicional if else escribe un programa que imprima en pantalla 
si un número dado por el usuario es par o impar.
"""

# numero = int(input("Ingrese un numero: "))
# if numero % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")


"""
Utilizando la condicional if else escribe un programa que pida un número al usuario, 
si éste es mayor que cinco, lo decremente en una unidad e imprima el resultado, 
y si es menor o igual no haga nada más que mostrarlo. 
"""

# numero2 = int(input("Ingrese un numero: "))
# if numero2 > 5:
#     numero2 -= 1
#     print(numero2)
# else:
#     print(numero2)

"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""

# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Es mayor de edad")
# else:
#     print("Es menor de edad")

"""
Escribir un programa que almacene la cadena de caracteres `contraseña`en una variable, 
luego pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada en la variable, 
el usuario puede escribir la palabra `contraseña` en mayúsculas o minúsculas 
y el programa lo aceptará como válido.
"""

# password = 'contraseña123'
# datain = input("Ingrese su contraseña: ")
# if datain == password:
#     print("Contraseña correcta")
# else:
#     print("Contraseña incorrecta")

"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""

# dividendo = int(input("Ingrese el dividendo: "))
# divisor = int(input("Ingrese el divisor: "))
# if divisor == 0:
#     print("Error el divisor no puede ser igual a 0")
# else:
#     resultado = dividendo / divisor
#     print(resultado)

"""
Para declarar impuestos se debe ser mayor de 16 años y tener unos ingresos iguales o superiores 
a 25 mil pesos mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales, 
y muestre por pantalla si el usuario tiene que declarar o no.
"""

# print('evaluacion para declarar impuestos')
# edad = int(input('Ingrese su edad: '))
# ingresos = int(input('Ingrese sus ingresos mensuales: '))
# if edad >= 16 and ingresos >= 25000:
#     print('deacuerdo a sus datos debe declarar impuestos')
# else:
#     print('deacuerdo a sus datos esta exento de declarar impuestos')

"""
Escribe un programa que pregunte al usuario un día de la semana e imprima por pantalla 
- “Buen inicio de semana” cuando el usuario ingrese lunes
- “Dos es mejor que uno” cuando el usuario ingrese martes
- “Ya es mitad de semana, ¡ánimo!” cuando el usuario ingrese miércoles
- “Un día más…” cuando el usuario ingrese jueves
- “Por fin, ¡A descansar!” cuando el usuario ingrese viernes
- “¿Qué haces aquí?” cuando el usuario ingrese algún día del fin de semana
"""

# dia_semana = input('Ingrese un dia de la semana: ')
# dia_semana = dia_semana.lower()
# match dia_semana:
#     case 'lunes':
#         print('Buen inicio de semana')
#     case 'martes':
#         print('Dos es mejor que uno')
#     case 'miercoles':
#         print('Ya es mitad de semana, ¡ánimo!')
#     case 'jueves':
#         print('Un día más...')
#     case 'viernes':
#         print('Por fin, ¡A descansar!')
#     case _:
#         print('¿Qué haces aquí?')
