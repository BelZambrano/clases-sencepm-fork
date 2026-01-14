cantidad = int(input("¿Cuántos productos quieres ingresar? "))
base_de_datos = []

for i in range(cantidad):
    print(f"\nDatos del producto {i + 1}:")
    sku = input("SKU: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    
    producto = {
        "sku": sku,
        "nombre": nombre,
        "precio": precio
    }
    
    base_de_datos.append(producto)

print("\n--- Base de Datos Final ---")
print(base_de_datos)