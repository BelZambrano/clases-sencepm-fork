#Escritura de clases tipo A
class Persona:

    def __init__(self, nombre, rut, email):
        self.nombre = nombre
        self.rut = rut
        self.e_mail = email


p1 = Persona(
    nombre= "Ana",
    rut= 189996654,
    email= "ana@mail.com" 
)

print(p1.__dict__)


#Escritura de clases tipo B
class Persona:

    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.rut = datos["rut"]
        self.e_mail = datos["email"]


datos_persona = {
    "nombre": "Boris",
    "apellido": "tu apellido",
    "rut": 189996654,
    "email": "Boris@mail.com" 
}

p2 = Persona(datos_persona)

print(p2.__dict__)


#Escritura de calses tipo C


class Humano:
    campos  = ["nombre", "apellido", "rut", "mail"]

    def __init__(self, **kwargs):
        for datos in self.campos:
            setattr(self, datos, kwargs.get(datos))


p3 = Humano(
    nombre= "Yayo",
    apellido = "Mi apellido",
    rut= 189996654,
    mail= "yayo@mail.com")

print(p3.__dict__)



