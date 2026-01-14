productos = []

cantidad = input("¿Cuántos productos quieres ingresar? ")

if cantidad == "0":
    print("No se ingresan productos.")

elif cantidad == "1":
    sku = input("SKU: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    productos.append({"sku": sku, "nombre": nombre, "precio": precio})
    print("Producto agregado.")

elif cantidad == "2":
    sku1 = input("SKU producto 1: ")
    nombre1 = input("Nombre producto 1: ")
    precio1 = float(input("Precio producto 1: "))
    productos.append({"sku": sku1, "nombre": nombre1, "precio": precio1})

    sku2 = input("SKU producto 2: ")
    nombre2 = input("Nombre producto 2: ")
    precio2 = float(input("Precio producto 2: "))
    productos.append({"sku": sku2, "nombre": nombre2, "precio": precio2})
    print("Dos productos agregados.")

elif cantidad == "3":

    sku1 = input("SKU 1: ")
    nombre1 = input("Nombre 1: ")
    precio1 = float(input("Precio 1: "))
    productos.append({"sku": sku1, "nombre": nombre1, "precio": precio1})

    sku2 = input("SKU 2: ")
    nombre2 = input("Nombre 2: ")
    precio2 = float(input("Precio 2: "))
    productos.append({"sku": sku2, "nombre": nombre2, "precio": precio2})

    sku3 = input("SKU 3: ")
    nombre3 = input("Nombre 3: ")
    precio3 = float(input("Precio 3: "))
    productos.append({"sku": sku3, "nombre": nombre3, "precio": precio3})
    print("Tres productos agregados.")

else:
    print("Ingresa solo 0, 1, 2 o 3.")


print("\nBASE DE DATOS INGRESADA:")
print("SKU | Nombre | Precio")
print("-" * 25)

if len(productos) > 0:
    print(f"{productos[0]['sku']} | {productos[0]['nombre']} | ${productos[0]['precio']:.0f}")
if len(productos) > 1:
    print(f"{productos[1]['sku']} | {productos[1]['nombre']} | ${productos[1]['precio']:.0f}")
if len(productos) > 2:
    print(f"{productos[2]['sku']} | {productos[2]['nombre']} | ${productos[2]['precio']:.0f}") 