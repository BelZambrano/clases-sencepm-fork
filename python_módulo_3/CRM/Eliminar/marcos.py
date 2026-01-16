clientes_eliminados = []
seguir = "s"

while seguir == "s":
    #Lista de clientes a eliminar
    print("\nClientes disponibles:")
    for c in clients:
        print(c["id"], "-", c["nombre_completo"])

    #Ingreso del cliente a eliminar
    id_eliminar = int(input("\nID del cliente a eliminar: "))

    #Busco el cliente ingresado en la lista clients, lo elimino y lo agrego a la lista clientes_eliminados
    for c in clients:
        if c["id"] == id_eliminar:
            clients.remove(c)
            clientes_eliminados.append(c)
            print("Cliente eliminado:", c["nombre_completo"])
            break
    else:
        print("Cliente no encontrado")

    #Seguir eliminando clientes?
    seguir = input("\n¿Eliminar otro cliente? (s/n): ").lower()

#Imprimir resultados
print("\nClientes actuales:")
for c in clients:
    print(c["id"], "-", c["nombre_completo"])

print("\nClientes eliminados:")
for c in clientes_eliminados:
    print(c["id"], "-", c["nombre_completo"])