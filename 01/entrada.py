#en python podemos recibir datos con la funcion input
input ("Ingrese su nombre: ")

#podemos guardar el valor ingresado en una variable para usarlo
nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

#podemos recibir datos numericos pero la funcion input devuelve un string

edad = input("Ingrese su edad: ")
print(edad + " años")
print(type(edad))

#podemos convertir el string a int con la funcion int

edad = int(edad)
print(edad)
print(type(edad))

#podemos recibir datos directamente con decimales o enteros anteponindo la funcion para convertir el tipo de dato

precio = float(input("Ingrese el precio: "))
print(precio)
print(type(precio))

#podemos comparar los datos recibidos para dar datos booleanos 
vivo = input("Está vivo? s/n ") == 's'
print(vivo)
print(type(vivo))