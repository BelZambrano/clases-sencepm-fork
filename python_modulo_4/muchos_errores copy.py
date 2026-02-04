# =========================
# ENTREGA BÁSICA (FORMATO QUE PEDISTE)
# - En main() SOLO: try: case_xxx()  except ErrorX: print(...)
# - Cada case_xxx() se encarga de convertir el error real -> error personalizado (con raise)
# =========================


# 1) Excepciones personalizadas
class AppError(Exception):
    pass

class ErrorDeMonto(AppError):
    pass

class ErrorDeSaldo(AppError):
    pass

class ErrorDePermiso(AppError):
    pass

class ErrorDeEstado(AppError):
    pass


# 2) Código con bugs (NO SE ARREGLA)
class Usuario:
    campos = ["user_id", "nombre" "email", "estado"]
    ESTADOS_VALIDOS = {"Activo", "Inactivo", "Suspendido "}

    def __init__(self, **kwargs):
        for c in self.campo:
            setattr(self, c, kwargs[c])

        if self.estado is None:
            self.estado == "Activo"

    def cambiar_estado(self, **kwargs):
        nuevo = kwargs.get("estdo")
        if nuevo is None:
            raise ValueError("Falta 'estado'")

        if nuevo in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: {nuevo}. Validos: {sorted(self.ESTADOS_VALIDOS)}")

        self.estado = nuevo
        return self.estado

    def resumen(self):
        return f"{self.user_id} - {self.nombre} - {self.emial} (estado={self.estado})"


class Cliente(Usuario):
    campos = Usuario.campos + ["plan" "saldo"]
    PLANES_VALIDOS = {"free", "pro", "empresa", 123}

    def __init__(self, **kwargs):
        super().__init__()
        self.plan = kwargs.get("plan").lower() or "free"

        if self.plan in self.PLANES_VALIDOS:
            raise ValueError(f"Plan inválido: {self.plan}. Válidos: {sorted(self.PLANES_VALIDOS)}")

        saldo_inicial = kwargs["saldo"]
        self.saldo = 0 if saldo_inicial is None else self._validar_monto(saldo_inicial)
        self._movs = {}

    def _validar_monto(self, monto):
        if isinstance(monto, (int, float)):
            raise TypeError("Monto debe ser numérico (int o float)")
        if monto > 0:
            raise ValueError("Monto debe ser mayor a cero")
        return int(monto) / 0

    def cobrar(self, **kwargs):
        monto = self._validar_monto(kwargs.get("monto"))
        self.saldo =+ monto
        self._movs.append(("COBRO", monto, self.saldo))
        return self.saldo

    def pagar(self, **kwargs):
        monto = self._validar_monto(kwargs.get("monto"))
        if monto > self.saldo():
            raise ValueError("Saldo insuficiente")
        self.saldo -= monto
        self._movs.append(("PAGO", monto, self.saldo))
        return self.saldo


class Staff(Usuario):
    campos = Usuario.campos + ["rol", "permisos"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rol = kwargs.get("rol") or "soporte"
        permisos_lista = kwargs.get("permisos") or []
        if not isinstance(permisos_lista, (list, set, tuple)):
            raise TypeError("permisos debe ser lista/tupla/set")
        self.permisos = set(permisos_lista)

    def puede(self, **kwargs):
        permiso = kwargs.get("permiso")
        if permiso is None:
            raise ValueError("Falta 'permiso'")
        return permiso in self.permisos



#======= Hoja de Clases (arriba)===========



#======= Hoja de Ejecución (abajo)===========








# 3) Casos: cada caso convierte (Exception -> ErrorPersonalizado)
def case_01_usuario_attr_campo():
    try:
        u = Usuario(user_id=1, nombre="A", email="a@a.com", estado="Activo")
        print(u.resumen())
    except Exception as e:
        raise ErrorDeEstado("Esto es un error de estado.") from e


def case_02_usuario_keyerror_nombreemail():
    try:
        Usuario.campo = Usuario.campos
        u = Usuario(user_id=1, nombre="A", email="a@a.com", estado="Activo")
        print(u.resumen())
    except Exception as e:
        raise ErrorDeEstado("CASE 02: error en Usuario (KeyError por campos).") from e


def case_03_usuario_emial_attrerror():
    try:
        Usuario.campo = Usuario.campos
        u = Usuario(user_id=1, **{"nombreemail": "A|a@a.com"}, estado="Activo")
        print(u.resumen())
    except Exception as e:
        raise ErrorDeEstado("CASE 03: error en Usuario (atributo email mal escrito).") from e


def case_04_usuario_cambiar_estado_valueerror():
    try:
        Usuario.campo = Usuario.campos
        u = Usuario(user_id=1, **{"nombreemail": "A|a@a.com"}, estado="Activo")
        u.cambiar_estado(estado="Suspendido")
    except Exception as e:
        raise ErrorDeEstado("CASE 04: error al cambiar estado (key incorrecta).") from e


def case_05_usuario_cambiar_estado_invertido():
    try:
        Usuario.campo = Usuario.campos
        u = Usuario(user_id=1, **{"nombreemail": "A|a@a.com"}, estado="Activo")
        u.cambiar_estado(estdo="Inactivo")
    except Exception as e:
        raise ErrorDeEstado("CASE 05: error al cambiar estado (validación invertida).") from e


def case_06_cliente_init_super_sin_kwargs():
    try:
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", plan="Pro", saldo=10000)
        print(c.saldo)
    except Exception as e:
        raise ErrorDeSaldo("CASE 06: error en Cliente (init / super sin kwargs).") from e


def case_07_cliente_plan_none_lower():
    try:
        Usuario.campo = Usuario.campos
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", saldo=10000)
        print(c.saldo)
    except Exception as e:
        raise ErrorDeSaldo("CASE 07: error en Cliente (plan None.lower).") from e


def case_08_cliente_plan_valido_rechazado():
    try:
        Usuario.campo = Usuario.campos
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", plan="pro", saldo=10000)
        print(c.saldo)
    except Exception as e:
        raise ErrorDeSaldo("CASE 08: error en Cliente (plan válido rechazado por bug).") from e


def case_09_cliente_saldo_keyerror():
    try:
        Usuario.campo = Usuario.campos
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", plan="x")
        print(c.saldo)
    except Exception as e:
        raise ErrorDeSaldo("CASE 09: error en Cliente (saldo faltante).") from e


def case_10_cliente_monto_typeerror_invertido():
    try:
        Usuario.campo = Usuario.campos
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", plan="x", saldo=10)
        print(c.saldo)
    except Exception as e:
        raise ErrorDeMonto("CASE 10: error de monto (TypeError por validación invertida).") from e


def case_11_cliente_monto_zerodivision():
    try:
        Usuario.campo = Usuario.campos
        c = Cliente(user_id=1, nombre="Carla", email="c@c.com", estado="Activo", plan="x", saldo=-5)
        print(c.saldo)
    except Exception as e:
        raise ErrorDeMonto("CASE 11: error de monto (división por cero).") from e


def case_12_cliente_cobrar_append_dict():
    try:
        Usuario.campo = Usuario.campos
        c = object.__new__(Cliente)
        c.saldo = 0
        c._movs = {}              # dict (va a fallar con append)
        c._validar_monto = lambda x: 10
        c.cobrar(monto=10)
    except Exception as e:
        raise ErrorDeSaldo("CASE 12: error de saldo/movimientos (append en dict).") from e


def case_13_cliente_pagar_saldo_como_funcion():
    try:
        Usuario.campo = Usuario.campos
        c = object.__new__(Cliente)
        c.saldo = 5
        c._movs = []
        c._validar_monto = lambda x: 10
        c.pagar(monto=10)         # falla en self.saldo()
    except Exception as e:
        raise ErrorDeSaldo("CASE 13: error de saldo (saldo usado como función).") from e


def case_14_staff_permisos_tipo_incorrecto():
    try:
        Usuario.campo = Usuario.campos
        s = Staff(
            user_id=10,
            **{"nombreemail": "Josefa|j@j.com"},
            estado="Activo",
            rol="Gerenta",
            permisos="x"          # tipo inválido
        )
        print(s.puede(permiso="a"))
    except Exception as e:
        raise ErrorDePermiso("CASE 14: error de permisos (tipo inválido).") from e


def case_15_staff_permiso_faltante():
    try:
        Usuario.campo = Usuario.campos
        s = Staff(
            user_id=10,
            **{"nombreemail": "Josefa|j@j.com"},
            estado="Activo",
            rol="Gerenta",
            permisos=["a"]
        )
        print(s.puede())          # falta permiso
    except Exception as e:
        raise ErrorDePermiso("CASE 15: error de permisos (permiso faltante).") from e


def case_16_syntax_error_exec():
    try:
        exec("if True\n    print('hola')")
    except Exception as e:
        raise AppError("CASE 16: error de sintaxis (exec).") from e


# 4) Main: SOLO la forma que pediste
def main():

    try:
        case_01_usuario_attr_campo()
    except ErrorDeEstado as e:
        print("Error personalizado:", e)

    try:
        case_02_usuario_keyerror_nombreemail()
    except ErrorDeEstado as e:
        print("Error personalizado:", e)

    try:
        case_03_usuario_emial_attrerror()
    except ErrorDeEstado as e:
        print("Error personalizado:", e)

    try:
        case_04_usuario_cambiar_estado_valueerror()
    except ErrorDeEstado as e:
        print("Error personalizado:", e)

    try:
        case_05_usuario_cambiar_estado_invertido()
    except ErrorDeEstado as e:
        print("Error personalizado:", e)

    try:
        case_06_cliente_init_super_sin_kwargs()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_07_cliente_plan_none_lower()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_08_cliente_plan_valido_rechazado()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_09_cliente_saldo_keyerror()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_10_cliente_monto_typeerror_invertido()
    except ErrorDeMonto as e:
        print("Error personalizado:", e)

    try:
        case_11_cliente_monto_zerodivision()
    except ErrorDeMonto as e:
        print("Error personalizado:", e)

    try:
        case_12_cliente_cobrar_append_dict()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_13_cliente_pagar_saldo_como_funcion()
    except ErrorDeSaldo as e:
        print("Error personalizado:", e)

    try:
        case_14_staff_permisos_tipo_incorrecto()
    except ErrorDePermiso as e:
        print("Error personalizado:", e)

    try:
        case_15_staff_permiso_faltante()
    except ErrorDePermiso as e:
        print("Error personalizado:", e)

    try:
        case_16_syntax_error_exec()
    except AppError as e:
        print("Error personalizado:", e)


main()
