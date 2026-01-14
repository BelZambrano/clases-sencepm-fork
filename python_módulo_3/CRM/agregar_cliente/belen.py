clientes = []
id_actual = 1

print("AGREGAR NUEVO CLIENTE")

nombre = input("Ingrese nombre: ").strip()
while nombre == "":
    print("El nombre no puede estar vacío.")
    nombre = input("Ingrese nombre: ").strip()

apellidos = input("Ingrese apellidos: ").strip()
while apellidos == "":
    print("Los apellidos no pueden estar vacíos.")
    apellidos = input("Ingrese apellidos: ").strip()

telefono = input("Ingrese teléfono (ej: +56912345678 o 912345678): ").strip()

while True:
    if telefono.startswith("+56"):
        es_valido = (
            len(telefono) == 12 and
            telefono[0:4] == "+569" and
            telefono[4:].isdigit()
        )
        if es_valido:
            break
        else:
            print("Teléfono inválido. Formato correcto: +569XXXXXXXX")
    else:
        es_valido = (
            len(telefono) == 9 and
            telefono.startswith("9") and
            telefono.isdigit()
        )
        if es_valido:
            telefono = "+56" + telefono
            break
        else:
            print("Teléfono inválido. Formato correcto: 9XXXXXXXX o +569XXXXXXXX")

    telefono = input("Ingrese teléfono (ej: +56912345678 o 912345678): ").strip()

correo = input("Ingrese correo: ").strip()

while True:
    if "@" in correo and "." in correo:
        pos_arroba = correo.find("@")
        pos_punto = correo.rfind(".")
        if pos_arroba > 0 and pos_punto > pos_arroba + 1 and not correo.endswith("."):
            break

    print("Correo inválido. Ejemplo válido: nombre@gmail.com")
    correo = input("Ingrese correo: ").strip()

print("Estados disponibles:")
print("1. Cliente potencial")
print("2. Alto interés")
print("3. En proceso de compra")
print("4. Cliente efectivo")
print("5. Super cliente")

opcion = input("Seleccione el estado del cliente (1-5): ").strip()
while opcion not in ["1", "2", "3", "4", "5"]:
    print("Opción inválida.")
    opcion = input("Seleccione el estado del cliente (1-5): ").strip()

if opcion == "1":
    estado = "Cliente potencial"
elif opcion == "2":
    estado = "Alto interés"
elif opcion == "3":
    estado = "En proceso de compra"
elif opcion == "4":
    estado = "Cliente efectivo"
else:
    estado = "Super cliente"

cliente = {
    "id": id_actual,
    "nombre": nombre,
    "apellidos": apellidos,
    "telefono": telefono,
    "correo": correo,
    "estado": estado
}

clientes.append(cliente)
id_actual += 1

print("Cliente agregado correctamente:")
print(cliente)