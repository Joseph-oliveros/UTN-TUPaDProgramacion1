#EJERCICIO 1
try:
    with open ("productos.txt","w") as archivo:
        archivo.write("manzana,2000,40\n")
        archivo.write("pera,2500,35\n")
        archivo.write("banana,1500,50\n")
except FileNotFoundError:
    print("No se encontró el archivo productos.txt. Se creara uno nuevo.")

#EJERCICIO 2

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        producto,precio,cantidad = linea.strip().split(",")
        print(f"Producto: {producto} | Precio: {precio} | Cantidad: {cantidad}")
        
#EJERCICIO 3 

print("¡Agregue un nuevo producto!")

producto=input("Nombre: ")
precio=input("Precio: ")
cantidad=input("Cantidad: ")

with open("productos.txt","a") as archivo:
    archivo.write(f"{producto},{precio},{cantidad}\n")
    
print("¡Producto agregado!")

#EJERCICIO 4

productos=[]

try:
    with open ("productos.txt","r") as archivo:
        for linea in archivo:
            nombre,precio,cantidad = linea.strip().split(",")
            producto = {
                "nombre" : nombre,
                "precio" : float(precio),
                "cantidad" : int(cantidad),
            }

            productos.append(producto)
except ValueError:
    print ("Error: ingrese números válidos para el precio y la cantidad.")

print(productos)

#EJERCICIO 5

producto_buscado = input("Ingrese el nombre del producto que busca: ").lower()

encontrado = False

for p in productos:
    if p["nombre"] == producto_buscado:
        encontrado = True
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

if not encontrado:
    print("Producto inexistente.")

#EJERCICIO 6

with open ("productos.txt","w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
