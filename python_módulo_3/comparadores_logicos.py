entrada = input("Ingrsa un numero entero: ")



try:
    numero = int(entrada)
    if(numero % 2 == 0) and (numero % 3 == 0):
        print("Es PAR y MULTIPLO de 3")
    elif numero % 2 == 0:
        print("Solo es un numero par y no pmultiplo de 3")
    else:
        print("es impar")
except ValueError:
    print("Ingresa el dato correctamente")


try:
    numero = int(entrada)
    if(numero % 2 == 0) or (numero % 3 == 0):
        print("Es PAR o MULTIPLO de 3")
    elif numero % 2 == 0:
        print("Solo es un numero par")
    else:
        print("es impar")
except ValueError:
    print("Ingresa el dato correctamente")


genero = input("ingresa tu genero: ")
edad = int(input("ingresa tu edad: "))


if (genero == "genero fluido") or (edad >= 60):
    print("Gratis")

else:
    if (genero == "mujer") and (edad >= 25):
        print("Entra gratis")
    elif (genero == "mujer") and ( edad >= 18):
        print("paga")
    else:
        print("no entra")

#para el zen de python y buenas prácticas el da abajo es mejor que el de arriba aunque ambos funcionan y hacen lo mismo
if (genero == "genero fluido") or (edad >= 60):
    print("Gratis")
elif (genero == "mujer") and (edad >= 25):
    print("Entra gratis")
elif (genero == "mujer") and ( edad >= 18):
    print("paga")
else:
    print("no entra")



