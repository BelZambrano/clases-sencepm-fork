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


while 1:
    print("\n=== Menú ===")
    print("1) Generar reporte")
    print("2) Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        total = len(clients)

        # Inicializar contadores
        c_potencial = 0
        c_alto = 0
        c_proceso = 0
        c_efectivo = 0
        c_super = 0

        # Contar por estado leyendo la clave "estado"
        for cli in clients:
            est = str(cli.get("estado", "")).strip().lower()

            match est:
                case "cliente potencial":
                    c_potencial += 1
                case "alto interés" | "alto interes":
                    c_alto += 1
                case "en proceso de compra":
                    c_proceso += 1
                case "cliente efectivo":
                    c_efectivo += 1
                case "super cliente" | "súper cliente":
                    c_super += 1

        if total == 0:
            p_potencial = p_alto = p_proceso = p_efectivo = p_super = 0.0
        else:
            p_potencial = c_potencial / total * 100
            p_alto = c_alto / total * 100
            p_proceso = c_proceso / total * 100
            p_efectivo = c_efectivo / total * 100
            p_super = c_super / total * 100

        print("\n=== Reporte ===")
        print("Número total de personas en la base de datos:", total)
        print(f"Clientes potenciales: {c_potencial} ({p_potencial:.2f}%)")
        print(f"Alto interés: {c_alto} ({p_alto:.2f}%)")
        print(f"En proceso de compra: {c_proceso} ({p_proceso:.2f}%)")
        print(f"Clientes efectivos: {c_efectivo} ({p_efectivo:.2f}%)")
        print(f"Super cliente: {c_super} ({p_super:.2f}%)")

    elif opcion == "2":
        print("Saliendo... 👋")
        break
    else:
        print("Opción inválida. Intente nuevamente.")