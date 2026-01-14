# --- INICIO DEL PROGRAMA CRM (Bloque 1: Alta con Validaciones) ---

base_datos_clientes = []

print("--- REGISTRO DE NUEVO CLIENTE (CON VALIDACIONES) ---")

# 1. Validación de ID (Solo números)
while True:
    id_cliente = input("Ingrese el ID del cliente (Solo números): ")
    if id_cliente.isdigit() and len(id_cliente) > 0:
        break # Rompe el ciclo si es dígito
    else:
        print("❌ Error: El ID debe contener solo números y no estar vacío.")

# 2. Validación de Nombre (Solo letras y espacios)
while True:
    nombre = input("Ingrese el Nombre Completo (Solo letras): ")
    # .replace elimina espacios para verificar si el resto son letras
    if nombre.replace(" ", "").isalpha() and len(nombre) > 0:
        break
    else:
        print("❌ Error: El nombre no debe contener números ni símbolos.")

# 3. Validación de Teléfono (Solo números, longitud mínima ejemplo 8)
while True:
    telefono = input("Ingrese el Teléfono (Solo números): ")
    if telefono.isdigit() and len(telefono) >= 8:
        break
    else:
        print("❌ Error: Ingrese un teléfono válido (mínimo 8 dígitos).")

# 4. Validación de Correo (Debe contener '@' y '.')
while True:
    correo = input("Ingrese el Correo Electrónico: ")
    if "@" in correo and "." in correo:
        break
    else:
        print("❌ Error: El formato del correo es inválido (falta '@' o '.').")

# 5. Validación de Estado (Selección predefinida)
print("\nSeleccione el estado del cliente:")
print("1. Cliente potencial")
print("2. Alto interés")
print("3. En proceso de compra")
print("4. Cliente efectivo")
print("5. Super cliente")

estado_final = "" # Variable para guardar el texto final

while True:
    opcion = input("Ingrese el número de la opción (1-5): ")
    
    if opcion == "1":
        estado_final = "Cliente potencial"
        break
    elif opcion == "2":
        estado_final = "Alto interés"
        break
    elif opcion == "3":
        estado_final = "En proceso de compra"
        break
    elif opcion == "4":
        estado_final = "Cliente efectivo"
        break
    elif opcion == "5":
        estado_final = "Super cliente"
        break
    else:
        print("❌ Error: Opción no válida. Por favor ingrese un número del 1 al 5.")

# --- Creación del Registro ---
nuevo_cliente = {
    "id": id_cliente,
    "nombre": nombre,
    "telefono": telefono,
    "correo": correo,
    "estado": estado_final
}

base_datos_clientes.append(nuevo_cliente)

print("\n--- ✅ CLIENTE VALIDADO Y REGISTRADO ---")
print(base_datos_clientes)