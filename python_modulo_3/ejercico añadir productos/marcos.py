productos = []

while True:
    try:
        cantidad = int(input("¿Cuántos productos quieres ingresar? "))
        break
    except ValueError:
        print("Error: debes ingresar un número entero válido. Intenta nuevamente.")


for i in range(cantidad):
    print("Ingreso producto ", {i + 1})

    while True:
        sku = input("SKU: ").strip()
        valido = True

        for c in sku:
            if not (c.isalpha() or c.isdigit() or c == "_"):
                valido = False
                break

        if sku != "" and valido:
            break
        print("Error: el SKU solo puede contener letras, números y _.")

    while True:
        nombre = input("Nombre: ").strip()
        if nombre != "":
            break
        print("Error: el nombre es obligatorio.")
        
    while True:
        precio = input("Precio: ").strip()

        if precio == "":
            print("Error: el precio es obligatorio.")
            continue

        try:
            precio = float(precio)
            if precio > 0:
                break
            else:
                print("Error: el precio debe ser un número positivo.")
        except ValueError:
            print("Error: el precio debe ser un número válido.")

    producto = {
        "SKU": sku,
        "Nombre": nombre,
        "Precio": precio
    }

    productos.append(producto)

print("--- BASE DE DATOS DE PRODUCTOS ---")
for p in productos:
    print("SKU: " + p["SKU"] + " | Nombre: " + p["Nombre"] + " | Precio: $" + str(p["Precio"]))