#EJERCICIO 1

encriptado=""
alfabeto="abcdefghijklmnopqrstuvwxyz"


cantidad=int(input("Ingrese la cantidad de lugares a correr: "))

for i in range(1, 6):
    mensaje = input(f"Ingrese el mensaje a encriptar: ")
    encriptado = ""
    for letra in mensaje:
        if letra in alfabeto:
            pos=alfabeto.index(letra.lower())
            nueva_pos=(pos+cantidad)%len(alfabeto)
            nueva_letra=alfabeto[nueva_pos]
            encriptado=encriptado+nueva_letra
            if letra.isupper():
                nueva_letra=nueva_letra.upper()
                encriptado=encriptado+nueva_letra
        else:
            encriptado=encriptado+letra
        
    print(f"Mensaje {i}: {encriptado}")

#EJERCICIO 2

import random

final=""
resultado=True

opciones=["piedra","papel","tijeras"]

while resultado:
    opcion=input("Elija una opción: ").lower()
    if opcion in opciones:
        print("Eleccion usuario: ",opcion)
        resultado=False
    else:
        print("Opción inexistente.")

opcion_pc=random.choice(opciones)
print("Eleccion de la pc: ",opcion_pc)

if opcion=="piedra" and opcion_pc=="piedra":
    final="Empate."
elif opcion=="piedra" and opcion_pc=="tijeras":
    final="Usuario es el ganador."
elif opcion=="piedra" and opcion_pc=="papel":
    final="Pc es la ganadora."
elif opcion=="papel" and opcion_pc=="piedra":
    final="Usuario es el ganador."
elif opcion=="papel" and opcion_pc=="tijeras":
    final="Pc es la ganadora."
elif opcion=="papel" and opcion_pc=="papel":
    final="Empate."
elif opcion=="tijeras" and opcion_pc=="piedra":
    final="Pc es la ganadora."
elif opcion=="tijeras" and opcion_pc=="papel":
    final="Usuario es el ganador."
elif opcion=="tijeras" and opcion_pc=="tijeras":
    final="Empate."
    
print(final)