"""
# repaso de scoope

def funcion_principal():
    a = 'a'
    b = 'b'
    
    def funcion_anidada():
        c = 'c'

        print(a) #las variables pueden ser accedidas desde cualquier lugar dentro de la funcion anidada.
        print(c) #pero no desde fuera de la funcion anidada. esto es por que tiene un scoope superior
        print(b)
    funcion_anidada()
    print(c)  #esto dara un error puesto que esta variable esta dentro de la funcion anidada y no en este scoope

funcion_principal()
"""

#un closure es una funcion que puede generar de forma dinamica a otra funcion 
#y esta funcion puede acceder a las variables locales aun cuando la pirmera haya finalizado

def saludar(username):
    mensaje = f'Hola {username}' #esta es una variable local

    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje

username = 'Ulifly'
respuesta = saludar(username)

respuesta()