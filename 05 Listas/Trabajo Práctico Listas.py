#EJERCICIO 1

lista_100=list(range(4,101,4))
print(lista_100)

#EJERCICIO 2

lista=[1,2,3,4,5]

print(lista[-2])

#EJERCICIO 3

lista_vacia=[]

lista_vacia.append("auto")
lista_vacia.append("moto")
lista_vacia.append("casa")

print(lista_vacia)

#EJERCICIO 4

animales=["perro","gato","conejo","pez"]
print(animales)

animales[1]="loro"
animales[-1]="oso"

print(animales)

#EJERCICIO 5

#Lo que pasa en este programa es que esta eliminando con el metodo remove
#el número mayor de nuestra lista, que fue buscado atraves de la funcion max
#que nos de vuelve el mayor.

#EJERCICIO 6

lista1=list(range(10,31,5))
print(lista1)

print(lista1[0])
print(lista1[1])

#EJERCICIO 7

autos=["sedan","polo","suran","gol"]
print(autos)

autos[1]="amarok"
autos[2]="bora"

print(autos)

#EJERCICIO 8

dobles=[]

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#EJERCICIO 9

compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
print(compras)

compras[2].append("jugo")
print(compras)

compras[1][1]="tallarines"
print(compras)

compras[0].remove("pan")
print (compras)

#EJERCICIO 10

lista_anidada=[15,True,[25.5,57.9,30.6],False]
print(lista_anidada)
