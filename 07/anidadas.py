"""
podemos anidar funciones dentro de funciones
"""

def operacion_bancaria(cantidad, balance, tipo='deposito'): #aqui ponemo por default el tipo deposito

    def deposito(cantidad, balance):
        return(cantidad + balance)
    

    def retiro(cantidad, balance):
        if cantidad > balance:
            return("No hay saldo suficiente")           
        else: 
            return(balance - cantidad)

    if tipo == "deposito":
        return deposito(cantidad, balance)
    elif tipo == "retiro":
        return retiro(cantidad, balance)

resultado = operacion_bancaria(400, 1000, "retiro") #si pasamos el tipo retiro se ejecuta dicha funcion
print(resultado)
