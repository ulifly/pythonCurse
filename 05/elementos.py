simpsons = {
    'homer': 'papa',
    'marge': 'mama',
    'bart': 'hijo',
    'lisa': 'hija',
}
#obtenemos un valor pasando la llave

print(simpsons['homer'])

#podemos saber si una llave existe en el diccionario

print('maggie' in simpsons)
print('homer' in simpsons)

#podemos usar get si no estamos seguros si existe o no la llave esto para evitar error

valor = simpsons.get('maggie')
print(valor)

#tambien podemos especificar un valor por defecto en caso de que la llave no exista

valor = simpsons.get('maggie', 'no existe')
print(valor)

#podemos usar el metodo setdefault para añadir un elemento al diccionario si el elemento no existe
simpsons.setdefault('homer', 'hijo')
simpsons.setdefault('maggie', 'hija')
print(simpsons)

