from funciones import precio_pan


def main():
    tipo = input("Ingresa un tipo de pan (marraqueta / hallulla / amasado)")
    kg = int(input("Cuánto pesa?"))

    total = precio_pan(kg, tipo)
    print(total)

    if total is None:
        print("tipo no válido")
    else:
        print(f"El total a pagar por {kg}kg de {tipo} es ${int(total)}")

if __name__ == "__main__":
    main()