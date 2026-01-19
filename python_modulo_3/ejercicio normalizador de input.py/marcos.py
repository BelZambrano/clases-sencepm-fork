datos = []

while True:
    celular = input("Ingrese el número de su celular: (Ejemplo: 912345678)").strip()

    if not celular.isdigit():
        print("Error: el celular debe contener solo números.")
        continue

    if len(celular) == 8:
        celular = "569" + celular
    elif len(celular) == 9 and celular.startswith("9"):
        celular = "56" + celular
    elif len(celular) == 11 and celular.startswith("569"):
        pass
    else:
        print("Error: formato de celular inválido.")
        continue

    break

while True:
    correo = input("Ingrese su correo electrónico: (Ejemplo: ejemplo@correo.cl)").strip()

   # validacion de correo   
    if (
            "@" in correo
            and correo.count("@") == 1
            and "." in correo.split("@")[1]
            and not correo.startswith("@")
            and not correo.endswith(".")
        ):
            break
    else:
        print("Error: correo inválido. Ejemplo: ejemplo@correo.cl")

registro = {
    "celular": celular,
    "correo": correo
}

datos.append(registro)

print("DATOS GUARDADOS")
for d in datos:
    print("Celular:", d["celular"], "| Correo:", d["correo"])