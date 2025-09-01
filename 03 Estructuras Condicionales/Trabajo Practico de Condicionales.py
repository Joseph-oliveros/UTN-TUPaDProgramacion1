#EJERCICIO 1

edad=0
edad=int(input("Ingrese su edad: "))

if edad>=18:
    print("Es mayor de edad.")
else:
    pass

#EJERCICIO 2

nota=0
nota=int(input("Ingrese su nota: "))

if nota>=6:
    print ("Aprobado.")
else:
    print("Desaprobado.")

#EJERCICIO 3

num=0
num=int(input("Ingrese un número par: "))

if num%2==0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#EJERCICIO 4

edad=0
categoria=""
edad=int(input("Ingrese su edad: "))

if edad<12:
    categoria="Niño/a."
elif edad<18:
    categoria="Adolescente."
elif edad<30:
    categoria="Adulto/a joven."
else:
    categoria="Adulto/a."

print(f"Usted pertenece a la categoria: {categoria}")

#EJERCICIO 5

clave=""
clave=input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(clave)<8 or len(clave)>14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
else:
    print("Ha ingresado una contraseña correcta")

#EJERCICIO 6

from statistics import mode,median,mean
import random

# mean= promedio (media)
# median= valor central de los datos
# mode= valor que mas veces aparece

sesgo=""
numeros_aleatorios=[random.randint(1,100)for i in range(50)]

print(f"Lista de números: {numeros_aleatorios}")

moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

print(f"La moda es: {moda}")
print(f"La mediana es: {mediana}")
print(f"La media es: {media}")

if media>mediana and mediana>moda:
    sesgo="Sesgo positivo."
elif media<mediana and mediana<moda:
    sesgo="Sesgo negativo."
elif media==mediana and mediana==moda:
    sesgo="Sin sesgo."
else:
    sesgo="No se puede determinar el sesgo."

print(sesgo)
    
#EJERCICIO 7

frase=""
vocales=""
vocal_final=""

frase=input("Ingrese una frase o palabra: ")
frase_minus=frase.lower()
vocales="aeiou"

if frase_minus[-1] in vocales:
    vocal_final=(f"{frase}!")
else:
    vocal_final=(frase)

print(vocal_final)
    
#EJERCICIO 8

nombre=""
numero=0

nombre=input("Ingrese su nombre: ")

print("(1) Si quiere su nombre en mayusculas")
print("(2) Si quiere su nombre en minusculas")
print("(3) Si quiere su nombre con la primera letra mayuscula")

numero=int(input("Ingrese la opcion deseada: "))

if numero==1:
    print(nombre.upper())
elif numero==2:
    print(nombre.lower())
elif numero==3:
    print(nombre.title())
else:
    print("OPCIÓN INCORRECTA")

#EJERCICIO 9

magnitud=0
categoria=""

magnitud=float(input("Ingrese la magnitud del terremoto: "))

if magnitud<3:
    categoria="\"Muy leve\" (imperceptible)."
elif magnitud>=3 and magnitud<4:
    categoria="\"Leve\" (ligeramente perceptible)."
elif magnitud>=4 and magnitud<5:
    categoria="\"Moderado\" (sentido por personas, pero generalmente no causa daños)."
elif magnitud>=5 and magnitud<6:
    categoria="\"Fuerte\" (puede causar daño en estructuras débiles)."
elif magnitud>=6 and magnitud<7:
    categoria="\"Muy fuerte\" (puede causar daños significativos)."
else:
    categoria="\"Extremo\" (puede causar graves daños a gran escala)."
    
print(categoria)

#EJERCICIO 10

hemisferio=""
mes=""
dia=0
estacion_norte=""
estacion_sur=""

hemisferio=input("Ingrese el hemisferio (N/S): ").lower()
mes=input("Ingrese el mes: ")
dia=int(input("Ingrese el día: "))
mes_minus=mes.lower()

if dia<=0 or dia>31:
    print("Ingrese un día válido.")
else:
    if mes_minus=="diciembre":
        if dia>=21 and dia<=31:
            estacion_norte="Invierno"
            estacion_sur="Verano"
        elif dia<=20 and dia>0:
            estacion_norte="Otoño"
            estacion_sur="Primavera"
    elif mes_minus=="enero":
        if dia>0 and dia<=31:
            estacion_norte="Invierno"
            estacion_sur="Verano"
    elif mes_minus=="febrero":
        if dia>0 and dia<=29:
            estacion_norte="Invierno"
            estacion_sur="Verano"
    elif mes_minus=="marzo":
        if dia>0 and dia<=20:
            estacion_norte="Invierno"
            estacion_sur="Verano"
        elif dia>=21 and dia<=31:
            estacion_norte="Primavera"
            estacion_sur="Otoño"
    elif mes_minus=="abril" or mes_minus=="mayo":
        if dia>0 and dia<=30: 
            estacion_norte="Primavera"
            estacion_sur="Otoño"
    elif mes_minus=="junio":
        if dia>0 and dia<=20:
            estacion_norte="Primavera"
            estacion_sur="Otoño"
        elif dia>=21:
            estacion_norte="Verano"
            estacion_sur="Invierno"
    elif mes_minus=="julio" or mes_minus=="agosto":
        if dia>0 and dia<=31:
            estacion_norte="Verano"
            estacion_sur="Invierno"
    elif mes_minus=="septiembre":
        if dia>0 and dia<=20:
            estacion_norte="Verano"
            estacion_sur="Invierno"
        elif dia>=21:
            estacion_norte="Otoño"
            estacion_sur="Primavera"
    elif mes_minus=="octubre":
        if dia>0 and dia<=31:
            estacion_norte="Otoño"
            estacion_sur="Primavera"
    elif mes_minus=="noviembre":
        if dia>0 and dia<=30:
            estacion_norte="Otoño"
            estacion_sur="Primavera"
    else:
        print("Ingrese un mes valido.")
        exit()

if hemisferio=="n":
    print(f"Estación hemisferio norte: {estacion_norte}")
elif hemisferio=="s":
    print(f"Estación hemisferio sur: {estacion_sur}")
else:
    print("Ingrese una estación valida")