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

productos_con_descuento = ["P1010", "P1007", "P1003"]
carrito = []

print("LISTADO DE PRODUCTOS")
for p in product_list:
    print(p["sku"], "-", p["nombre"], "- $", p["precio"])

while True:
    sku = input("Ingresa SKU del producto (ENTER para finalizar): ").upper()
    if sku == "":
        break

    encontrado = False
    for p in product_list:
        if p["sku"] == sku:
            carrito.append(p)
            encontrado = True
            print("Producto agregado:", p["nombre"])
            break

    if not encontrado:
        print("SKU no válido")
    else:
        print("Productos en el carrito:", len(carrito))
        print("Total parcial: $", sum(item["precio"] for item in carrito))


total = 0
total_con_descuento = 0

for p in carrito:
    total += p["precio"]
    if p["sku"] not in productos_con_descuento:
        total_con_descuento += p["precio"]

descuento = 0
if total > 100000:
    descuento = total_con_descuento * 0.10

total_final = total - descuento


print("RESUMEN DEL CARRITO")
print("Total sin descuento: $", total)
print("Descuento aplicado: $", int(descuento))
print("Total a pagar: $", int(total_final))