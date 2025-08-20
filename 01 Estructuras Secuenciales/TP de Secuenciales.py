
print("Hola mundo!")


nombre=input("Ingrese su nombre porfavor: ")
print(f"Hola {nombre}!")


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
lugar_residencia=input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")


radio=float(input("Porfavor ingrese el radio de un circulo: "))
area=3.14*radio**2
perimetro=3.14*radio*2
print(f"el area del circulo es: {area:.2f}")
print(f"el perimetro del circulo es: {perimetro:.2f}")


segundos=int(input("Ingrese la cantidad de segundos que quiere saber en horas: "))
horas=segundos/3600
print(f"Sus segundos {segundos} en horas son: {horas:.2f}")


numero=int(input("Indique el numero del cual desea ver la tabla:  "))
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")


numero_1=float(input("Ingrese el primer número de la operacion (NO PUEDE SER CERO): "))
numero_2=float(input("Ingrese el segundo número de la operación (NO PUEDE SER CERO): "))
print("La suma es igual a: ",round(numero_1+numero_2))
print("La resta es igual a: ",round(numero_1-numero_2))
print("La división es igual a: ",numero_1/numero_2)
print("La multiplicación es igual a: ",round(numero_1*numero_2))




altura=float(input("Ingrese su altura en cm: "))
peso=float(input("Ingrese su peso en kg: "))
altura_metros=altura/100
imc=peso/altura_metros**2
print(f"Su indice de masa corporal (IMC) es: {imc:.2f}")


celsius=float(input("Introduzca la temperatura en grados Celsius (°C):"))
fahrenheit=celsius*1.8+32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")


numero1=float(input("Indique el primer número: "))
numero2=float(input("Indique el segundo número: "))
numero3=float(input("Indique el tercer número: "))
promedio=(numero1+numero2+numero3)//3
print(f"El promedio de sus tres números es: {promedio}")