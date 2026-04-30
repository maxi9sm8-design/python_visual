# input sirve para preguntarle algo al usuario y guardar su respuesta en una variable

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
# el input siempre devuelve una cadena de texto
# por lo que si queremos usar la edad como un número, debemos convertirla

edad = int(edad)
# ahora podemos usar la edad como un número

print("Hola", nombre, "tienes", edad, "años")
# también podemos hacer operaciones con la edad

edad_futura = edad + 5
print("En 5 años tendrás", edad_futura, "años")
# podemos usar el input para pedir cualquier tipo de información

color_favorito = input("¿Cuál es tu color favorito? ")
print("Tu color favorito es", color_favorito)
# también podemos usar el input para pedir información más compleja

direccion = input("¿Cuál es tu dirección? ")
print("Tu dirección es", direccion)
# el input también puede tener un mensaje personalizado

mensaje = input("Escribe un mensaje para ti mismo: ")
print("Tu mensaje es:", mensaje)