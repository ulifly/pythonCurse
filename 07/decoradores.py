"""
en python un decorador se define como una funcion que toma como parametro otra funcion
y retorna una funcion con un comportamiento diferente 
Esta nueva función encapsula o envuelve la función original, 
permitiendo modificar su comportamiento. Para aplicar un decorador a una función, 
se utiliza la sintaxis @nombre_del_decorador justo encima de la definición de la función.
"""

def funcion_decorador(funcion_a_decorar):
    def funcion_interior():
        print("Este es el cuerpo de la funcion decorada")
        funcion_a_decorar()
    return funcion_interior



@funcion_decorador
def funcion_a_decorar():
    print("Esta es la funcion a decorar")

funcion_a_decorar()


"""
Tambien podemos decorar funciones que reciben parametros
"""

def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print("---> antes del llamado")

        operacion = funcion_b(*args, **kwargs)

        print("---> despues del llamado")

        return operacion

    return funcion_c


@funcion_a
def suma(num1 , num2):
    return (num1 + num2)

resultado = suma(10, 20)
print(resultado)
