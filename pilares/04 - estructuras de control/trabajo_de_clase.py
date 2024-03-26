"""
Realizar un programa que solicite un número al usuario y determine si es par o impar 
utilizando la estructura if. Si el número es par, el programa debe mostrar el mensaje "El número es par"; 
si es impar, debe mostrar el mensaje "El número es impar".
"""

# numero = int(input("Ingrese un número: "))
# if numero % 2 == 0:
#     print("El número es par")
# else:
#     print("El número es impar")

"""
Realizar un programa que solicite dos números al usuario y determine cuál es el mayor utilizando la estructura 
if-else. Si los números son iguales, el programa debe mostrar el mensaje "Los números son iguales".
"""

# numero1 = int(input("Ingrese un número: "))
# numero2 = int(input("Ingrese otro número: "))

# if numero1 > numero2:
#     print("El primer número es mayor")
# elif numero1 == numero2:
#     print("Los números son iguales")
# else:
#     print("El segundo número es mayor")

"""
Realizar un programa que solicite una letra al usuario y determine si es una vocal o una consonante 
utilizando la estructura if-else. Si la letra es una vocal, el programa debe mostrar el mensaje "La letra es una vocal"; 
si es una consonante, debe mostrar el mensaje "La letra es una consonante".
"""

# letra = input("Ingrese una letra: ")
# if letra.lower() in "aeiou":
#     print("La letra es una vocal")
# else:
#     print("La letra es una consonante")

"""
Realizar un programa que solicite al usuario un número del 1 al 7 
y muestre el día de la semana correspondiente utilizando la estructura if-else. 
Por ejemplo, si el usuario ingresa el número 1, el programa debe mostrar el mensaje "Lunes".
"""

# dia_de_la_semana = int(input('ingrese un numero entre el 1 y el 7: '))
# if dia_de_la_semana == 1:
#     print('el numero corresponde al dia lunes')
# elif dia_de_la_semana == 2:
#     print('el numero corresponde al dia martes')
# elif dia_de_la_semana == 3:
#     print('el numero corresponde al dia miercoles')
# elif dia_de_la_semana == 4:
#     print('el numero corresponde al dia jueves')
# elif dia_de_la_semana == 5:
#     print('el numero corresponde al dia viernes')
# elif dia_de_la_semana == 6:
#     print('el numero corresponde al dia sabado')
# elif dia_de_la_semana == 7:
#     print('el numero corresponde al dia domingo')
# else:
#     print('el numero ingresado no corresponde a ningun dia de la semana')


"""
Escribe un programa que pida al usuario un número y le muestre si es positivo, negativo o cero.
"""

# numero = int(input("Ingrese un número: "))

# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# elif numero == 0:
#     print("El número es cero")

"""
Realizar un programa que solicite un número al usuario y calcule su factorial 
utilizando un ciclo for. El programa debe mostrar el resultado del cálculo.
"""

print('calculo de factorial')
numero = int(input('ingrese un numero: '))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i
    print(f'el factorial de {numero} es {factorial}')
