class Usuario:
    campos = ["user_id", "nombre", "email", "estado"]

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))
        
        if self.estado is None:
            self.estado = "activo"

    def resumen(self):
        return f"[{self.user_id}]{self.nombre}<{self.email}>(estado={self.estado})"

    def login(self):
        print(f"{self.nombre} ha iniciado sesión.")

    def logout(self):
        print(f"{self.nombre} ha cerrado sesión.")


class Cliente(Usuario):
    campos = Usuario.campos + ["direccion", "telefono"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def registrar(self):
        print(f"Cliente {self.nombre} registrado con éxito en {self.direccion}.")


class Repartidor(Usuario):
    campos = Usuario.campos + ["vehiculo", "calificacion"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def entregar(self):
        print(f"Repartidor {self.nombre} está realizando una entrega en {self.vehiculo}.")


class Admin(Usuario):
    campos = Usuario.campos + ["nivel_acceso"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def gestionar_usuarios(self):
        print(f"Administrador {self.nombre} está gestionando usuarios.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente(user_id=1, nombre="Juan Pérez", email="juan.perez@example.com", direccion="Calle Falsa 123", telefono="555-1234")
    cliente1.registrar()
    cliente1.login()

    # Crear un repartidor
    repartidor1 = Repartidor(user_id=2, nombre="Pedro González", email="pedro.gonzalez@example.com", vehiculo="Moto", calificacion=4.8)
    repartidor1.entregar()
    repartidor1.login()

    # Crear un administrador
    admin1 = Admin(user_id=3, nombre="Ana Torres", email="ana.torres@example.com", nivel_acceso="SuperAdmin")
    admin1.gestionar_usuarios()
    admin1.login()

    # Cerrar sesión
    cliente1.logout()
    repartidor1.logout()
    admin1.logout()

    # Mostrar resúmenes
    print(cliente1.resumen())
    print(repartidor1.resumen())
    print(admin1.resumen())