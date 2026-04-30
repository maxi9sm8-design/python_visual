# el if elif y else son estructuras de control de flujo
# que nos permiten tomar decisiones en nuestro código
# el if se ejecuta si la condición es verdadera
edad = 18
# el elif se ejecuta si la condición del if es falsa y la condición del elif es verdadera
edad = 16
input_edad = input("¿Cuántos años tienes? ")
input_edad = int(input_edad)
if input_edad >= 18:
    print("Eres mayor de edad")
elif input_edad >= 16:
    print("Eres un adolescente")
# el else se ejecuta si ninguna de las condiciones anteriores es verdadera
else:
    print("Eres un niño")
# también podemos usar el if elif else para comparar varias condiciones
color = "rojo"
input_color = input("¿Cuál es tu color favorito? el rojo o el verde? ")
if input_color == "rojo":
    print("El color es rojo")
elif input_color == "verde":
    print("El color es verde")
else:
    print("El color es otro")
    
