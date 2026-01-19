lista_productos = []

numero_productos = int(input('¿Cuántos productos quieres ingresar?: '))

for i in range(numero_productos):
    print(f"\nDatos del producto n° {i + 1}:")
    
    while True:
        sku = input('Ingresa el SKU: ').strip()
        if sku:
            break
        print("Vuelva a ingresar SKU (no puede estar vacío)")
    
    nombre = str(input(f'Ingresa el nombre: '))
    
    while True:
        try:
            precio = int(input('Ingresa el precio en CLP: '))
            if precio >= 0:
                break
            else:
                print("El precio no puede ser negativo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
    
    producto = {
        "sku": sku,
        "nombre": nombre,
        "precio": precio
    }
    lista_productos.append(producto)


print("\nBase de Datos de Productos:\n")
for prod in lista_productos:
    print(f"SKU: {prod['sku']} | Nombre: {prod['nombre']} | Precio: ${prod['precio']}")