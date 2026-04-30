# el while sirve para repetir un bloque de código
# mientras una condición sea verdaderas
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1
    
    
    
print("_________________________________________________________________________")    
# también podemos usar el while para pedir información al usuario
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe algo (o salir para terminar): ")
    print("Tu respuesta fue:", respuesta)
# el while también puede tener un else que se ejecuta cuando la condición es falsa



print("________________________________________________________________________")  
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1
else:
    print("El contador ha llegado a 5")

print("ocupamos el else para saber cuando el contador ha llegado a 5")
# el while también puede tener un break para salir del bucle



print("_________________________________________________________________________")  
contador = 0
while True:
    print("El contador es:", contador)
    contador += 1
    if contador >= 5:
        break

print("ocupamos break para salir del bucle cuando el contador llega a 5")



print("_________________________________________________________________________")  
# el while también puede tener un continue para saltar a la siguiente iteración
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print("El contador es:", contador)

print("ocupamos continue para saltar la iteración cuando el contador es 3")



print("_________________________________________________________________________")  

# el while también puede tener un pass para no hacer nada en una iteración
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        pass
    print("El contador es:", contador)

print("ocupamos pass para no hacer nada en la iteración cuando el contador es 3")
print("_________________________________________________________________________")  
