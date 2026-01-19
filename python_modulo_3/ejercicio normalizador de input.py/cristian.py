def validar_correo(correo):
    return "@" in correo and "." in correo

while True:
    correo = input("Ingresa tu correo electrónico: ").strip()
    if validar_correo(correo):
            break
    else:
        print("Correo inválido. Debe contener '@' y '.'")
telefono = input(f"Ingrese su numero de telefono: ").strip()

formato_telefono = f"+56{telefono}"

persona ={
     "correo" : correo,
     "telefono" : formato_telefono
}

print("=== Datos ingresados ===")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")