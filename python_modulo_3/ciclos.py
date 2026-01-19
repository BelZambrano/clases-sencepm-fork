estudiantes = ["Juan", "Camilo", "Lucious", "Harry"]

for nombre in estudiantes:
    print("Estudiante: ", nombre)


total = 0

while total < 50:
    entrada = input("ingresa un numero para sumar (total actual =" + str(total) +"):")
    numero = int(entrada)
    total += numero
    continue

print("listo. total final:", total)
