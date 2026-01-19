base_datos = []

while True:
    try:
        cantidad = int(input("Cuantos productos quieres ingresar? "))
        if cantidad > 0:
            break
        print("Por favor ingrese un número mayor a 0")
    except ValueError:
        print("error: Debe ingresar un número válido entero")

for i in range(cantidad):
    print(f"Producto {i+1}")

    while True:
        sku = input("Ingrese el SKU: ").strip()
        if sku: 
            break
        print("El SKU no puede estar vacío.")

    while True:
        nombre = input("Ingresa el nombre: ").strip()
        if nombre: 
            break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            precio = int(input("Ingresa el precio: "))
            if precio > 0: break
            print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Error: Ingresa un número entero para el precio.")
    
    producto = {
        "sku": sku,
        "nombre": nombre,
        "precio": precio
    }

    base_datos.append(producto)

print("\nInformación en base de datos:")
for p in base_datos:
    print(f"SKU: {p['sku']} | Nombre: {p['nombre']} | Precio: ${p['precio']}")