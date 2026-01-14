import sys

# Función auxiliar para formato chileno ($1.000)
def formato_clp(valor):
    return f"${valor:,.0f}".replace(",", ".")

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

# SKUs que no reciben descuento (pero ayudan a llegar a la meta)
excluidos = ["P1010", "P1007", "P1003"]

carrito = []
total_bruto = 0

print(f"\n{' CATÁLOGO E-COMMERCE ':*^40}")
for i, item in enumerate(product_list):
    precio_str = formato_clp(item['precio'])
    # Marcamos visualmente los productos en "Oferta" (excluidos del descuento global)
    marca = " [OFERTA YA APLICADA]" if item['sku'] in excluidos else ""
    print(f"{i + 1}. {item['nombre']:<25} | {precio_str}{marca}")

print("-" * 40)

while True:
    entrada = input("\nIngrese n° de producto (0 para pagar): ").strip()
    
    # 1. Validación de vacíos
    if not entrada:
        print("⚠ Error: Debes ingresar un número.")
        continue

    # 2. Validación numérica (isdigit rechaza letras y números negativos)
    if not entrada.isdigit():
        print("⚠ Error: Ingresa solo números enteros positivos.")
        continue

    opcion = int(entrada)

    if opcion == 0:
        break
    
    # 3. Validación de rango (que el producto exista)
    idx = opcion - 1
    if 0 <= idx < len(product_list):
        item = product_list[idx]
        carrito.append(item)
        total_bruto += item['precio']
        print(f"✅ Agregado: {item['nombre']} ({formato_clp(item['precio'])})")
        print(f"   Subtotal actual: {formato_clp(total_bruto)}")
    else:
        print(f"⚠ Error: El producto número {opcion} no existe.")

# Lógica de cálculo final
if len(carrito) > 0:
    descuento = 0
    monto_descontable = 0
    
    # Umbral de promoción
    if total_bruto > 100000:
        for prod in carrito:
            if prod['sku'] not in excluidos:
                monto_descontable += prod['precio']
        
        descuento = int(monto_descontable * 0.10) # int para evitar decimales en CLP

    total_final = total_bruto - descuento

    print(f"\n{' BOLETA ELECTRÓNICA ':^30}")
    print("=" * 30)
    print(f"Total Bruto:       {formato_clp(total_bruto):>10}")
    
    if descuento > 0:
        print(f"Descuento (10%):  -{formato_clp(descuento):>10}")
        print(f"(Aplica sobre: {formato_clp(monto_descontable)})")
    else:
        print(f"Descuento:         {formato_clp(0):>10}")
        if total_bruto <= 100000:
            falta = 100001 - total_bruto
            print(f"Info: Agrega {formato_clp(falta)} más para 10% dcto.")

    print("-" * 30)
    print(f"TOTAL A PAGAR:     {formato_clp(total_final):>10}")
    print("=" * 30)
else:
    print("\nCarrito vacío. Gracias por su visita.")