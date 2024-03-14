
"""
Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. 
Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. 
Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios. <<<<---

Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, 
usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones 
sobre los valores que se pueden ingresar.

Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres 
y un longitud máxima de 50.
Así mismo el número de teléfono será a 10 dígitos.
Si por alguna razón el usuario ingresa mal alguno de estos datos, 
el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.
"""
print('Reto python dia 2')

no_usuarios_registro = int(input('cuantos usuarios deseas registrar? '))
while no_usuarios_registro > 0:

    nombre = input('ingresa tu nombre(s): ')

    while len(nombre) < 5 or len(nombre) > 50:
        print('nombre invalido, debe contener al menos 5 carateres y no exeder de 50')
        nombre = input('ingresa tu nombre(s):')
    else:
        apellidos = input('ingresa tus apellidos: ')
        while len(apellidos) < 5 or len(apellidos) > 50:
            print('apellidos invalido, debe contener al menos 5 carateres y no exeder de 50')
            apellidos = input('ingresa tus apellidos: ')
        else:
            telefono = input('Ingresa el numero telefonico: ')
            while len(telefono) != 10:
                print('telefono invalido, debe contener 10 digitos')
                telefono = input('Ingresa el numero telefonico: ')
            else:
                email = input('ingresa el correo electronico: ')
                while len(email) < 5 or len(email) > 50:
                    print('email invalido, debe contener mas e 5 caracteres y menos de 50')            
                else:
                    message = f'Hola {nombre} {apellidos}, en breve recibirás un correo a {email}.'
                    print(message)
                    no_usuarios_registro -= 1
else:
    print('registro exitoso')



# nombre =    input('ingresa tu nombre(s):')
# apellidos = input('ingresa tus apellidos:')
# telefono =  input('ingresa tu numero de telefono:')
# email =     input('ingresa tu email:')

# #print('Hola' + ' ' +nombre + ' ' + apellidos + ', en breve recibirás un correo a ' + email + '.')
# message = f'Hola {nombre} {apellidos}, en breve recibirás un correo a {email}.'
# print(message)