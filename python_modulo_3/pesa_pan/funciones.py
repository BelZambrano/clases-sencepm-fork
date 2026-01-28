def normalizar(texto):
    return texto.strip().lower()

def precio_pan(kg, tipo):
    tipo = normalizar(tipo)

    if tipo == "hallulla":
        return 2000 * kg
    elif tipo == "amasado":
        return 2500 * kg
    elif tipo == "marraqueta":
        return 2100 * kg
    else:
        return None
    
