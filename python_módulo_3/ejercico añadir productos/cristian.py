listado_productos = []

cantidad = int(input("Ingrese la cantidad de productos a ingresar: "))

for i in range (cantidad):
    print(f"Producto {i +1}:" )
    sku = input("ingrese el SKU: ")
    producto = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))    

    productos ={
        "SKU" : sku,
        "Producto" : producto,
        "Precio" : precio
    }

    listado_productos.append(productos)

print("--- Listado de productos ---")
for p in listado_productos:
    print(f"SKU: {p['SKU']} | Producto: {p['Producto']} | Precio: ${p['Precio']:f}")