#Sentecia condicional tradicional
opcion_texto = input("elige una opcion, (1= saldo, 2 = cambiar clave,  3 = retirar)")

if opcion_texto.isdigit():
    opcion = int(opcion_texto)

    if opcion == 1:
        print("tu saldo es $50.000")
    if opcion == 2:
        print("En este momento no podemos cambiar tu clave")
    if opcion == 3:
        print("Este cajero no tiene dinero")
    else:
        print("Opcióningresada inválida")
else:
    print("Opcion invalida, no es dígito")

#Misma sentencia de arriba pero con formato switch

opcion_texto = input("elige una opcion, (1= saldo, 2 = cambiar clave,  3 = retirar)")

if opcion_texto.isdigit():
    opcion = int(opcion_texto)

    acciones = {
        1: "tu saldo es $50.000",
        2: "En este momento no podemos cambiar tu clave",
        3: "Este cajero no tiene dinero"
    }

    print(acciones.get(opcion, "Opcióningresada inválida"))

else:
    print("Opcion invalida, no es dígito")