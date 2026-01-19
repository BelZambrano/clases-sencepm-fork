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

total_compra = 0
suma_para_descuento = 0

print("--- PRODUCTOS DISPONIBLES ---")
for p in product_list:
    print(f"{p['sku']}: {p['nombre']} (${p['precio']})")

while True:
    try:
        sku_usuario = input("\nIngrese SKU (o 'fin' para pagar): ").upper()
        
        if sku_usuario == "FIN":
            break
            
        encontrado = False
        for p in product_list:
            if p["sku"] == sku_usuario:
                total_compra += p["precio"]
                
                if p["sku"] not in ["P1010", "P1007", "P1003"]:
                    suma_para_descuento += p["precio"]
                
                print(f"{p['nombre']} añadido.")
                print(f"   Llevas un total de compra de: ${total_compra}")
                
                encontrado = True
                break

        if not encontrado:
            print("SKU no válido.")
            
    except Exception:
        print("Error en la entrada. Intenta de nuevo.")

descuento = 0
if total_compra > 100000:
    descuento = suma_para_descuento * 0.10
    print("\n¡Se aplicó un 10% de descuento en productos seleccionados!")

total_final = total_compra - descuento

print("\n" + "="*20)
print(f"SUBTOTAL: ${total_compra}")
print(f"DESCUENTO: -${int(descuento)}")
print(f"TOTAL FINAL: ${int(total_final)}")
print("="*20)