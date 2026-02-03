class Usuario:
    datos = ["nombre" , "apellido"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c, None))


class Cliente(Usuario):
    datos = ["nombre", "apellido", "tipo_cliente"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c, None))


class Repartidor(Usuario):
    datos = ["nombre", "apellido", "disponibilidad"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c, None))


class Admin(Usuario):
    datos = ["nombre", "apellido", "activo", "nivel_acceso"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c, None))
            

a = Admin(id=1, nombre="Juan", apellido="Perez", activo=True, nivel_acceso=1)


print(a.nombre)
print(a.apellido)
print(a.activo)
print(a.nivel_acceso)

b=Repartidor(id=2, nombre="Pedro", apellido="Gomez", disponibilidad=True)

print(b.nombre)
print(b.apellido)
print(b.disponibilidad)

c=Cliente(id=3, nombre="Maria", apellido="Lopez", tipo_cliente="Premium")

print(c.nombre)
print(c.apellido)
print(c.tipo_cliente)
