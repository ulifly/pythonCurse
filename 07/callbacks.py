"""
los callbacks son funciones utilizadas como argumentos para otras funciones
"""

promedio = lambda *args: sum(args)/len(args)
aprobatorio = lambda promedio: promedio >= 7

def notas(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args) #aqui recojemos la funcion promedio y le pasamos los argumentos
                                    #y se asina a la variable promedio
    
    if func_aprobatorio(promedio): #aqui recojemos la funcion aprobatorio y le pasamos el promedio
        print(f'Estas aprobado con promedio de {promedio}')
    else:
        print(f'Estas reprobado {promedio}')

print(notas(promedio, aprobatorio, 7, 5, 6, 8, 8))

"""
como podemos ver los callbacks son funciones que se pasan como argumentos a otras funciones
y son muy utiles sobre todo para programacion funcinal ya que nos ayudan a reutilizar codigo
y modulizarlo
"""