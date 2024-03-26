"""
un generador es una funcion que crea objetos iterables
la siguiente es una simple funcio que imprime los numeros pares del 0 al 100
la utilizaremos de ejemplo:

def pares():
    for numero in range(0, 101, 2):
        print(numero)

pares()

"""
#ahora vamos a crear un generador de numeros pares

def pares():
    for numero in range(0, 101, 2):
        yield numero #yield es una palabra reservada que nos permite generar un generador 
                     #pues adiferencia de return no detiene la ejecucion

# for numero_par in pares():        omitimos esto para el sig ejemplo
#     print(numero_par)
        
"""
la utilidad de los generadores es que no necesitamos crear una lista para poder recorrerla
asi ahorramos espacio en memoria y se llama el iterable bajo demanda
"""

generador = pares()
print(next(generador)) #con la funcion next podemos recorrer el generador dato por dato
print(next(generador)) #en vez de obtener todos los datos de golpe
print(next(generador))
