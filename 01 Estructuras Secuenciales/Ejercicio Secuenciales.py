#EJERCICIO PROPINAS

monto_total=float(input("Ingrese el monto total de la cuenta: "))

propina_10=monto_total*0.10
propina_15=monto_total*0.15

total_10=monto_total+propina_10
total_15=monto_total+propina_15

print(f"Propina sugerida (10%): ${propina_10:.2f}")
print(f"Total a pagar (10%): ${total_10:.2f}")
print(f"Propina sugerida (15%): ${propina_15:.2f}")
print(f"Total a pagar (15%): ${total_15:.2f}")