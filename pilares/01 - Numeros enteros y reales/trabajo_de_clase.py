### Trabajo de clase:
"""
- Escribe un comando que muestre en pantalla el resultado de la suma de cuatro variables de valor entero. <----

- Escribe el comando que devuelva el tipo de valor de cada una de esas variables.<----

- Asigna el resultado de la suma de variables a otra variable y convierte su valor de `int` a `float.` <---
  Imprime el tipo de valor final de la variable.

- Escribe un comando que asigne la conversión de un dato tipo `float` a una variable y después muestre <---
  el valor de la variable en pantalla.

- Escribe un comando de una sola línea donde se muestre en pantalla la conversión de un dato `int`a `float`. <---
"""
num1 = 1
num2 = 2
num3 = 3
num4 = 4

print(num1 + num2 + num3 + num4)
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

suma = num1 + num2 + num3 + num4
suma_float = float(suma)
print(suma_float)
print(type(suma_float))
print(float(num1))