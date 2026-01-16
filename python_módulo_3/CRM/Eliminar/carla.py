clientes_eliminados = []

print("LISTA DE CLIENTES:")
for c in clients:
    print(
        f"ID: {c['id']} | "
        f"Nombre: {c['nombre_completo']} | "
        f"Correo: {c['correo']} | "
        f"Teléfono: {c['telefono']} | "
        f"Estado: {c['estado']}"
    )

cliente  = None

while cliente is None:
    try:
        id_buscar = int(input("\nIngrese el ID del cliente a eliminar: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        continue

    for i, c in enumerate(clients):
        if c["id"] == id_buscar:
            indice_cliente = i
            cliente = c

    if cliente is None:
        print("Cliente no encontrado. Intente nuevamente.")

clientes_eliminados.append(cliente)
clients.pop(indice_cliente)

print("\nClientes activos:")
for c in clients:
    print(
        f"ID: {c['id']} | "
        f"Nombre: {c['nombre_completo']} | "
        f"Correo: {c['correo']} | "
        f"Teléfono: {c['telefono']} | "
        f"Estado: {c['estado']}"
    )

print("\nClientes eliminados:")
print(clientes_eliminados)