### Trabajo de clase:
"""
- Multiplica 10 por 5, súmalo a 16 entre 80 e imprime el resultado.
"""
#print ((10 * 5) + (16 / 80))

"""
- Pide al usuario que ingrese dos números enteros. 
  Calcula el módulo de la división del primer número entre el segundo y 
  muestra el resultado en pantalla.
"""

#num1 = int(input('ingtresa el primer numero '))
#num2 = int(input('ingresa el segundo numero '))

#print(f' el modulo de {num1} entre {num2} es {num1%num2}')

"""
- Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
  (es suficiente con mostrar `True` o `False`):
    - Si los dos números son iguales
    - Si los dos números son diferentes
    - Si el primero es mayor que el segundo
    - Si el segundo es mayor o igual que el primero
"""
# print('comparacion de numeros')
# comparar1 = int(input('ingrese el primer numero a comparar '))
# comparar2 = int(input('ingrese el segundo numero a comparar '))
# iguales = comparar1 == comparar2
# diferentes = comparar1 != comparar2
# mayorque = comparar1 > comparar2
# segmayorigual = comparar2 >= comparar1

# print(f'los numeros son iguales? {iguales}')
# print(f'los numeros son diferentes {diferentes}')
# print(f'el primer numero es mayor que el segundo {mayorque}')
# print(f'el seguno numero es mayor o igual que el primero {segmayorigual}')



"""
- Dados tres números de tipo `float` ingresados por el usuario, 
  muestra en pantalla la multiplicación, la suma y la resta de los tres, 
  y por último la división de dos de ellos.
"""
# print('operaciones con numeros')

# operacion_num1 = float(input('ingrese el umero 1 de 3: '))
# operacion_num2 = float(input('ingrese el umero 2 de 3: '))
# operacion_num3 = float(input('ingrese el umero 3 de 3: '))

# operacion_multiplicacion = operacion_num1 * operacion_num2 * operacion_num3
# operacion_suma = operacion_num1 + operacion_num2 + operacion_num3
# operacion_resta = operacion_num1 - operacion_num2 - operacion_num3
# operacion_division = operacion_num1 / operacion_num2

# print(f'la suma de los 3 numeros es: {operacion_suma}')
# print(f'la resta de los 3 numeros es: {operacion_resta}')
# print(f'la multiplicacion de los 3 numeros es: {operacion_multiplicacion}')
# print(f'la division del primer numeros entre el segundo es: {operacion_division}')

""""
- Realiza un programa que lea el valor de un lado de un cuadrado, que calcule su área, 
  su perímetro y los imprima en pantalla.
"""

# print('perimetro y arera de un cuadraro')
# lado = float(input('ingrese la longitud del lado del cuadrado: '))
# print(f'el perimetro del cuadrado es: {lado * 4}')
# print(f'el area del cuadraro es: {lado*lado}')

"""
- Pide al usuario ingresar el radio de un círculo (valor flotante). 
  Calcula el área del círculo utilizando la fórmula: `a = pi * radio^2.` 
  Utiliza el valor aproximado de pi como 3.14159. Muestra el resultado en pantalla.
"""

# print ('Area de un circulo')
# radio = float(input('ingrese el radio del circulo: '))
# print(f'el area  del circulo es: {3.14159 * radio**2}')

"""
- Escribe un programa que le pregunte el año de nacimiento al usuario y le devuelva su edad en años, 
  el valor de su edad debe imprimirse como `int`.
"""

# print('calculndo edad')
# fecha_nacimiento = int(input('ingrese su fecha de nacimiento: '))
# print(f'tu edad debe ser {2024 - fecha_nacimiento}')

"""
- Pide al usuario que ingrese el precio original de un producto (valor real) 
  y el porcentaje de descuento a aplicar (valor entero).
  Calcula el precio final después del descuento utilizando operaciones aritméticas 
  y muestra el resultado en pantalla.
"""

# print('descuentos')
# precio = float(input('ingrese el precio del articulo: '))
# a_descuento = int(input('ingrese el porcentaje de descuento: '))
# descuento = precio * a_descuento / 100
# print(f'El precio con descuento es: {precio - descuento}')

"""
- Solicita al usuario que ingrese una longitud en metros (valor real). 
  Convierte la longitud a centímetros utilizando una operación matemática simple y 
  muestra el resultado en pantalla.
"""

# print('metros a centimetros')
# longitud = float(input('ingrese la longitud en metros: '))
# print(f'La longitud en centimetros es {longitud * 100}') 

"""
- Pide al usuario que ingrese un número entero de dos dígitos. 
  Calcula la suma de los dos dígitos utilizando operaciones aritméticas básicas 
  y muestra el resultado en pantalla.
"""

# print('suma digitos')
# dos_digitos = input('ingrese un numero entero de dos digitos: ')
# digito1 = int(dos_digitos[0])
# digito2 = int(dos_digitos[1])
# print(f'la suma del primer digito {digito1} + {digito2} el segundo digito es: {digito2 + digito1} ')

"""
- Pide al usuario que ingrese dos números, sin usar estructuras de control, 
  determina si la división es exacta y muestra por pantalla 
  `“La división es exacta: True/False”` dependiendo el caso.
"""

# print ('confirmar si la division es exacta')
# num_a_dividir = float(input('ingrese el numero a dividir: '))
# num_divisor = float(input('ingrese entre que numero se va a dividir: '))
# comprobacion = num_a_dividir%num_divisor == 0
# print(comprobacion)
