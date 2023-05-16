# DesafioEntregable3-Aignasse Naomi
intentos = 8

import random

azar = random.randint(1, 100)

nombre = input("Ingrese su nombre")

print(nombre, "debes adivinar un numero entero entre el 1 y el 100, tienes 8 intentos")

for i in range(8):
    numero = input("Ingrese el número que cree que es")
    x = numero.isdigit()
    if x == True:
        if numero == azar:
            print("Felicidades, adivinaste el numero")
        elif numero != azar:
            intentos = intentos - 1
            print("No adivinaste el numero")

    elif x == False:
        intentos = intentos - 1
        print("No ingresaste un numero entero")

    if intentos > 0:
        print("No adivinaste, te quedan", intentos, "intentos")
    elif intentos == 0:
        print("Lo siento ya no le quedan intentos, el numero a adivinar era", azar)
