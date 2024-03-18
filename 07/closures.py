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