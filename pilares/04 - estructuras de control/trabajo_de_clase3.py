"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido.
"""
# edad = int(input("Ingrese su edad: "))
# for i in range(edad):
#     print(i+1)


"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 15 veces
"""

# palabra = input("Ingrese una palabra: ")
# for i in range(15):
#     print(palabra)
    
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""

# inpares = []
# numero = int(input("Ingrese un numero entero positivo: "))
# for i in range(1, numero+1):
#     if i % 2 != 0:
#         inpares.append(str(i))

# cadena = ",".join(inpares)
# print(cadena)

"""
Escribir un programa que pregunte al usuario una cantidad que desee invertir, 
el interés anual y el número de años, y muestre por pantalla 
el capital obtenido en la inversión cada año que dura la inversión.
"""

print('modelo de inversion')
cantidad_a_invertir = float(input('ingrese la inversion: '))
interes_anual = float(input('ingrese el interes anual: '))
anios_inversion = int(input('ingrese los años que mantendra su inversion: '))

for anio in range(1, anios_inversion+1):
    roi_anual = cantidad_a_invertir * interes_anual / 100
    capital_anual = roi_anual + cantidad_a_invertir
    print(f'año: {anio} --> retorno de inversion: {roi_anual} el capital total anual: {capital_anual}')
    cantidad_a_invertir = capital_anual
