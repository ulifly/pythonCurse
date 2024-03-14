#en python podemos usar for para iterar en una lista, un string, una tupla o en un diccionario 

lista = [1,2,3,4,5]
for i in lista:
    print(i + 1)

alumnos = ["Juan", "Pedro", "Maria"]
for alumno in alumnos:
    print(f'el nombre del alumno es: {alumno}' )

nombre = 'ironman'
for letra in nombre:
    print(f'{letra}-')
