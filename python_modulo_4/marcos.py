class Usuario:
    campos = ["nombre", "email", "telefono", "direccion"]

    def __init__(self, **kwargs):
        for campo in self.campos:
            setattr(self, campo, kwargs.get(campo))
        self.activo = True

    def autenticar(self) -> bool:
        return self.activo

    def actualizar_contacto(self) -> None:
        return None

    def desactivar(self) -> None:
        self.activo = False


class Cliente(Usuario):
    campos = Usuario.campos + ["direccion_entrega_preferida", "metodo_pago_preferido", "puntos_fidelidad"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.historial = []
        
        if getattr(self, "puntos_fidelidad", None) is None:
            self.puntos_fidelidad = 0

    def crear_pedido(self):
        pedido = "pedido"
        self.historial.append(pedido)
        return pedido

    def pagar_pedido(self) -> bool:
        return True

    def ver_historial(self) -> list:
        return self.historial


class Repartidor(Usuario):
    campos = Usuario.campos + ["vehiculo_tipo", "zona", "disponible"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if getattr(self, "disponible", None) is None:
            self.disponible = True

    def aceptar_pedido(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True
        return False

    def actualizar_estado_entrega(self) -> None:
        return None

    def marcar_disponible(self) -> None:
        self.disponible = True


class Admin(Usuario):
    campos = Usuario.campos + ["rol", "permisos"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if getattr(self, "permisos", None) is None:
            self.permisos = []

    def gestionar_restaurante(self) -> None:
        return None

    def actualizar_producto(self) -> None:
        return None

    def asignar_repartidor(self) -> None:
        return None


# EJEMPLO DE USO

# ---------- Usuario ----------
usuario = Usuario(
    nombre="Carlos",
    email="carlos@email.com",
    telefono="911111111",
    direccion="Av. Central 100"
)

print("Usuario autenticado:", usuario.autenticar())
usuario.desactivar()
print("Usuario autenticado después de desactivar:", usuario.autenticar())

print("-" * 40)

# ---------- Cliente ----------
cliente = Cliente(
    nombre="María",
    email="maria@email.com",
    telefono="922222222",
    direccion="Calle 45",
    direccion_entrega_preferida="Calle 45, Depto 3",
    metodo_pago_preferido="Tarjeta"
)

pedido1 = cliente.crear_pedido()
pedido2 = cliente.crear_pedido()

print("Pedido creado:", pedido1)
print("Pedido creado:", pedido2)
print("Pago realizado:", cliente.pagar_pedido())
print("Historial del cliente:", cliente.ver_historial())

print("-" * 40)

# ---------- Repartidor ----------
repartidor = Repartidor(
    nombre="Juan",
    email="juan@delivery.com",
    telefono="933333333",
    direccion="Base Norte",
    vehiculo_tipo="Moto",
    zona="Centro",
    disponible=True
)

print("Repartidor acepta pedido:", repartidor.aceptar_pedido())
print("Repartidor acepta otro pedido:", repartidor.aceptar_pedido())
repartidor.marcar_disponible()
print("Repartidor disponible nuevamente:", repartidor.disponible)

print("-" * 40)

# ---------- Admin ----------
admin = Admin(
    nombre="Ana",
    email="ana@admin.com",
    telefono="944444444",
    direccion="Oficina Central",
    rol="Administrador",
    permisos=["crear", "editar"]
)

admin.gestionar_restaurante()
admin.actualizar_producto()
admin.asignar_repartidor()

print("Acciones de admin ejecutadas correctamente")