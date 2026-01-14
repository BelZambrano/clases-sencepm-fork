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

print("=== ECOMMERCE - LISTADO DE PRODUCTOS ===")
contador = 0
while contador < len(product_list):
    producto = product_list[contador]
    print(f"{producto['sku']} - {producto['nombre']} - ${producto['precio']:,.0f}")
    contador += 1

carrito = []
total = 0
print("\n=== Agregar al carrrit0 (ingresa SKU o 'listo') ===")
while True:
    sku_input = input("SKU: ").strip().upper()
    if sku_input == "LISTO":
        break
    encontrado = False
    contador = 0
    while contador < len(product_list):
        if product_list[contador]["sku"] == sku_input:
            carrito.append(product_list[contador])
            total += product_list[contador]["precio"]
            print(f"✓ Agregado: {product_list[contador]['nombre']}")
            encontrado = True
            break
        contador += 1
    if not encontrado:
        print("SKU no encontrado")

print("\n=== CARRITO ===")
contador = 0
while contador < len(carrito):
    print(f"{carrito[contador]['sku']} - {carrito[contador]['nombre']} - ${carrito[contador]['precio']:,.0f}")
    contador += 1

print(f"\nSUBTOTAL: ${total:,.0f}")
descuento_productos = ["P1003", "P1007", "P1010"]
total_normal = 0
contador = 0
while contador < len(carrito):
    if carrito[contador]["sku"] not in descuento_productos:
        total_normal += carrito[contador]["precio"]
    contador += 1

if total >= 100000:
    descuento = total_normal * 0.10
    total_final = total - descuento
    print(f"Descuento 10% en productos normales: -${descuento:,.0f}")
    print(f"TOTAL FINAL: ${total_final:,.0f}")
else:
    print("Total menor a $100.000 - Sin descuento")