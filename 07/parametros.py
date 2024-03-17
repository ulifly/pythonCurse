#podemos pasar un parametro por defaullt
def area_circulo(radio, pi=3.14):
    return pi * radio ** 2

print(area_circulo(5)) #aqui solo pasamos un parametro por que pi lo definimos por default

#sin embargo si pasamos un paramatre se toma en que pasamos y no el por defecto

print(area_circulo(5, 3.141592)) #aqui pasamos el valor de pi y el valor del radio


#si pasamos un parametro por default debe ir al final.
#sin embargo podemos pasar parametros con el mismo nombre y no tener problemas. con la posicion

print(area_circulo(pi=3.141592, radio=8)) 
