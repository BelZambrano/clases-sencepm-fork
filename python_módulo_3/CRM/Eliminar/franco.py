clientes_eliminados = []

# 2. Mostramos la lista inicial (Mejora UX)
print("\n--- SISTEMA DE ELIMINACIÓN DE CLIENTES ---")
print("LISTA DE CLIENTES ACTUALES:")
for c in clients:
    print(f"ID: {c['id']} | Nombre: {c['nombre_completo']} | Estado: {c['estado']}")
print("-" * 60)

cliente_a_eliminar = None
indice_cliente = -1

# 3. Bucle de búsqueda robusto
while cliente_a_eliminar is None:
    try:
        id_buscar = int(input("\nIngrese el ID del cliente a eliminar: "))
    except ValueError:
        print("❌ Error: El ID debe ser un número entero.")
        continue

    # Usamos enumerate para obtener tanto el índice (i) como el cliente (c)
    for i, c in enumerate(clients):
        if c["id"] == id_buscar:
            indice_cliente = i
            cliente_a_eliminar = c
            break # Rompemos el ciclo apenas lo encontramos (Eficiencia)

    if cliente_a_eliminar is None:
        print("⚠️ Cliente no encontrado. Intente nuevamente.")

# 4. Operación de Modificación y Traslado
# MEJORA SOLICITADA: Cambiamos el estado ANTES de moverlo
print(f"\nProcesando eliminación de: {cliente_a_eliminar['nombre_completo']}...")

cliente_a_eliminar['estado'] = "Cliente eliminado"  # <--- Cambio de estado

# Agregamos a la papelera (con el nuevo estado)
clientes_eliminados.append(cliente_a_eliminar)

# Eliminamos de la lista original usando el índice encontrado (muy eficiente)
clients.pop(indice_cliente)

print(f"✅ Cliente eliminado y archivado correctamente.")

# 5. Reporte Final (Mejora visual)
print("\n" + "="*30)
print("       CLIENTES ACTIVOS")
print("="*30)
if not clients:
    print("(Lista vacía)")
else:
    for c in clients:
        print(f"ID: {c['id']} | {c['nombre_completo']} ({c['estado']})")

print("\n" + "="*30)
print("     CLIENTES ELIMINADOS")
print("="*30)
if not clientes_eliminados:
    print("(Papelera vacía)")
else:
    for c in clientes_eliminados:
        print(f"ID: {c['id']} | {c['nombre_completo']} --> ESTADO: {c['estado']}")