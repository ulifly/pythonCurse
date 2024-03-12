#podemos generar cadenas con otras cadenas a esto se le llama concatenar

cadena = "Hola"
cadena2 = "Mundo"
cadena = "bonjour"
helloWorld = (cadena + ' ' + cadena2)
print(helloWorld)

#podemos concatenar con el operador %s pasandole el argumento
cadena2 = "zoquetes"
saludo = "%s %s %s"  %(cadena, "pedazo de",  cadena2)
print(saludo)

#podemos utilizar placeholders seguido del metodo format como en el sig ejemplo

nombre = 'Ulises'
apellido = 'Desentis'

nombreCompleto = 'Sr. {} {} '.format(nombre, apellido)

print(nombreCompleto)

#tambien podemos nombrar los placeholders y enviarles parametros como en el sig ejemplo

computadora = 'MacBook con {periferico1} y {periferico2}'.format(
    periferico1 = 'raton', 
    periferico2 = 'monitor') 

print(computadora)

#podemos interpolar strings con fstrings utilizando la letra f como en el sig ejemplo

nombreCompleto2 = f'Sr. {nombre} {apellido} {5>3}'

print(nombreCompleto2)
