# el for sirve para repetir un bloque de código un número determinado de veces
for i in range(5):
    print("El número es:", i)

print("_________________________________________________________________________")

# también podemos usar el for para iterar sobre una lista
colores = ["rojo", "verde", "azul"]
for color in colores:
    print("El color es:", color)



print("_________________________________________________________________________")

# el for también puede tener un else que se ejecuta cuando el bucle termina
for i in range(5):
    print("El número es:", i)
else:
    print("El bucle ha terminado")
    
print("ocupamos el else para saber cuando el bucle ha terminado")

print("_________________________________________________________________________")

# el for también puede tener un break para salir del bucle
for i in range(5):
    print("El número es:", i)
    if i == 3:
        break
    
print("ocupamos break para salir del bucle cuando el número es 3")


print("_________________________________________________________________________")

# el for también puede tener un continue para saltar a la siguiente iteración

for i in range(5):
    if i == 3:
        continue
    print("El número es:", i)
    
print("ocupamos continue para saltar la iteración cuando el número es 3")

print("_________________________________________________________________________")

# el for también puede tener un pass para no hacer nada en una iteración

for i in range(5):
    if i == 3:
        pass
    print("El número es:", i)
    
print("ocupamos pass para no hacer nada en la iteración cuando el número es 3")


print("_________________________________________________________________________")
