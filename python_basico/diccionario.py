diccionario = {
    "clave": "valor",
    "otra clave": 23,
    "una clave más": "otro valor"
}

persona = {
    "nombre": "Apolo",
    "edad": 5000,
    "correo": None,
}

print("Acá imprimo todo el diccionario persona: ", persona)
print("Acá solo estoy imprimiento el valor de la clave 'nombre' para el diccionario 'persona'", persona["nombre"])

correo = persona["correo"]
print(correo)

persona["correo"] = "soyapolo@olimpo.com"
correo = persona["correo"]
print(correo)

persona["ubicación"] = "olimpo"

print(persona)
print(type(persona))