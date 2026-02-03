class Persona:
    campos = ["nombre", "edad"]

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))

    def presentarse(self):
        print(f"Hola  mi nombre es {self.nombre} y mi edad es {self.edad}")

class Empleado(Persona):
    campos = Persona.campos + ["cargo"]
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cargo = kwargs.get("cargo")

    def presentarse(self):
        print(f"Hola  mi nombre es {self.nombre} y mi edad es {self.edad} y mi cargo es {self.cargo}")

    def trabajar(self):
        print(f"{self.nombre} ya está trabajando como {self.cargo}")


e1 = Empleado(nombre= "Ana", edad= "50", cargo= "Analista")
e1.presentarse()
e1.trabajar()
print(e1.nombre)



#--------------------------------------------
#--------------------------------------------
#--------------------------------------------



class Animal:
    campos = ["nombre"]

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))

    def emitir_sonido(self):
        print("Sonigo genérico")


class Perro(Animal):
    def emitir_sonido(self):
        print("guau") 

class Gato(Animal):
    def emitir_sonido(self):
        print("miau")       


a1 = Perro(nombre= "Baboy")
a2 = Gato(nombre= "Mishi")

a1.emitir_sonido()
a2.emitir_sonido()



#--------------------------------------------
#--------------------------------------------
#--------------------------------------------



class Volador:

    def __init__(self, **kwargs):
        pass

    def moverse(self):
        print("Estoy volando")

class Nadador:
    def __init__(self, **kwargs):
        pass


    def moverse(self):
        print("Estoy nadando")


class Pato(Nadador, Volador):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def moverse_ambos(self):
        Volador.moverse(self)
        Nadador.moverse(self)

p = Pato()
p.moverse()

print(Pato.__mro__)

p.moverse_ambos()


    
#--------------------------------------------
#--------------------------------------------
#--------------------------------------------

class Vehiculo:
    campos = ["marca", "modelo"]

    def __init__(self, **kwargs):
        for c in self.campos:
            setattr(self, c, kwargs.get(c))

    def moverse(self):
        print("moviendose...")


class Auto(Vehiculo):

    def moverse(self):
        print("Conduciendo por la ciudad")


class Bicicleta(Vehiculo):
    def moverse(self):
        print("Pedaleando por la ciudad")

class Moto(Vehiculo):

    campos = Vehiculo.campos + ["cilindrada"]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cilindrada = kwargs.get("cilindrada")  

    def moverse(self):
        print("Moviéndome más feliz")


vehiculos = [
    Auto(marca="Toyota", modelo= "Rav 4"),
    Bicicleta(marca= "Trek", modelo= "Y3"),
    Moto(marca= "Kawasaky", modelo= "Versys", cilindrada= "650")
]


for v in vehiculos:
    v.moverse()
    