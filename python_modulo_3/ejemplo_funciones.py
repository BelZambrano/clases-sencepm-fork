def normalizar(texto):
    return texto.strip().lower()

def perecio_pan(kg, tipo):
#                5  Marraqueta

    tipo = normalizar(tipo)
    #  Marraqueta = normalizar(  Marraqueta)


    print("marraqueta")
    if tipo == "hallulla":
    # marraqueta
        return 2000 * kg
    elif tipo == "amasado":
        return 2500 * kg
    
    elif tipo == "marraqueta":
        return 2100 * kg
    
    else:
        return None
    
kilos = 5
tipo_pan = "    Hallulla"


print(perecio_pan(5, "      Marraqueta"))