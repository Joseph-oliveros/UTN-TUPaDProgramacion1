dia,dd,mm=(input("Ingrese la fecha actual en formato\
dia/DD/MM: ")).split()

dia=dia.lower()

if len(dd) !=2 or len(mm) !=2:
    print("¡Fecha invalida!")
    exit()
else:
    pass

dd=int(dd)
mm=int(mm)

lista_dias=["lunes","martes","miercoles","jueves","\
viernes","sabado","domingo"]

if dia not in lista_dias:
    print("Ese dia no existe!")
elif dd<=0 or dd>31:
    print("El dia no puede ser cero o mayor a 31")
else:
    print(f"{dia} {dd}/{mm:02d}")

examenes=["lunes","martes","miercoles"]

if dia in examenes:
    aprobados=int(input("Ingrese cuantos alumnos aprobaron: "))
    desaprobados=int(input("Ingrese cuantos alumnos desaprobaron: "))
    total=aprobados+desaprobados
    porcen_aprobados=aprobados/total*100
    print(f"El porcentaje de aprobados es: {porcen_aprobados:.2f}")

elif dia=="jueves":
    porc_asistencia=float(input("ingrese porcentaje de asistencia: "))
    if porc_asistencia>50:
        print("Asistió la mayoria.")
    else:
        print("No asistió la mayoria.")

elif dia=="viernes":
    if dd==1 and (mm==1 or mm==7):
        print("Comienzo de nuevo ciclo.")
        alumnos=int(input("Ingrese la cantidad de alumnos: "))
        arancel=float(input("Ingrese el arancel en $ por cada alumno: "))
        ingreso_total=alumnos*arancel
        print(f"El ingreso total fue ${ingreso_total:.2f}")
    else:
        print("No hay actividades")    

    
