# --- 1. CONFIGURACIÓN DE DATOS ---
product_list = [
    {"sku": "P1001", "nombre": "Audífonos Bluetooth", "precio": 24990},
    {"sku": "P1002", "nombre": "Teclado Mecánico", "precio": 44990},
    {"sku": "P1003", "nombre": "Mouse Gamer", "precio": 19990},
    {"sku": "P1004", "nombre": "Lámpara LED", "precio": 15990},
    {"sku": "P1005", "nombre": "Cargador Inalámbrico", "precio": 22990},
    {"sku": "P1006", "nombre": "Soporte Notebook", "precio": 17990},
    {"sku": "P1007", "nombre": "Parlante Portátil", "precio": 29990},
    {"sku": "P1008", "nombre": "Cámara Web HD", "precio": 30990},
    {"sku": "P1009", "nombre": "Disco Externo 500GB", "precio": 49990},
    {"sku": "P1010", "nombre": "Kit Limpieza", "precio": 10990},
]

# SKUs que NO permiten aplicar descuento
excluidos = ["P1010", "P1007", "P1003"]
carrito = []
total_bruto = 0

# --- 2. MOSTRAR CATÁLOGO Y COMPRA ---
print(f"\n{' CATÁLOGO E-COMMERCE ':*^50}")

for i, item in enumerate(product_list):
    precio_str = f"${item['precio']:,.0f}".replace(",", ".")
    marca = " [OFERTA]" if item['sku'] in excluidos else ""
    print(f"{i + 1}. {item['nombre']:<25} | {precio_str}{marca}")

print("-" * 50)

while True:
    entrada = input("\nIngrese n° de producto (0 para finalizar): ").strip()
    
    if not entrada:
        print("⚠ Error: Ingresa un número.")
        continue

    if not entrada.isdigit():
        print("⚠ Error: Solo números enteros positivos.")
        continue

    opcion = int(entrada)

    if opcion == 0:
        break
    
    idx = opcion - 1
    if 0 <= idx < len(product_list):
        item = product_list[idx]
        carrito.append(item)
        total_bruto += item['precio']
        print(f"✅ Agregado: {item['nombre']}")
    else:
        print(f"⚠ Error: El producto {opcion} no existe.")

# --- 3. REGISTRO DE USUARIO CON VALIDACIÓN ESTRICTA ---
if len(carrito) > 0:
    print(f"\n{' DATOS DE ENVÍO ':*^50}")
    
    # 3.1 VALIDACIÓN DE CORREO
    # Definimos qué caracteres son aceptables en un correo estándar
    caracteres_validos_email = "abcdefghijklmnopqrstuvwxyz0123456789@._-"
    correo_final = ""
    
    while True:
        entrada_correo = input("Ingresa tu correo: ").strip() # Quitamos espacios inicio/fin
        
        # Validación A: Espacios intermedios
        if " " in entrada_correo:
            print("❌ Error: El correo no puede contener espacios.")
            continue
            
        # Validación B: Estructura mínima
        if "@" not in entrada_correo or "." not in entrada_correo:
            print("❌ Error: Falta '@' o el punto '.'")
            continue
            
        # Validación C: Caracteres extraños (Loop de verificación)
        es_valido = True
        for letra in entrada_correo.lower():
            if letra not in caracteres_validos_email:
                es_valido = False
                print(f"❌ Error: Carácter inválido detectado ('{letra}')")
                break # Rompe el for, no el while
        
        if es_valido:
            correo_final = entrada_correo.lower()
            break # Correo aceptado

    # 3.2 VALIDACIÓN DE TELÉFONO
    # Permitimos entrada sucia con + - y espacios, pero NO letras ni símbolos raros ($ % &)
    caracteres_validos_fono = "0123456789+- "
    fono_final = ""
    
    while True:
        entrada_fono = input("Ingresa tu teléfono (+569...): ")
        
        # Validación A: Que no escriban letras ni símbolos raros
        tiene_raros = False
        for char in entrada_fono:
            if char not in caracteres_validos_fono:
                tiene_raros = True
                print(f"❌ Error: Carácter extraño detectado ('{char}'). Solo números, +, - y espacios.")
                break
        
        if tiene_raros:
            continue # Vuelve a pedir el número

        # Limpieza manual (Solo dejamos números para validar largo)
        limpio = entrada_fono.replace(" ", "").replace("+", "").replace("-", "")
        
        # Validación B: Longitud y formato Chile
        if limpio.isdigit():
            if len(limpio) == 9: # Ej: 911223344
                fono_final = "56" + limpio
                break
            elif len(limpio) == 11 and limpio.startswith("56"): # Ej: 56911223344
                fono_final = limpio
                break
            else:
                print("❌ Error: Longitud incorrecta. Debe ser celular (9 dígitos) o formato completo (11 dígitos).")
        else:
            # Esta parte teóricamente no se alcanza por la Validación A, pero es seguridad extra
            print("❌ Error: El número resultante no es válido.")

    # --- 4. CÁLCULO Y BOLETA ---
    descuento = 0
    monto_descontable = 0
    
    if total_bruto > 100000:
        for prod in carrito:
            if prod['sku'] not in excluidos:
                monto_descontable += prod['precio']
        descuento = int(monto_descontable * 0.10)

    total_pagar = total_bruto - descuento

    # IMPRESIÓN FINAL
    print(f"\n{' BOLETA ELECTRÓNICA ':^40}")
    print("=" * 40)
    print(f"Cliente:   {correo_final}")
    print(f"Teléfono:  +{fono_final}")
    print("-" * 40)
    
    for prod in carrito:
        p_str = f"${prod['precio']:,.0f}".replace(",", ".")
        mark = "*" if prod['sku'] in excluidos else ""
        print(f"- {prod['nombre']:<25} {p_str}{mark}")
        
    print("-" * 40)
    bruto_fmt = f"${total_bruto:,.0f}".replace(",", ".")
    dcto_fmt = f"-${descuento:,.0f}".replace(",", ".")
    final_fmt = f"${total_pagar:,.0f}".replace(",", ".")
    
    print(f"Total Bruto:       {bruto_fmt:>12}")
    print(f"Descuento (10%):   {dcto_fmt:>12}")
    print("-" * 40)
    print(f"TOTAL A PAGAR:     {final_fmt:>12}")
    print("=" * 40)
    
else:
    print("\nCarrito vacío. No se registraron datos.")