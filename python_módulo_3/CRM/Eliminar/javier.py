id_a_eliminar = int(input("ID a eliminar: "))

clientes_eliminados = []

encontrado = False
for cliente in clients[:]:
    if cliente["id"] == id_a_eliminar:
        print(f"Eliminando: {cliente['nombre_completo']} ({cliente['estado']})")
        clients.remove(cliente)
        clientes_eliminados.append(cliente)
        encontrado = True
        break

if not encontrado:
    print("ID no existe.")

if input("\nMostrar listas? (s/n): ").lower() == 's':
    print("\nACTIVOS:", [f"{c['id']}-{c['nombre_completo'][:12]}" for c in clients])
    print("ELIMINADOS:", [f"{c['id']}-{c['nombre_completo'][:12]}" for c in clientes_eliminados])