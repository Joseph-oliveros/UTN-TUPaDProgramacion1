#EJERCICIO 1

for i in range(0,101):
    print(i)

#EJERCICIO 2

num=int(input("Ingrese un numero entero: "))

if num==0:
    digitos=1
else:
    digitos=0

while num>0:
    num=num//10
    digitos=digitos+1

print(f"El número tiene {digitos} digitos.")

#EJERCICIO 3

num1=0
num2=0

num1=int(input("Elija un número: "))
num2=int(input("Elija otro número: "))

menor=min(num1,num2)    #devuelve el menor entre num1 y num2
mayor=max(num1,num2)    #devuelve el mayor entre num1 y num2

sumatoria=0

for i in range(menor+1,mayor,1):
    sumatoria+=i
    
print(f"La sumatoria de los numeros que están entre los suyos es: {sumatoria}") 

#EJERCICIO 4

suma=0

while True:
    num=int(input("Ingrese un número (0 para detener): "))
    if num!=0:
        suma+=num
    else:
        break

print(f"La suma total es: {suma}")
    
#EJERCICIO 5

import random

intentos=0
aleatorio=0

aleatorio=random.randint(0,9)

while True:
    intentos+=1
    num=int(input("Ingrese un número aleatorio: "))

    if num<0 or num>9:
        print("Numero fuera de rango, ¡vuelva a intentar!")
        continue

    if num==aleatorio:
        print("¡Usted acertó el número!")
        print(f"Sus intentos fueron {intentos}")
        break
    
    else:
        print("¡Casi! ¡Casi!")

#EJERCICIO 6

for i in range(100,-1,-2):
    print(i)

#EJERCICIO 7

num=int(input("Ingrese un número: "))
suma=0
for i in range(0,num+1):
    suma+=i    

print(f"La suma de números comprendidos entre 0 y el suyo: {suma}")

#EJERCICIO 8

par=0
impar=0
negativo=0
positivo=0

for i in range(100):
    num=int(input("Ingrese un número: "))
    if num%2!=0:
        impar+=1
    else:
        par+=1

    if num<0:
        negativo+=1
    elif num>0:
        positivo+=1

print(f"Pares: {par}")
print(f"Impares: {impar}")
print(f"Negativos: {negativo}")
print(f"Positivos: {positivo}")

#EJERCICIO 9

n=5
sumatoria=0
media=0
num=0

for i in range(n):
    num=int(input("Ingrese un número: "))
    sumatoria+=num

media=sumatoria/n
    
print(f"La media es: {media}")

#EJERCICIO 10

num=input("Ingrese un número: ")

invertido=num[::-1] #slicing (inicio,fin,paso)

print(f"El número invertido es: {invertido}")