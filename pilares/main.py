animal = "Leon" #Variable global

def imprimir_animal():
		animal = "Ballena" #Variable local
		print(animal)

imprimir_animal() #Aqui el resultado sera Ballena

print(animal)#Aquí sera Leon

#--------------------------------------
def imprimir_animal():
		global animal
		animal = "Ballena"
		
imprimir_animal()
print(animal)

resultado = 5 * 4 
