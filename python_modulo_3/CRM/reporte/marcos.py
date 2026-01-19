clients = [
    {"id": 1, "nombre_completo": "Ana Torres", "correo": "ana.torres@correo.com", "telefono": "+56 9 42351234", "estado": "Cliente potencial"},
    {"id": 2, "nombre_completo": "Luis Ramírez", "correo": "luis.ramirez@correo.com", "telefono": "+56 9 93481234", "estado": "Alto interés"},
    {"id": 3, "nombre_completo": "Claudia Soto", "correo": "claudia.soto@correo.com", "telefono": "+56 9 78123456", "estado": "Cliente efectivo"},
    {"id": 4, "nombre_completo": "Jorge Fuentes", "correo": "jorge.fuentes@correo.com", "telefono": "+56 9 63547812", "estado": "En proceso de compra"},
    {"id": 5, "nombre_completo": "Marta Herrera", "correo": "marta.herrera@correo.com", "telefono": "+56 9 98124578", "estado": "Super cliente"},
    {"id": 6, "nombre_completo": "Carlos Díaz", "correo": "carlos.diaz@correo.com", "telefono": "+56 9 71234598", "estado": "Alto interés"},
    {"id": 7, "nombre_completo": "Francisca Rojas", "correo": "francisca.rojas@correo.com", "telefono": "+56 9 91234871", "estado": "Cliente efectivo"},
    {"id": 8, "nombre_completo": "Pedro Gutiérrez", "correo": "pedro.gutierrez@correo.com", "telefono": "+56 9 84567213", "estado": "Cliente potencial"},
    {"id": 9, "nombre_completo": "Valentina Bravo", "correo": "valentina.bravo@correo.com", "telefono": "+56 9 78341236", "estado": "Super cliente"},
    {"id": 10, "nombre_completo": "Diego Castro", "correo": "diego.castro@correo.com", "telefono": "+56 9 93456781", "estado": "En proceso de compra"},
    {"id": 11, "nombre_completo": "Camila Paredes", "correo": "camila.paredes@correo.com", "telefono": "+56 9 91234578", "estado": "Cliente potencial"},
    {"id": 12, "nombre_completo": "Andrés Molina", "correo": "andres.molina@correo.com", "telefono": "+56 9 89451236", "estado": "Cliente efectivo"},
    {"id": 13, "nombre_completo": "Patricia Silva", "correo": "patricia.silva@correo.com", "telefono": "+56 9 74382910", "estado": "Alto interés"},
    {"id": 14, "nombre_completo": "Matías Reyes", "correo": "matias.reyes@correo.com", "telefono": "+56 9 87234561", "estado": "En proceso de compra"},
    {"id": 15, "nombre_completo": "Isidora Méndez", "correo": "isidora.mendez@correo.com", "telefono": "+56 9 98127345", "estado": "Super cliente"},
    {"id": 16, "nombre_completo": "Sebastián Núñez", "correo": "sebastian.nunez@correo.com", "telefono": "+56 9 65432178", "estado": "Cliente efectivo"},
    {"id": 17, "nombre_completo": "Fernanda Loyola", "correo": "fernanda.loyola@correo.com", "telefono": "+56 9 72345681", "estado": "Alto interés"},
    {"id": 18, "nombre_completo": "Tomás Aravena", "correo": "tomas.aravena@correo.com", "telefono": "+56 9 83451234", "estado": "Cliente potencial"},
    {"id": 19, "nombre_completo": "Josefa Espinoza", "correo": "josefa.espinoza@correo.com", "telefono": "+56 9 96432187", "estado": "Cliente efectivo"},
    {"id": 20, "nombre_completo": "Ricardo Vergara", "correo": "ricardo.vergara@correo.com", "telefono": "+56 9 78912345", "estado": "Super cliente"}
]

opcion = ""

# Preguntar hasta que el usuario ingrese una opción válida
while opcion != "s" and opcion != "n":
    opcion = input("¿Desea generar el reporte de clientes? (s/n): ").lower()

    if opcion == "s":

        # Obtengo el TOTAL de personas
        total_personas = len(clients)

        # Inicializo los CONTADORES
        potenciales = 0
        alto_interes = 0
        proceso_compra = 0
        clientes_efectivos = 0
        super_clientes = 0

        # Recorro la base de datos y cuento cada estado
        for cliente in clients:
            if cliente["estado"] == "Cliente potencial":
                potenciales += 1
            elif cliente["estado"] == "Alto interés":
                alto_interes += 1
            elif cliente["estado"] == "En proceso de compra":
                proceso_compra += 1
            elif cliente["estado"] == "Cliente efectivo":
                clientes_efectivos += 1
            elif cliente["estado"] == "Super cliente":
                super_clientes += 1

        # Calculo los porcentajes
        porc_potenciales = (potenciales * 100) / total_personas
        porc_alto_interes = (alto_interes * 100) / total_personas
        porc_proceso_compra = (proceso_compra * 100) / total_personas
        porc_clientes_efectivos = (clientes_efectivos * 100) / total_personas
        porc_super_clientes = (super_clientes * 100) / total_personas

        # Genero e imprimo el REPORTE
        print("\n===== REPORTE DE CLIENTES =====")
        print("a) Número total de personas:", total_personas)
        print("b) Clientes potenciales:", potenciales, "-", round(porc_potenciales, 2), "%")
        print("c) Personas con alto interés:", alto_interes, "-", round(porc_alto_interes, 2), "%")
        print("d) Personas en proceso de compra:", proceso_compra, "-", round(porc_proceso_compra, 2), "%")
        print("e) Clientes efectivos:", clientes_efectivos, "-", round(porc_clientes_efectivos, 2), "%")
        print("f) Super clientes:", super_clientes, "-", round(porc_super_clientes, 2), "%")

    elif opcion == "n":
        print("Reporte no generado. Programa finalizado.")

    else:
        print("Opción no válida. Debe ingresar 's' o 'n'.\n")