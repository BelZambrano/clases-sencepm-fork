entrada = input("Ingrsa un numero decimal: ")



try:
    numero = float(entrada)
    if numero > 0:
        print("El numero es Positivo")
        if numero >= 3:
           print("el numero es igual o mayor a tres")
        else:
           print("el numero es menor a 3")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")
except ValueError:
    print("Entrada invalida debe escribir un numero por ejemplo (3.0, -1.0, 2.7, 0)")  


print("el programa se ejecutó completo")