# los diccionarios en python son una estructura de datos
# que nos permite almacenar una colección de elementos
# los diccionarios se definen con llaves {}
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("El diccionario es:", diccionario)

print("_________________________________________________________________________")
# los diccionarios pueden contener cualquier tipo de dato
diccionario2 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid", "hobbies": ["futbol", "musica"], "activo": True}
print("El diccionario 2 es:", diccionario2)

print("diferentes tipos de datos")
print("_________________________________________________________________________")
# los diccionarios son mutables, es decir, podemos modificar sus elementos
diccionario["nombre"] = "Pedro"
print("El diccionario modificado es:", diccionario)
print("mutables")

print("_________________________________________________________________________")

# se puede acceder a los elementos de un diccionario mediante su clave
print("El nombre es:", diccionario["nombre"])
print("La edad es:", diccionario["edad"])
print("La ciudad es:", diccionario["ciudad"])
print("acceder con la clave")

print("_________________________________________________________________________")

# también se ocupan seguidamente en for para iterar sobre los elementos de un diccionario

for clave in diccionario:
    print("La clave es:", clave, "y el valor es:", diccionario[clave])
    
print("for")

print("_________________________________________________________________________")

# o en while y for para crear código más complejo y optimizado

contador = 0
while contador < 5:
    for clave in diccionario:
        print("La clave es:", clave, "y el valor es:", diccionario[clave])
    contador += 1
    
print("for y while combinados")

print("_________________________________________________________________________")

# se pueden agregar, editar y eliminar elementos de un diccionario

diccionario["pais"] = "España" # agregar un elemento
print("El diccionario con el nuevo elemento es:", diccionario)

diccionario["edad"] = 35 # editar un elemento
print("El diccionario con el elemento editado es:", diccionario)

del diccionario["ciudad"] # eliminar un elemento
print("El diccionario con el elemento eliminado es:", diccionario)
print("agregar, editar y eliminar elementos")