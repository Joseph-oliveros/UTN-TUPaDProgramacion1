#EJERCICIO 1

def imprimir_hola_mundo():
    return ("Hola mundo!")

saludar=imprimir_hola_mundo()
print(saludar)

#EJERCICIO 2

def saludar_usuario(nombre):
    return (f"¡Hola {nombre}!")

nombre_usuario=input("Ingrese su nombre: ")
saludar=saludar_usuario(nombre_usuario)
print(saludar)

#EJERCICIO 3

def informacion_personal(nombre,apellido,edad,residencia):
    return (f"Soy {nombre}, {apellido}, tengo {edad} años y vivo en {residencia}")

nombre=input("Ingrese su nombre: ").capitalize()
apellido=input("Ingrese su apellido: ").capitalize()
edad=int(input("Indique su edad: "))
residencia=input("Indique dónde reside: ").capitalize()

informacion=informacion_personal(nombre,apellido,edad,residencia)
print(informacion)

#EJERCICIO 4

def calcular_area_circulo(radio):
    return 3.14*radio**2

def calcular_perimetro_circulo(radio):
    return 2*3.14*radio

radio=float(input("Ingrese el radio: "))

area_circulo=calcular_area_circulo(radio)
print(f"El area del circulo es: {area_circulo:.2f}")

perimetro_circulo=calcular_perimetro_circulo(radio)
print(f"El perimetro del circulo es: {perimetro_circulo:.2f}")

#EJERCICIO 5

def segundos_a_horas(segundos):
    return segundos/3600

seg=int(input("Ingrese cuantos segundos desea pasar a horas: "))

resultado=segundos_a_horas(seg)
print(f"Sus segundos en horas son: {resultado:.2f} horas")

#EJERCICIO 6

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} X {i} = {numero*i}")
    
num=int(input("Ingrese un número para saber su tabla: "))

tabla_multiplicar(num)

#EJERCICIO 7

def operaciones_basicas(a,b):
    return a+b,a-b,a*b,a/b

a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

suma,resta,multiplicacion,division=operaciones_basicas(a,b)

print(f"Suma= {suma}")
print(f"Resta= {resta}")
print(f"Multiplicación= {multiplicacion}")
print(f"División= {division}")

#EJERCICIO 8

def calcular_imc(peso,altura):
    return peso/(altura**2)

peso=float(input("Ingrese se peso en kilogramos: "))
altura=float(input("ingrese su altura en metros: "))

imc=calcular_imc(peso,altura)
print(f"Su indice de masa corporal es: {imc:.2f}")

#EJERCICIO 9

def celsius_a_fahrenheit(celsius):
    return (celsius*9/5)+32

celsius=float(input("Ingrese la temperatura en grados Celsius: "))
conversion=celsius_a_fahrenheit(celsius)

print(f"{celsius:.2f}°C equivalen a {conversion:.2f}°F.")

#EJERCICIO 10

def calcular_promedio(a,b,c):
    return (a+b+c)/3

a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))

promedio=calcular_promedio(a,b,c)
print(f"El promedio de sus números es: {promedio:.2f}")
