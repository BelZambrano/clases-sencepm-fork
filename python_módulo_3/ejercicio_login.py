##Mauricio
#usuarios = {
#    "ana": "1234",
#    "juan": "abcd",
#    "luis": "pass"
#}
#
#while True:
#    user = input("Usuario: ").strip()
#    pwd = input("Contraseña: ").strip()
#
#    if user in usuarios and usuarios[user] == pwd:
#        print("Acceso concedido ✅")
#        break
#    else:
#        print("Usuario o contraseña inválidos. Intenta de nuevo.")
#
#
##Javier
#usuarios = {
#    'admin': 'admin123',
#    'usuario1': 'pass1',
#    'usuario2': 'pass2'
#}
#
#
#limite_intentos = 3  
#intentos = 0
#
#while True:
#    username = input("Ingrese usuario: ").strip()
#    password = input("Ingrese contraseña: ").strip()
#    
#    if username in usuarios and usuarios[username] == password:
#        print("¡Acceso permitido! Bienvenido.")
#        break  
#    
#    intentos += 1
#    print("Credenciales inválidas. Intente de nuevo.")
#    
#    if limite_intentos is not None and intentos >= limite_intentos:
#        print("Intentos agotados. Acceso denegado.")
#        break
#
#print("Fin del programa.")
#
#
##Hector
#
#usuarios = {"correo1@gmail.com": "clave1", "correo2@gmail.com": "clave2", "correo3@gmail.com": "clave3"}
#intentos = 3
#
#while intentos > 0 :
#    ingreso_correo = input("correo: ")
#    ingreso_clave = input("Contraseña: ")
#
#    if usuarios.get(ingreso_correo) == ingreso_clave:
#        print("Acceso permitido")
#        break
#
#    intentos -= 1
#    print("Datos incorrectos")
#
#if intentos == 0:
#    print("Demasiados intentos")
#
##Miguel
#usuarios_db = {
#    "admin@correo.com": "1234",
#    "juan.perez@correo.com": "python2026",
#    "maria.g@correo.com": "claveSegura!"
#}
#
#intentos_restantes = 3
#
#print("--- Sistema de Acceso ---")
#
#while intentos_restantes > 0:
#    usuario = input("\nIngrese su correo electrónico: ")
#    password = input("Ingrese su contraseña: ")
#
#    if usuarios_db.get(usuario) == password:
#        print(f"\n✅ Acceso concedido. ¡Bienvenido, {usuario}!")
#        break
#    
#    intentos_restantes -= 1
#    if intentos_restantes > 0:
#        print(f"❌ Credenciales incorrectas. Te quedan {intentos_restantes} intentos.")
#    else:
#        print("🚫 Has agotado tus intentos. Acceso bloqueado.")
#
##Carla
#
#usuarios = {
#    "ana@email.com":"Contraseña123.",
#    "juam@gmail.com":"Contraseña456.",
#    "maria@gmail.com":"Contraseña987."
#}
#
#intentos = 0
#max_intentos = 3
#
#while intentos < max_intentos:
#    correo = input("Ingrese su correo electrónico: ").strip()
#    contrasenia = input("Ingrese su contraseña: ")
#    if (correo not in usuarios) or (usuarios[correo]) != contrasenia:
#        intentos += 1
#        if intentos < max_intentos:
#            print("Correo o contraseña incorrectos. Por favor intente de nuevo, recuerde que tiene 3 intentos.")
#        else:
#            print("Acceso bloqueado. Demasiados intentos, intente de nuevo dentro de 5 minutos.")
#    else:
#        print("Acceso permitido.")
#        break
#
##Belen
#usuarios = {
#    "pepa": 1234,
#    "pipo": 4321,
#    "lala": 1111
#}
#
#intentos = 0
#max_intentos = 3
#
#while intentos < max_intentos:
#    usuario = input("Ingrese su usuario: ")
#    clave = int(input("Ingrese su contraseña: "))
#
#    if usuario in usuarios and usuarios[usuario] == clave:
#        print("Acceso permitido. Bienvenido", usuario)
#        break
#    else:
#        intentos = intentos + 1
#        intentos_restantes = max_intentos - intentos
#
#        if intentos_restantes > 0:
#            print("Usuario o contraseña incorrectos.")
#            print("Intentos restantes:", intentos_restantes)
#        else:
#            print("Acceso bloqueado. Ha superado el número de intentos.")
#
##Marcos
#
#usuarios = {
#    "juan@gmail.com": "1234",
#    "ana@gmail.com": "abcd",
#    "carlos@gmail.com": "asd123"
#}
#
#intentos = 3
#
#while intentos > 0:
#    correo = input("Ingrese su correo: ")
#    clave = input("Ingrese su contraseña: ")
#
#    encontrado = False
#    
#    for usuario in usuarios:
#        #print(usuario)
#        if correo == usuario:
#            encontrado = True
#            
#            if clave == usuarios[usuario]:
#                print("Login correcto. Bienvenido.")
#                intentos = 0
#            else:
#                print("Contraseña incorrecta.")
#            break
#    
#    if encontrado == False:
#        print("Correo no registrado.")
#    
#    if intentos > 0:
#        intentos -= 1
#        print("Intentos restantes:", intentos)
#
#print("Fin del programa.")
#
#
##Cristian
#
#usuarios = {
#   "cristian.tc661@gmail.com": "12345",
#   "esteban@gmail.com" : "6789",
#   "alan.brito@gmail.com" : "13579"   
#}
#
#max_intentos = 3
#intentos = 0 
#
#while intentos < max_intentos:
#    usuario = input("Ingrese su usuario: ")
#    clave = input("ingrese su clave: ")
#
#    if usuario in usuarios:
#        if usuarios [usuario] == clave:
#            print("Acceso correcto, bienvenido: ", usuario)
#            break
#        else:
#            print("Contraseña incorrecta!!")
#
#    else:
#        print("Usuario no existe!") 
#
#    intentos += 1
#    
#    print(f"Lleva {intentos} de un maximo de  {max_intentos} intentos")  
#
#if  intentos == max_intentos:
#    print ("Acceso bloqueado, supero el maximo de intentos")
#

usuarios = [
    {"correo": "micorreo@gmail.com", "clave": 1234},
    {"correo": "tucorreo@gmail.com", "clave": 1235},
    {"correo": "sucorreo@gmail.com", "clave": 1236}
]


max_intentos = 3
intentos = 0
acceso_ok = False

while intentos < max_intentos and not acceso_ok:
    correo = input("ingresa correo: ")
    clave = input("Tu clave: ")

    for u in usuarios:
        if u["correo"] == correo and u["clave"] == clave:
            acceso_ok = True
            break
    
    if not acceso_ok:
        intentos += 1
        print("Datos incorrectos")

if acceso_ok:
    print("Hola")
else:
    print("bloqueado ya cumpliste los 3 intentos")


