# las tuplas en python son una estructura de datos
# que nos permite almacenar una colección de elementos
# las tuplas se definen con paréntesis ()
tupla = (1, 2, 3, 4, 5)
print("La tupla es:", tupla)
print("_________________________________________________________________________")
# las tuplas pueden contener cualquier tipo de dato
tupla2 = (1, "hola", 3.14, True)
print("La tupla 2 es:", tupla2)
print("diferentes tipos de datos")


print("_________________________________________________________________________")
# las tuplas son inmutables, no podemos modificar sus elementos
# tupla[0] = 10 # esto nos dará un error porque las tuplas
# son inmutables
print("inmutables")
print("_________________________________________________________________________")
# las tuplas también pueden contener otras tuplas
# lo que se conoce como tuplas anidadas
tupla3 = (1, 2, (3, 4), 5)
print("La tupla 3 es:", tupla3)
print("tuplas anidadas")


print("_________________________________________________________________________")
# las tuplas también pueden contener elementos repetidos
tupla4 = (1, 2, 2, 3, 4, 4, 5)
print("La tupla 4 es:", tupla4)

print("elementos repetidos")
print("_________________________________________________________________________")
# se puede acceder a los elementos de una tupla mediante su índice, que comienza en 0
print("El primer elemento de la tupla es:", tupla[0])
print("El segundo elemento de la tupla es:", tupla[1])
print("El tercer elemento de la tupla es:", tupla[2])
print("El cuarto elemento de la tupla es:", tupla[3])
print("El quinto elemento de la tupla es:", tupla[4])

print("acceder con el numero de tupla")
print("_________________________________________________________________________")
# también se ocupan seguidamente en for para iterar sobre los elementos de una tupla
colores = ("rojo", "verde", "azul")
for color in colores:
    print("El color es:", color)
    
print("for")
print("_________________________________________________________________________")
# o en while y for para crear código más complejo y optimizado
colores = ("rojo", "verde", "azul")
contador = 0
while contador < 5:
    for color in colores:
        print("El color es:", color)
    contador += 1
    
print("for y while combinados")
print("_________________________________________________________________________")