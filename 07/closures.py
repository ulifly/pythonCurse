"""
# repaso de scope

def funcion_principal():
    a = 'a'
    b = 'b'
    
    def funcion_anidada():
        c = 'c'

        print(a) #las variables pueden ser accedidas desde cualquier lugar dentro de la función anidada.
        print(c) #pero no desde fuera de la función anidada. esto es por que tiene un scope superior
        print(b)
    funcion_anidada()
    print(c)  #esto dará un error puesto que esta variable esta dentro de la función anidada y no en este scope

funcion_principal()
"""

#un closure es una funcion que puede generar de forma dinámica a otra funcion 
#y esta funcion puede acceder a las variables locales aun cuando la primera haya finalizado

def saludar(username):
    mensaje = f'Hola {username}' #esta es una variable local

    def mostrar_mensaje():
        print(mensaje) #esta es una variable local y puede acceder a la variable local de la funcion principal

    return mostrar_mensaje

username = 'Ulifly'
respuesta = saludar(username)

respuesta()  
username = 'otro usuario (esto nunca se va a mostrar)'

respuesta()

"""
Un closure se refiere a una función anónima que puede acceder a variables fuera de su ámbito de definición. 
En otras palabras, permite encapsular datos y lógica en un bloque independiente y reutilizable. 
Los closures son útiles para crear funciones más dinámicas y adaptables a diferentes contextos.

un closure se crea cuando una función interna accede a variables locales de una función externa. 
Esto permite que la función interna conserve acceso a esas variables incluso después de que la función externa haya finalizado su ejecución.
"""