# Creamos una lista de destino
clientes_eliminados = []

# Definir los IDs que eliminaremos
ids_a_eliminar = [1, 2, 3]

# Extraemos los que coinciden con los IDs para la lista de "eliminados"
clientes_eliminados.extend([c for c in clients if c["id"] in ids_a_eliminar])

# Sobreescribimos la lista original solo con los que no están en la lista de IDs
clients = [c for c in clients if c["id"] not in ids_a_eliminar]

print(f"Usuarios eliminados:")
for eliminado in clientes_eliminados:
    print(f"- ID {eliminado['id']}: {eliminado['nombre_completo']}")

print(f"\nNúmero de usuarios restantes en la base de datos: {len(clients)}")