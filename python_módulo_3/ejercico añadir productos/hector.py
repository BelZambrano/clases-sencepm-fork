productos = []

while True:
    try:
        cantidad_productos = int(input("ingrese la cantidad de productos: "))
        if cantidad_productos < 1:
            print("la cantidad de productos debe ser mayor a 0")
            continue
        break
    except ValueError:
        print("la cantidad de productos debe ser un número")
        continue

for i in range(cantidad_productos):
    while True:
        try:
            nombre_producto = input("ingrese el nombre del producto: ")
            break
        except ValueError:
            print("el nombre del producto no puede estar vacío")
            continue
    while True:
        try:
            precio_producto = int(input("ingrese el precio del producto: "))
            break
        except ValueError:
            print("el precio del producto debe ser un número")
            continue

    producto = {
        "SKU": "000" + str(i + 1),
        "nombre": nombre_producto,
        "precio": precio_producto
    }

    productos.append(producto)

#print(productos)
for producto in productos:
    print(
        "|",
        producto["SKU"],
        "|",
        producto["nombre"],
        "|",
        producto["precio"],
        "|"
    )