
# Crear un archivo .py
# crear 2 variable a y b 
# Asignar un valor a y b por el usuario
# sumar a + b
# mostrar en pantall el resultado de a + b 

a = None
b = None


a = input("Asigna el valor de a:")
b = input("Asigna el valor de b:")

print("el tipo de dato de 'a' es: ",type(a))

print("el tipo de dato de 'b' es: ",type(b))

resultado = a + b
print(resultado)


#Forzar tipo de dato

a = int(input("Asigna el valor de a:"))
b = int(input("Asigna el valor de b:"))

print("el tipo de dato de 'a' es: ",type(a))

print("el tipo de dato de 'b' es: ",type(b))

resultado = str(a + b)
print(resultado)
print("el tipo de dato del resultado esta forzado y ahora es: ", type(resultado))

resultado = float(a + b)

print(resultado)
print("el tipo de dato del resultado esta forzado y ahora es: ", type(resultado))