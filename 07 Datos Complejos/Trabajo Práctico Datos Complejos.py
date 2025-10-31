#EJERCICIO 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300

#EJERCICIO 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#EJERCICIO 3

lista_frutas=list(precios_frutas.keys())

print(lista_frutas)

#EJERCICIO 4

agenda_telefonica={}

for i in range(5):
    nombre=input(f"Ingrese el nombre del contacto {i+1}: ")
    numero=input(f"Ingrese el número de {nombre}: ")
    agenda_telefonica[nombre]=numero

nombre_a_consultar = input("Indique el nombre para consultar el número: ")

if nombre_a_consultar in agenda_telefonica:
    print(f"El número de {nombre_a_consultar} es: {agenda_telefonica[nombre_a_consultar]}")
else:
    print(f"El contacto {nombre_a_consultar} no existe en la agenda.")

#EJERCICIO 5

frase=input("Ingrese una frase: ").lower().split()

palabras_unicas=set(frase)

diccionario = {}

for palabra in frase:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento", diccionario)

#EJERCICIO 6

alumnos = {}

for i in range(3):
    nombre=input(f"Ingrese el nombre del alumno {i+1}: ")
    lista_notas=[]
    for j in range(3):
        nota=float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        lista_notas.append(nota)
    notas=tuple(lista_notas)
    alumnos[nombre]=notas  

print("Promedios: ")
for nombre, notas in alumnos.items():
    promedio=sum(notas)/len(notas)
    print(f"{nombre}: {promedio:.2f}")

#EJERCICIO 7

aprobados_parcial1={"Ana","Juan","Luis","Sofía","Pedro"}
aprobados_parcial2={"Juan","Pedro","Marta","Carlos","Sofía"}

ambos_parciales=aprobados_parcial1 & aprobados_parcial2
print(f"Aprobaron ambos parciales: {ambos_parciales}")

solo_uno=aprobados_parcial1 ^ aprobados_parcial2
print(f"Aprobaron solo uno: {solo_uno}")

al_menos_uno=aprobados_parcial1 | aprobados_parcial2
print(f"Aprobaron al menos uno: {al_menos_uno}")

#EJERCICIO 8

diccionario={"tablet":60,"celular":80,"silla":50,"mesa":20}

producto=input("Ingrese el producto para saber su stock: ").lower()

if producto in diccionario:
    print(diccionario[producto])

agregar=input("Ingrese el producto que desea agregar unidades: ")

if agregar in diccionario:
    unidades=int(input("Indique cuátnas unidades desea agregar: "))
    diccionario[agregar]+=unidades
else:
    print("Producto inexistente.")
    

nuevo=input("Ingrese el nuevo producto: ")

if nuevo not in diccionario:
    stock_nuevo=int(input("Ingrese la cantidad del nuevo producto: "))
    diccionario[nuevo]=stock_nuevo
else:
    print("Ya existe ese producto.")

#EJERCICIO 9

diccionario={("lunes","08:00"):"Facultad",("miercoles","22:00"):"Gym",("domingo","20:00"):"Futbol"}

act=input("Indica día o horario: ").lower()

encontrado=False
for (dia,hora),actividad in diccionario.items():
    if act==dia or act==hora:
        print(f"{dia} a las {hora} : {actividad}")
        encontrado=True
        
if not encontrado:
    print("No hay actividad.")

#EJERCICIO 10

paises={"Argentina":"Buenos Aires","Chile":"Santiago"}
nuevo={}
for pais, capital in paises.items():
    nuevo[capital]=pais
print(nuevo)
