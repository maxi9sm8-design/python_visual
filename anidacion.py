# la anidacion sirve para optimizar nuestro código y evitar repetir código innecesario
print("Anidacion con if elif else")
color = input("¿Cuál es tu color favorito? el rojo, el verde o el azul? ")
if color == "rojo":
    print("El color es rojo")
elif color == "verde":
    print("El color es verde")
elif color == "azul":
    print("El color es azul")
else:
    print("El color es otro")
    
print("la anidacion con if elif else nos permite comparar varias condiciones sin repetir código innecesario")
print("_________________________________________________________________________")

#anidacion con match case
color = input("¿Cuál es tu color favorito? el rojo, el verde o el azul? ")
match color:
    case "rojo":
        print("El color es rojo")
    case "verde":
        print("El color es verde")
    case "azul":
        print("El color es azul")
    case _:
        print("El color es otro")
        
print("la anidacion con match case nos permite comparar varias condiciones sin repetir código innecesario y de una forma más elegante y fácil de leer")
print("_________________________________________________________________________")

#anidacion con for
colores = ["rojo", "verde", "azul"]
for color in colores:
    print("El color es:", color)
    
print("la anidacion con for nos permite iterar sobre una lista sin repetir código innecesario")

print("_________________________________________________________________________")

#anidacion con while
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1
    
print("la anidacion con while nos permite repetir un bloque de código mientras una condición sea verdadera sin repetir código innecesario")

print("_________________________________________________________________________")

#todo esto lo podemos combinar para crear código más complejo y optimizado
color = input("¿Cuál es tu color favorito? el rojo, el verde o el azul? ")
contador = 0
while contador < 5:
    match color:
        case "rojo":
            print("El color es rojo")
        case "verde":
            print("El color es verde")
        case "azul":
            print("El color es azul")
        case _:
            print("El color es otro")
    contador += 1
    
print("la anidacion nos permite combinar varias estructuras de control de flujo para crear código más complejo y optimizado")
print("____________________________________________________________________________")

print("se puede anidar cualquier estructura, no hay límites para la anidación")