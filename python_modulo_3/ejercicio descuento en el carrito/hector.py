precio_total = 0
descuento = 0

product_list = [
    {"sku": "P1001", "nombre": "Audífonos Bluetooth", "precio": 24990},
    {"sku": "P1002", "nombre": "Teclado Mecánico", "precio": 44990},
    {"sku": "P1003", "nombre": "Mouse Gamer", "precio": 19990},
    {"sku": "P1004", "nombre": "Lámpara LED de Escritorio", "precio": 15990},
    {"sku": "P1005", "nombre": "Cargador Inalámbrico", "precio": 22990},
    {"sku": "P1006", "nombre": "Soporte para Notebook", "precio": 17990},
    {"sku": "P1007", "nombre": "Parlante Portátil", "precio": 29990},
    {"sku": "P1008", "nombre": "Cámara Web HD", "precio": 30990},
    {"sku": "P1009", "nombre": "Disco Duro Externo 500GB", "precio": 49990},
    {"sku": "P1010", "nombre": "Kit de Limpieza Electrónica", "precio": 10990},
]

sku_sin_descuento = ["P1010", "P1007", "P1003"]
carrito = []

while True:
    try:
        opcion = input("¿Desea agregar un producto? (s/n): ")
        if opcion == "s":
            try:
                sku = input("Ingrese el SKU del producto: ")
                if sku in product_list["sku"]:
                    carrito.append(sku)
                    print("Producto agregado")
                else:
                    print("SKU no existe")
            except ValueError:
                print("SKU no puede estar vacío")
                continue
        if opcion == "n":
            break
    except ValueError:
        print("Opción inválida")
        continue

for sku in carrito:
    for producto in product_list:
        if producto["sku"] == sku:
            precio_total += producto["precio"]
            break

if precio_total > 100000:
    for sku in carrito:
        if sku not in sku_sin_descuento:
            for producto in product_list:
                if producto["sku"] == sku:
                    descuento += producto["precio"] * 0.10
                    break

precio_final = precio_total - descuento

print("Total inicial:", precio_total)
print("Descuento total:", descuento)
print("Total a pagar:", precio_final)