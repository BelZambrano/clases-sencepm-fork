clientes = []

print("=== CRM - AGREGAR CLIENTES  ===")


seguir = True
while seguir:
    print("\n--- Nuevo cliente ---")
    
    id_cliente = input("ID: ")
    
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Nombre (solo letras): ").strip()
        if nombre.replace(" ", "").isalpha():
            nombre_valido = True
        else:
            print("Error: Solo letras.")
    
    telefono_valido = False
    while not telefono_valido:
        telefono = input("Teléfono (números/+/-): ").strip()
        if telefono.replace("+", "").replace("-", "").isdigit():
            telefono_valido = True
        else:
            print("Error: Solo números/+/-.")
    
    correo_valido = False
    while not correo_valido:
        correo = input("Correo (con @): ").strip()
        if "@" in correo:
            correo_valido = True
        else:
            print("Error: Debe tener @.")
    
    estado = input("Estado: ").strip().lower()
    
    cliente = {'id': id_cliente, 'nombre': nombre, 'telefono': telefono, 'correo': correo}
    match estado:
        case "cliente potencial": cliente['estado'] = "Cliente potencial"
        case "alto interés": cliente['estado'] = "alto interés"
        case "en proceso de compra": cliente['estado'] = "en proceso de compra"
        case "cliente efectivo": cliente['estado'] = "cliente efectivo"
        case "super cliente": cliente['estado'] = "super cliente"
        case _: cliente['estado'] = "Cliente potencial"
    
    clientes.append(cliente)
    print("✓ Cliente agregado.")
    
    continuar = input("\n¿Agregar otro? (s/n): ").strip().lower()
    if continuar == "n":
        seguir = False

print("\n=== BASE DE CLIENTES CRM ===")
for c in clientes:
    print(c)
print(f"Total: {len(clientes)} clientes.")