
iva = 0.19

def calculo_iva(a):
    calculo_iva = a * iva
    
    return calculo_iva


def saludar_usuario(nombre):
    saludar = f"hola {nombre}"
    return saludar

nombre_usuario = input("¿Cu{al es tu nombre?")

print(saludar_usuario(nombre_usuario))



resultado = calculo_iva(10000)

print(resultado)

def factura(total):
    total_factura = (total * iva) + total

    return total_factura

print(factura(20000))


