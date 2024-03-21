#en python podemos escribir funciones definiendolas con la palabra reservada def

def suma():
    num1=int(input("ingrese un numero: "))
    num2=int(input("ingrese otro numero: "))
    print("la suma es: ", num1+num2)

suma()

"""
las funciones son un conjunto de instrucciones que realizan una tarea especifica.
son utiles para no repetir codigo.
podemos llamar a una funcion desde otra funcion.
podemos pasar parametros a una funcion como en el sig ejemplo.
"""
def suma(num1, num2):#parametros
    print("la suma es: ", num1+num2)

suma(2,3)#argumentos


#podemos retornar valores de una funcion.

def resta(num1, num2):
    return num1-num2

resultado=resta(5, 2)
print(resultado)

#las funciones pueden retornar mas de un valor y los retornan en forma de tupla.
def operaciones(num1, num2):
    return num1*num2, num1/num2 #separamos los valores a retornar con coma

resultado = operaciones(5, 2)

print(resultado)#el resultado es una tupla

#como cualquier tupa podemos desempaquetarla
a, b = operaciones(5, 2)
print(a)
print(b)




