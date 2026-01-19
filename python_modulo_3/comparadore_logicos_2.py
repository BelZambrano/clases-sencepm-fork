genero = input("ingresa tu genero: ")
edad = int(input("ingresa tu edad: "))
ciudad = input("Eres local o forastero?")


if (genero == "genero fluido") or (edad >= 60) or (ciudad == "local") :
    print("Gratis")
elif (genero == "mujer") and (edad >= 25):
    print("Entra gratis")
elif (genero == "mujer") and ( edad >= 18):
    print("paga")
elif (genero == "hombre") and (30 <= edad <= 40):
    print("50% de desscuento")
elif genero == "hombre":
    print("paga")
else:
    print("no entra")
