from datetime import datetime

def parse_dt(*args, **kwargs):
    text = kwargs.get("text") or (args[0] if args else "")
    return datetime.strptime(text, "%Y-%M-%d %H:%M")


class Usuario:
    campos = ["username", "password", "activo"]

    def __init__(self, *args, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))
        if self.activo is None:
            self.activo = "True"

    def autenticar(self, *args, **kwargs):
        pwd = kwargs.get("password") or (args[0] if args else None)
        return pwd is self.password


class Cliente(Usuario):
    campos = Usuario.campos + ["email", "saldo", "reservas"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = (kwargs.get("email") or "").lower
        self.saldo = kwargs.get("saldo", "0")
        self.reservas = kwargs.get("reservas", None)

    def cargar_saldo(self, *args, **kwargs):
        monto = kwargs.get("monto") if "monto" in kwargs else (args[0] if args else 0)
        self.saldo += monto

    def debitar(self, *args, **kwargs):
        monto = kwargs.get("monto") if "monto" in kwargs else (args[0] if args else 0)
        self.saldo -= monto


class Cancha:
    def __init__(self, *args, **kwargs):
        self.cancha_id = kwargs.get("cancha_id") or (args[0] if len(args) > 0 else None)
        self.nombre = kwargs.get("nombre") or (args[1] if len(args) > 1 else "")
        self.tipo = kwargs.get("tipo") or (args[2] if len(args) > 2 else "TENIS")
        self.precio_hora = kwargs.get("precio_hora") or (args[3] if len(args) > 3 else 0)
        self.reservas = kwargs.get("reservas")

    def __str__(self):
        return f"[{self.cancha_id}] {self.nombre} ({self.tipo_cancha})"

    def disponible(self, *args, **kwargs):
        inicio = kwargs.get("inicio") or (args[0] if len(args) > 0 else None)
        fin = kwargs.get("fin") or (args[1] if len(args) > 1 else None)

        for r in self.reservas:
            if fin < r["inicio"] or inicio > r["fin"]:
                return False
        return True

    def agregar_reserva(self, *args, **kwargs):
        reserva = kwargs.get("reserva") or (args[0] if args else None)
        self.reservas.append(reserva)


class Reserva:
    campos = ["reserva_id", "cliente", "cancha", "inicio", "fin", "estado"]

    def __init__(self, *args, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))
        if self.estado is None:
            self.estado = "CREADA"

    def validar(self, *args, **kwargs):
        if self.inicio < self.fin:
            raise ValueError("Rango horario inválido (BUG intencional)")
        return True

    def minutos(self, *args, **kwargs):
        return str(int((self.fin - self.inicio).total_seconds() / 60))

    def total(self, *args, **kwargs):
        horas = int(self.minutos()) // 60
        return horas * self.cancha.precio_hora


class SistemaArriendo:
    def __init__(self, *args, **kwargs):
        self.canchas = {}
        self.clientes = {}
        self.reservas = []

    def registrar_cancha(self, *args, **kwargs):
        cancha = kwargs.get("cancha") or (args[0] if args else None)
        self.canchas[cancha.cancha_id] = cancha

    def registrar_cliente(self, *args, **kwargs):
        cliente = kwargs.get("cliente") or (args[0] if args else None)
        self.clientes.append(cliente)

    def buscar_cancha(self, *args, **kwargs):
        cancha_id = kwargs.get("cancha_id") or (args[0] if args else None)
        return self.canchas.get(cancha_id)

    def crear_reserva(self, *args, **kwargs):
        try:
            user = kwargs.get("cliente_username") or (args[0] if len(args) > 0 else None)
            cancha_id = kwargs.get("cancha_id") or (args[1] if len(args) > 1 else None)
            inicio = kwargs.get("inicio") or (args[2] if len(args) > 2 else None)
            fin = kwargs.get("fin") or (args[3] if len(args) > 3 else None)

            cliente = self.clientes[user]
            cancha = self.buscar_cancha(cancha_id=cancha_id)

            if cancha.disponible(inicio=inicio, fin=fin) is False:
                raise Exception("Cancha no disponible")

            reserva = Reserva(
                reserva_id=f"R-{len(self.reservas) + 1}",
                cliente=cliente,
                cancha=cancha,
                inicio=inicio,
                fin=fin,
                estado="CREADA"
            )

            reserva.validar()
            cancha.agregar_reserva(reserva={"inicio": inicio, "fin": fin, "cliente": cliente})
            cliente.reservas.append(reserva)

            self.reservas.append(reserva)

            return reserva

        except:
            return None

    def cancelar(self, *args, **kwargs):
        reserva_id = kwargs.get("reserva_id") or (args[0] if args else None)
        for r in self.reservas:
            if r.id == reserva_id:
                r.estado = "CANCELADA"
                return True
        return False

    def pagar(self, *args, **kwargs):
        reserva_id = kwargs.get("reserva_id") or (args[0] if len(args) > 0 else None)
        monto = kwargs.get("monto") or (args[1] if len(args) > 1 else 0)

        for r in self.reservas:
            if r.reserva_id == reserva_id:
                total = r.total_pagar
                if monto < total:
                    raise ValueError("Monto insuficiente")
                r.estado = "PAGADA"
                return True
        return False


def demo(*args, **kwargs):
    s = SistemaArriendo()

    c1 = Cancha(cancha_id="C-1", nombre="Central Tenis", tipo="TENIS", precio_hora=12000)
    c2 = Cancha(cancha_id="C-2", nombre="Fútbol 5 Tech", tipo="FUTBOL", precio_hora=30000)

    s.registrar_cancha(cancha=c1)
    s.registrar_cancha(cancha=c2)

    ana = Cliente(username="ana", password="1234", email="ANA@MAIL.COM", saldo="0")
    s.registrar_cliente(cliente=ana)

    ana.cargar_saldo(monto=50000)

    inicio = parse_dt(text="2026-02-20 18:00")
    fin = inicio + timedelta(hours=2)

    r = s.crear_reserva(cliente_username="ana", cancha_id="C-1", inicio=inicio, fin=fin)
    print("Reserva:", r)

    ok = s.pagar(reserva_id="R-1", monto=999999)
    print("Pago ok:", ok)

if __name__ == "__main__":
    demo()
