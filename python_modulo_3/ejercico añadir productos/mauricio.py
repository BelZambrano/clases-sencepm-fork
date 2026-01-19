#Mauricio
base_de_datos = []

while True:
    # Preguntamos al administrador cuántos productos desea ingresar
    while True:
        try:
            num_productos = int(input("¿Cuántos productos quieres ingresar? "))
            if num_productos < 1:
                print("Por favor, ingrese un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Recorremos el número de productos ingresados
    for i in range(num_productos):
        print(f"\n--- Ingreso del producto {i + 1} ---")
        
        # Validación del SKU (debe ser un número)
        while True:
            sku = input("Ingrese el SKU del producto (número): ")
            if sku.isdigit():
                sku = int(sku)  # Convertimos a entero
                break
            else:
                print("SKU inválido. Debe ser un número. Intente nuevamente.")

        # Validación del nombre (debe ser una cadena de texto)
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if isinstance(nombre, str) and nombre.strip():  # Verificamos que no esté vacío
                break
            else:
                print("Nombre inválido. Debe ser una cadena de texto. Intente nuevamente.")

        # Validación del precio (debe ser un número)
        while True:
            precio_input = input("Ingrese el precio del producto (número): ")
            try:
                precio = float(precio_input)  # Intentamos convertir a float
                if precio < 0:
                    print("El precio no puede ser negativo. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("Precio inválido. Debe ser un número. Intente nuevamente.")

        # Creamos un diccionario para el producto
        producto = {
            "sku": sku,
            "nombre": nombre,
            "precio": precio
        }
        
        # Agregamos el diccionario a la base de datos
        base_de_datos.append(producto)

    # Imprimimos la base de datos ingresada
    print("\n--- Base de datos de productos ---")
    for producto in base_de_datos:
        print(f"SKU: {producto['sku']}, Nombre: {producto['nombre']}, Precio: {producto['precio']:.2f}")

    # Preguntar si se desean ingresar más productos
    continuar = input("\n¿Desea ingresar más productos? (s/n): ").strip().lower()
    if continuar != 's':
        print("¡Gracias por usar el sistema!")
        break  # Salir del bucle''