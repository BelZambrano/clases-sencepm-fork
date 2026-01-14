carrito = [
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

# SKUs que no reciben el 10% de descuento adicional
SKUS_EXCLUIDOS = ["P1010", "P1007", "P1003"]

subtotal_total = sum(item['precio'] for item in carrito)

descuento = 0.10

print(f"Subtotal de la compra: ${subtotal_total:,.0f}")

if subtotal_total > 100000:
    print(f"¡El total supera $100.000! Se aplicará un {descuento*100}% de descuento en ítems elegibles.")

    # Calculamos la base para el descuento: Solo productos no excluidos
    monto_elegible_descuento = sum(
        item['precio'] 
        for item in carrito 
        if item['sku'] not in SKUS_EXCLUIDOS
    )
    
    descuento_total = monto_elegible_descuento * descuento
    total = subtotal_total - descuento_total
    
    print(f"\nMonto elegible para descuento: ${monto_elegible_descuento:,.0f}")
    print(f"Descuento aplicado {descuento*100}%: -${descuento_total:,.0f}")

else:
    total = subtotal_total
    print("El total es menor a $100.000, no aplica descuento extra.")

print(f"\nTotal a pagar: ${total:,.0f}")