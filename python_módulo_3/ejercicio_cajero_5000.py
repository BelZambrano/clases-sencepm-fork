# Marcos

#try:
#    monto = int(input("Ingrese el monto a retirar: "))
##
##    if monto <= 0:
##        print("Monto inválido")
##    elif monto % 5000 != 0:
##        print("El monto debe ser múltiplo de 5000")
##    else:
##        billetes = monto // 5000
##        print("Retire su dinero")
##        print("Cantidad de billetes de 5000:", billetes)
##
##except ValueError:
##    print("Error: debe ingresar solo números")
#
#
##Hector 
#print("Bienvenido a tu cuenta")
#cantidad = int(input("ingrese la cantidad a retirar: "))
#if cantidad < 1 :
#    print("debes ingresar un valor positivo")
#    cantidad = int(input("ingrese la cantidad a retirar: "))
#    while cantidad % 5000 != 0 :
#        print("debes ingresar un valor multiplo de 5000")    
#        cantidad = int(input("ingrese la cantidad a retirar: "))
#    else:
#        print("Retiro exitoso, por favor toma tu dinero")
#        print("monto retirado: ", cantidad)
#
#
##Anibal
#
#monto = int(input('Ingrese un monto para retirar (el cajero solo puede entregar montos múltiplos de $5000)'))
#
#if monto % 5000 == 0:
#    print(f'Tu monto retirado es: {monto}')
#else:
#    print('Monto inválido, seleccione un valor múltiplo de $5.000')
#
#
##JAvier
#
#monto = int(input("Ingrese el monto a retirar: "))
#
#if monto <= 0:
#    print("Monto inválido. Debe ser mayor que 0.")
#elif monto % 5000 != 0:
#    print("Monto inválido. Debe ser múltiplo de 5000.")
#else:
#    billetes = monto // 5000
#    print("Retirando", monto, "pesos.")
##    print("Entregar", billetes, "billetes de 5000.")
##
##
##
###Belen
##monto = int(input("Ingrese el monto a retirar: "))
##
##if monto % 5000 == 0:
##    cantidad_billetes = monto // 5000
##    print("Se entregan", cantidad_billetes, "billetes de $5000")
##else:
##    print("Monto incorrecto. El cajero solo entrega billetes de $5000")
#
#
##Carla
#retiro = int(input("Por favor ingrese el monto a retirar, este cajero solo tiene billetes de $5.000 pesos: "))
#resto = retiro%5000
#if resto == 0 and retiro > 0:
#    print(f"Entregando ${retiro}.")
#else:
#    print("Su monto no se puede dar en billetes de $5000, por favor intente de nuevo")
#
##Mauricio
#monto = int(input("Ingrese el monto a retirar: ").strip())
#
#if monto > 0 and monto % 5000 == 0:
#    billetes = monto // 5000
#    print(f"Retiro aprobado. Entregando {billetes} billete(s) de $5000. Total: ${monto}.")
#else:
#    print("Monto inválido: el cajero solo permite montos mayores a 0 y múltiplos de $5000.")

#
##David
#
#print("Bienvenido a tu cuenta")
#cantidad = int(input("Ingrese la cantidad a retirar: ")) 
#while cantidad < 1 or cantidad % 5000 != 0:
#    print("Error: El monto debe ser positivo y múltiplo de 5000")
#    cantidad = int(input("Ingrese la cantidad a retirar: "))
#
#billetes = cantidad // 5000
#print(f"Retiro exitoso. Entregando {billetes} billete(s) de 5000.")
#
#print("Monto retirado:", cantidad)
#
#
##Daniela
#
#monto = int(input("Ingrese el monto a retirar: "))
#
#if monto <= 0:
#    print("El monto debe ser mayor que cero.")
#
#elif monto % 5000 != 0:
#    print("Monto incorrecto. El cajero solo entrega billetes de $5.000.")
#
#else:
#    billetes = monto // 5000
#    print("Retiro aprobado.")
#    print("Se entregan", billetes, "billetes de $5.000.")
#    print("Total entregado: $", monto)

#David

#monto = int(input("ingrese el monto a retirar: "))
#
#if monto %5000 ==0: 
#    print("el monto retirado es: ", monto)
#
#else:
#    print("debe ingresar un monto multiplo de $5.000")



print("Este cajero solo tiene billetes de $5.000 ingresa un numero multiplo de $5.000")

suma = 0
intentos = 0
while intentos < 3:
    monto_ingresado = input("ingresa un monto a retirar")
    try:
        monto = int(monto_ingresado)
    except ValueError:
        print("ingresa un numero entero")
        intentos += 1
        continue
        

    if monto == 0:
        print("entrada invalida ingresa un monto válido")
        intentos += 1

    elif (monto > 0) and (monto % 5000 == 0):
        print("retiro aprobado por", monto)
        break

    else:
        print("retiro rechazado")
        intentos += 1

print("fin del ejercicio")