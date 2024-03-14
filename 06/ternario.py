"""
en pyton tenemos algo similar a otros lenguajes de programacion como el 
operador ternario,
"""

calificacion = int(input("ingrese la calificacion: "))

if calificacion >= 7:
    color = "Verde"
else:
    color = "Rojo"    
print(color)
#aqui refactorizamos el codigo 

#ponemos el valor verdadero seguido de la condicion y el valor a asignar si la condicion es falsa
color = "Verde" if calificacion >= 7 else "Rojo"
print(color)
