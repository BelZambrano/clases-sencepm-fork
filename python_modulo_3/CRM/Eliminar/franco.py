clients = [
    {"id": 1, "nombre_completo": "Ana Torres", "correo": "ana.torres@correo.com", "telefono": "+56 9 42351234", "estado": "Cliente potencial"},
    {"id": 2, "nombre_completo": "Luis Ramírez", "correo": "luis.ramirez@correo.com", "telefono": "+56 9 93481234", "estado": "Alto interés"},
    {"id": 3, "nombre_completo": "Claudia Soto", "correo": "claudia.soto@correo.com", "telefono": "+56 9 78123456", "estado": "Cliente efectivo"},
    {"id": 4, "nombre_completo": "Jorge Fuentes", "correo": "jorge.fuentes@correo.com", "telefono": "+56 9 63547812", "estado": "En proceso de compra"},
    {"id": 5, "nombre_completo": "Marta Herrera", "correo": "marta.herrera@correo.com", "telefono": "+56 9 98124578", "estado": "Super cliente"},
    {"id": 6, "nombre_completo": "Carlos Díaz", "correo": "carlos.diaz@correo.com", "telefono": "+56 9 71234598", "estado": "Alto interés"},
    {"id": 7, "nombre_completo": "Francisca Rojas", "correo": "francisca.rojas@correo.com", "telefono": "+56 9 91234871", "estado": "Cliente efectivo"},
    {"id": 8, "nombre_completo": "Pedro Gutiérrez", "correo": "pedro.gutierrez@correo.com", "telefono": "+56 9 84567213", "estado": "Cliente potencial"},
    {"id": 9, "nombre_completo": "Valentina Bravo", "correo": "valentina.bravo@correo.com", "telefono": "+56 9 78341236", "estado": "Super cliente"},
    {"id": 10, "nombre_completo": "Diego Castro", "correo": "diego.castro@correo.com", "telefono": "+56 9 93456781", "estado": "En proceso de compra"},
    {"id": 11, "nombre_completo": "Camila Paredes", "correo": "camila.paredes@correo.com", "telefono": "+56 9 91234578", "estado": "Cliente potencial"},
    {"id": 12, "nombre_completo": "Andrés Molina", "correo": "andres.molina@correo.com", "telefono": "+56 9 89451236", "estado": "Cliente efectivo"},
    {"id": 13, "nombre_completo": "Patricia Silva", "correo": "patricia.silva@correo.com", "telefono": "+56 9 74382910", "estado": "Alto interés"},
    {"id": 14, "nombre_completo": "Matías Reyes", "correo": "matias.reyes@correo.com", "telefono": "+56 9 87234561", "estado": "En proceso de compra"},
    {"id": 15, "nombre_completo": "Isidora Méndez", "correo": "isidora.mendez@correo.com", "telefono": "+56 9 98127345", "estado": "Super cliente"},
    {"id": 16, "nombre_completo": "Sebastián Núñez", "correo": "sebastian.nunez@correo.com", "telefono": "+56 9 65432178", "estado": "Cliente efectivo"},
    {"id": 17, "nombre_completo": "Fernanda Loyola", "correo": "fernanda.loyola@correo.com", "telefono": "+56 9 72345681", "estado": "Alto interés"},
    {"id": 18, "nombre_completo": "Tomás Aravena", "correo": "tomas.aravena@correo.com", "telefono": "+56 9 83451234", "estado": "Cliente potencial"},
    {"id": 19, "nombre_completo": "Josefa Espinoza", "correo": "josefa.espinoza@correo.com", "telefono": "+56 9 96432187", "estado": "Cliente efectivo"},
    {"id": 20, "nombre_completo": "Ricardo Vergara", "correo": "ricardo.vergara@correo.com", "telefono": "+56 9 78912345", "estado": "Super cliente"}
]

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
