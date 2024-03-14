"""
podemos evaluar multiples condiciones
lo que en otros lenguajes de programacion es elseif
en python usamos un metodo similar llamado elif

"""

calificacion = int(input("ingrese la calificacion: "))
if calificacion >= 90:
    print("Excelente")
elif calificacion == 80:
    print("Bien")
elif calificacion == 70:
    print("Regular")
elif calificacion == 60:
    print("Malo")
elif calificacion <= 50:
    print("Reprobado")

#podemps usar un metodo similar a switch en python es match
    
semaforo = "verde"

match semaforo:
    case "rojo":
        print("Detenido")
    case "amarillo":
        print("Precaucion")
    case "verde":
        print("Continuar")
    case _:
        print("Color no valido")
