total_final = 0  
carrito = []     

print("\n" + "="*50)
print("Compra Realizada")
print("="*50)

print("\n Para enviar confirmación de compra:")
correo = input("Ingresa tu correo (ejemplo: usuario@dominio.cl): ").strip()
while "@" not in correo or len(correo) < 5:
    print("Correo inválido - debe tener @")
    correo = input("Ingresa tu correo: ").strip()

telefono = input("Ingresa tu número (+569xxxxxxxx): ").strip()
while not telefono.startswith("+569") or len(telefono) != 12:
    print("Teléfono inválido - debe ser +569xxxxxxxx (12 dígitos)")
    telefono = input("Ingresa tu número (+569xxxxxxxx): ").strip()

print("\nDatos confirmados:")
print("-" * 30)
print(f"Correo: {correo}")
print(f"Teléfono: {telefono}")
print(f"Total: ${total_final:,.0f}")
print(f"Items: {len(carrito)} productos")

print("\nEnviando...")
contador = 0
while contador < 3:
    print(f" {contador+1}/3")
    contador += 1

print("Confirmación enviada")
print("Gracias por tu compra")