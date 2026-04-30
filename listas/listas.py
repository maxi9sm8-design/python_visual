#las listas en python son una estructura de datos que nos permite almacenar una colección de elementos
#las listas se definen con corchetes []
lista = [1, 2, 3, 4, 5]
print("La lista es:", lista)


print("_________________________________________________________________________")
#las listas pueden contener cualquier tipo de dato
lista2 = [1, "hola", 3.14, True]
print("La lista 2 es:", lista2)


print("diferentes tipos de datos")
print("_________________________________________________________________________")
#las listas son mutables, es decir, podemos modificar sus elementos
lista[0] = 10
print("La lista modificada es:", lista)

print("mutables")
print("_________________________________________________________________________")
#las listas también pueden contener otras listas, lo que se conoce como listas anidadas
lista3 = [1, 2, [3, 4], 5]
print("La lista 3 es:", lista3)


print("listas anidadas")
print("_________________________________________________________________________")
#las listas también pueden contener elementos repetidos 
lista4 = [1, 2, 2, 3, 4, 4, 5]
print("La lista 4 es:", lista4)


print("elementos repetidos")
print("_________________________________________________________________________")

 #se puede acceder a los elementos de una lista mediante su índice, que comienza en 0
print("El primer elemento de la lista es:", lista[0])
print("El segundo elemento de la lista es:", lista[1])
print("El tercer elemento de la lista es:", lista[2])
print("El cuarto elemento de la lista es:", lista[3])
print("El quinto elemento de la lista es:", lista[4])

print("acceder con el numero de lista")
print("_________________________________________________________________________")
#también se ocupan seguidamente en for para iterar sobre los elementos de una lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print("El color es:", color)

print("for")
print("_________________________________________________________________________")
# o en los 2 para crear código más complejo y optimizado
colores = ["rojo", "verde", "azul"]
contador = 0
while contador < 5:
    for color in colores:
        print("El color es:", color)
    contador += 1
    
print("for y while combinados")