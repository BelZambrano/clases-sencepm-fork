edad = int(input("ingresa tu edad: "))
ciudad = input("Eres local o forastero?")

if (ciudad == "local") and not (edad > 30): 
    print("50% descuento")
elif (ciudad == "local") and (edad >= 30):
    print("gratis")
else:
    print("paga")




