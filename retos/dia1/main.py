
"""
Para este primer reto de la semana, tu objetivo será poder crear un programa en 
Python el cual permita registrar a un usuario en el sistema.
Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

    Nombre(s)
    Apellidos
    Número de teléfono
    Correo electrónico.

Una vez el usuario haya ingresado todos los datos vía teclado, 
el programa le dará la bienvenida al usuario con el siguiente mensaje:

Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico.
"""

print('Reto python dia 1')
nombre =    input('ingresa tu nombre(s):')
apellidos = input('ingresa tus apellidos:')
telefono =  input('ingresa tu numero de telefono:')
email =     input('ingresa tu email:')

#print('Hola' + ' ' +nombre + ' ' + apellidos + ', en breve recibirás un correo a ' + email + '.')
message = f'Hola {nombre} {apellidos}, en breve recibirás un correo a {email}.'
print(message)
