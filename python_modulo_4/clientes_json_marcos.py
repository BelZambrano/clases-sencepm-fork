import json

class Cliente:
    clientes = []
    campos = ["cliente_id", "nombre", "email", "telefono"]
    archivo = "config/clientes.json"

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))

    def a_dict(self):
        return {
            "cliente_id": self.cliente_id,
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono
        }

    # ---------- ARCHIVO ----------
    def guardar_en_archivo(self):
        data = [c.a_dict() for c in Cliente.clientes]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                Cliente.clientes = [Cliente(**c) for c in data]
        except FileNotFoundError:
            Cliente.clientes = []

    # ---------- NEGOCIO ----------
    def agregar_cliente(self):
        for c in Cliente.clientes:
            if c.cliente_id == self.cliente_id:
                print("Ya existe un cliente con ese ID")
                return

        Cliente.clientes.append(self)
        self.guardar_en_archivo()
        print("Cliente agregado y guardado")

    def ver_clientes(self):
        if not Cliente.clientes:
            print("No hay clientes registrados")
            return

        print("\nID | NOMBRE | EMAIL | TELÉFONO")
        print("-" * 40)
        for c in Cliente.clientes:
            print(f"{c.cliente_id} | {c.nombre} | {c.email} | {c.telefono}")

    def editar_cliente(self, cliente_id, **kwargs):
        for c in Cliente.clientes:
            if c.cliente_id == cliente_id:
                for key, value in kwargs.items():
                    if key in self.campos and value is not None and value != "":
                        setattr(c, key, value)

                self.guardar_en_archivo()
                print("Cliente actualizado y guardado")
                return

        print("Cliente no encontrado")


# ---------------- MENÚ ----------------

def menu():
    sistema = Cliente()
    sistema.cargar_desde_archivo()

    while True:
        print("\n=== MENÚ CLIENTES ===")
        print("1. Crear cliente")
        print("2. Ver clientes")
        print("3. Editar cliente")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                cliente_id = int(input("ID cliente (número): ").strip())
            except ValueError:
                print("ID inválido")
                continue

            nombre = input("Nombre: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono: ").strip()

            nuevo = Cliente(
                cliente_id=cliente_id,
                nombre=nombre,
                email=email,
                telefono=telefono
            )
            nuevo.agregar_cliente()

        elif opcion == "2":
            sistema.ver_clientes()

        elif opcion == "3":
            try:
                cliente_id = int(input("ID del cliente a editar: ").strip())
            except ValueError:
                print("ID inválido")
                continue

            print("Deja vacío lo que NO quieras cambiar.")
            nombre = input("Nuevo nombre: ").strip()
            email = input("Nuevo email: ").strip()
            telefono = input("Nuevo teléfono: ").strip()

            sistema.editar_cliente(
                cliente_id,
                nombre=nombre if nombre != "" else None,
                email=email if email != "" else None,
                telefono=telefono if telefono != "" else None
            )

        elif opcion == "0":
            print("Saliendo... (fin del sprint)")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()