# el match case es una estructura de control de flujo
# que nos permite comparar un valor con varias opciones
# es similar al if elif else, pero más elegante y fácil de leer
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
        
# también podemos usar el match case para comparar varias condiciones
edad = int(input("¿Cuántos años tienes? "))
match edad:
    case edad if edad >= 18:
        print("Eres mayor de edad")
    case edad if edad >= 16:
        print("Eres un adolescente")
    case _:
        print("Eres un niño")
# el match case también puede usar patrones para comparar estructuras de datos
nombre1 = input("¿Cuál es tu nombre? ")
persona = {"nombre": nombre1, "edad": edad}
match persona:
    case {"nombre": nombre, "edad": edad} if edad >= 18:
        print(f"{nombre} es mayor de edad")
    case {"nombre": nombre, "edad": edad} if edad >= 16:
        print(f"{nombre} es un adolescente")
    case _:
        print("La persona es un niño")
        
#puedes ocupar if elif y else dentro de un case para comparar varias condiciones
match color:
    case "rojo":
        if edad >= 18:
            print("El color es rojo y eres mayor de edad")
        elif edad >= 16:
            print("El color es rojo y eres un adolescente")
        else:
            print("El color es rojo y eres un niño")
    case "verde":
        if edad >= 18:
            print("El color es verde y eres mayor de edad")
        elif edad >= 16:
            print("El color es verde y eres un adolescente")
        else:
            print("El color es verde y eres un niño")
    case "azul":
        if edad >= 18:
            print("El color es azul y eres mayor de edad")
        elif edad >= 16:
            print("El color es azul y eres un adolescente")
        else:
            print("El color es azul y eres un niño")