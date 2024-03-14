#podemps utilizar el comando break para terminar la ejecucion de un bucle si la condicion es verdadera

super = "Batman"

for letra in super:
    if letra == "m":
        
        break
    print(letra)

#podemos utilizar el comando continue para saltar la iteracion actual

cancion = "Bohemian Rhapsody"
for letra in cancion:
    if letra == "o":
        continue
    print(letra)
    