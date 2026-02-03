'''class Usuario: 
    campos = ["user_id", "nombre", "email", "estado"]

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))
        
        if  self.estado is None:
            self.estado = "activo"

    def resumen(self):
        return f"[{self.user_id}] {self.nombre} <{self.email}> (estado={self.estado})"
    

class Cliente(Usuario):
    campos = Usuario.campos + ["plan" + "saldo"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plan = kwargs.get("plan") or "free"

        self.saldo = int(kwargs.get("saldo"))
        if self.saldo is None:
            self.saldo = 0

    def cobrar(self, **kwargs):
        monto = kwargs.get("monto", 0)
        if not isinstance(monto, (int, float)):
            raise TypeError ("monto debe ser numérico")
        if monto <= 0:
            raise TypeError("el monto debe ser mayor a 0")
        if monto > self.saldo:
            raise ValueError("saldo insuficiente")
        

    def pagar(self, **kwargs):
        monto = kwargs.get("monto", 0)
        if not isinstance(monto, (int, float)):
            raise TypeError("monto debe ser un número")
        
        if monto <= 0:
            raise ValueError("Monto debe ser mayor a cero")
        
        if monto > self.saldo:
            raise ValueError("saldo insuficiente")
        
        self.saldo -= monto
        return self.saldo
    

    def resumen(self):
        resumen_base = super().resumen()
        return f"{resumen_base} | Cliente(plan={self.plan}, saldo={self.saldo})"

    
     
class Staff(Usuario):
    campos = Usuario.campos + ["rol", "permisos"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rol = kwargs.get("rol") or "soporte"

        permisos_lista = kwargs.get("permisos") or []
        self.permisos = set(permisos_lista)

    def puede(self, **kwargs):
        permiso = kwargs.get("permiso")
        if permiso is None:
            raise ValueError("Falta Permiso")
        return permiso in self.permisos
        

    def resumen(self):
        resumen_base = super().resumen()
        return f"{resumen_base} | Staff(rol= {self.rol}), permiso={sorted(self.permisos)}"
    


cliente_1 = Cliente(user_id= 10, nombre= "Juan", email= "juanito@mail.cl", estado="activo", plan= "prepago", saldo= "10000")


staff_1 = Staff(user_id= 1, nombre= "María", email= "mari@mail.cl", rols= "manager", permisos=["ticket:responder", "cliente:editar"])




print(cliente_1.resumen)
print(staff_1.resumen)
cliente_1.cobrar(monto=5000)
cliente_1.pagar(monto=3000)
print("saldo por pagar: ", cliente_1.saldo )

print("¿Sataff_1 puede responder el ticket?", staff_1.puede(permiso="ticket:responder"))







class Vehiculo:
    datos = ["nombre", "color"]

    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c))

    def bocina(self):
        return "ruido generico"


class Auto(Vehiculo):

    def bocina(self):
        return "ruido de auto"


class Bote(Vehiculo):


    def bocina(self):
        return "ruido de bote"




a = Auto("Corolla", "rojo")
b = Bote("Lancha", "azul")
print(a.bocina()) 
print(a.bocina())

'''


'''
def formato_pesos_clp(monto):
    return "$" + format(int(monto), ",").replace(",", ".")

class Empleado:
    campos = ["nombre", "sueldo_base"]

    def __init__(self, **kwargs):
        for campo in self.campos:
            setattr(self, campo, kwargs.get(campo))

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo base: {formato_pesos_clp(self.sueldo_base)}")

    def calcular_pago(self):
        return self.sueldo_base


class Desarrollador(Empleado):
    campos = Empleado.campos + ["lenguaje"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Lenguaje: {self.lenguaje}")

    def calcular_pago(self):
        # Bono fijo por ser desarrollador
        return self.sueldo_base + 200000


class Vendedor(Empleado):
    campos = Empleado.campos + ["ventas"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ventas del mes: {formato_pesos_clp(self.ventas)}")

    def calcular_pago(self):
        # Comisión simple del 5%
        return self.sueldo_base + (self.ventas * 0.05)


# -------------------------
# Uso del programa
# -------------------------

dev = Desarrollador(nombre="María", sueldo_base=1200000, lenguaje="Python")
vend = Vendedor(nombre="Juan", sueldo_base=900000, ventas=3000000)

print("---- DESARROLLADOR ----")
dev.mostrar_info()
print("Pago total:", formato_pesos_clp(dev.calcular_pago()))

print("\n---- VENDEDOR ----")
vend.mostrar_info()
print("Pago total:", formato_pesos_clp(vend.calcular_pago()))


'''


