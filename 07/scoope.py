"""
el scoope se refiere al alcance que tienen las entidades
El ámbito determina desde qué bloques de código pueden ser accedidas y utilizadas estas entidades, 
como variables, métodos o funciones. Por otro lado, 
el contexto se refiere a la pertenencia de estas entidades a un objeto o estructura específica.

pero veamos un ejemplo para que quede mas claro
"""

personaje = "Homero Simpson"# esta variable esta en el scoope global puede ser accedida desde cualquier parte del codigo
print(personaje)
print(id(personaje))

def futurama():
    personaje = "Bender"# esta variable esta en el scoope local solo puede ser accedida desde la funcion futurama
    print(personaje)
    personaje2 = "Fry"# esta variable esta en el scoope local solo puede ser accedida desde la funcion futurama

futurama()

print(personaje)  #esta variable esta en el scoope global puede ser accedida desde cualquier parte del codigo
#print(personaje2) #solo puede ser accedida desde la funcion futurama asi que nos dara error
                  #como esta definida en el scoope local no puede ser accedida desde fuera de la funcion

def familiaSimpson():
    print(personaje)#como personaje esta definida como una variable global la toma esta funcion
familiaSimpson()

#tambien podemos indicar a python que queremos tomar una variable global en una funcion si queremos modificar dicha variable
#paandole la instruccion global antes de la declaracion de la variable

def losSimpsons():
    global personaje
    personaje = "Lisa Simpson"

losSimpsons()
print(personaje)
print(id(personaje))#podemos identificar con el id del onjeto que es la misma variable que declaramos al inicio