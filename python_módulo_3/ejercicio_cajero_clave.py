## Belen
#clave_correcta = 1234
#intentos = 0
#
#while intentos < 3:
#    clave = int(input("Ingrese su contraseña de 4 dígitos: "))
#
#    if clave != clave_correcta:
#        intentos = intentos + 1 # intentos += 1
#
#        if intentos < 3:
#            print("Contraseña incorrecta.")
#            print("Advertencia: al tercer intento su clave será bloqueada.")
#        else:
#            print("Tarjeta bloqueada. Ha superado el número de intentos.")
#    else:
#        print("Contraseña correcta. Bienvenido a BancodelPatito.")
#        break
#
#
#Miguel
VALOR_BILLETE = 5000
CLAVE_SECRETA = "1234"
intentos = 0
acceso_concedido = False

while intentos < 3:
    clave = input("Ingrese su clave: ")
    if clave == CLAVE_SECRETA:
        acceso_concedido = True
        break
    
    intentos += 1
    if intentos < 3:
        print(f"Clave incorrecta. Quedan {3 - intentos} intentos.")

if not acceso_concedido:
    print("Ha excedido el número de intentos. Operación cancelada.")
else:
    print("acceso consedido")

##Javier
#print("Bienvenido")
#print("Inserte su tarjeta... (Presione Enter para continuar)")
#input()
#
#pin_correcto = 1234
#intentos_max = 3
#intentos = 0
#acceso = False
#
#while intentos < intentos_max:
#    pin = int(input("Ingrese su PIN de 4 dígitos: "))
#    
#    if pin == pin_correcto:
#        print("\nPIN correcto Acceso autorizado.")
#        print("Continúe con la operación de retiro...")
#        acceso = True
#        break
#    else:
#        intentos += 1
#        restantes = intentos_max - intentos
#        print(f"PIN incorrecto Intentos restantes: {restantes}")
#
#if not acceso:
#    print("\n¡Acceso bloqueado! Demasiados intentos fallidos.")
#    print("Retire su tarjeta.")
#

#Marcos
#user = "adm"
#password = "1234"
#
#intentos = 3
#
#while intentos > 0:
#    #usuario = input("Ingrese su usuario: ")
#    clave = input("Ingrese su clave: ")
#
#    #if usuario == user and clave == password:
#    if clave == password:
#        print("Inicio de sesión exitoso")
#        break
#    else:
#        intentos -= 1
#        #print("Usuario o clave incorrectos")
#        print("Clave incorrectos")
#        print("Intentos restantes:", intentos)
#
#if intentos == 0:
#    print("Cuenta bloqueada. Demasiados intentos fallidos")
#

#David
#pin_banco = "1234"
#intentos = 0
#tarjeta_bloqueada = True
#
#print("BIENVENIDO A SU BANCO")
#
#while intentos < 3:
#    pin_ingresado = input("Ingrese su PIN de 4 digitos: ")
#
#    if pin_ingresado == pin_banco:
#        tarjeta_bloqueada = False
#        break
#    
#    intentos += 1
#    print("PIN incorrecto.")
#
#if tarjeta_bloqueada:
#    print("Ha excedido el limite de intentos. Su tarjeta ha sido retenida.")
#else:
#    print("Acceso autorizado. Seleccione una operacion.")

#Hector
#contraseña_almacenada = 12345
#intentos = 3
#
#while intentos > 0:
#    contraseña_ingresada = input("Ingrese su contraseña: ")
#    if contraseña_ingresada == "":
#        print("la contraseña no puede estar vacío")
#        continue
#    if not contraseña_ingresada.isdigit():
#        print("La contraseña debe contener solo números")
#        continue
#
#    contraseña_ingresada = int(contraseña_ingresada)
#
#    if contraseña_ingresada == contraseña_almacenada:
#        print("Contraseña correcta, bienvenido a tu cuenta")
#        print("Tu saldo es 0000")
#        break
#    else:
#        intentos -= 1
#        print("Contraseña incorrecta, te quedan menos intentos")
#if intentos == 0:
#    print("Demasiados intentos, intente de nuevo más tarde")
#

##Carla
#
#pin_correcto = "0101"
#intentos = 0
#while intentos < 3:
#    print("Ingrese su pin para acceder a su cuenta:")
#    pin = input().strip()
#
#    if pin != pin_correcto:
#        intentos += 1
#        if intentos < 3:
#            print("Pin incorrecto, por favor intente de nuevo.")
#        else:
#            print("Pin incorrecto, intentos máximos alcanzados.")
#    else:
#        print("Ingreso correcto.")
#        break


##Mauricio
#PIN_CORRECTO = "1234"  # Cambia este valor si quieres otro PIN
#intentos_restantes = 3
#
#while intentos_restantes > 0:
#    pin = input("Ingrese su PIN de 4 dígitos: ").strip()
#    if pin == PIN_CORRECTO:
#        print("PIN correcto. Acceso concedido. ✅")
#        # Continuar con el flujo del cajero...
#        print("Continuando con las operaciones...")
#        break
#    else:
#        intentos_restantes -= 1
#        if intentos_restantes == 0:
#            print("Ha agotado los 3 intentos. Saliendo del flujo. 🚫")
#        else:
#            print(f"PIN incorrecto. Intentos restantes: {intentos_restantes}"

#cristian

#t("Ingrese su tarjeta por favor...")
#
# = 1234
#ntos = 0
#
#e Intentos < 3:
#Clave = int(input("ingrese su clave: "))
#
#if Clave != Pass:
#    Intentos = Intentos +1
#    print("Al tercer error se bloqueara su tarjeta")
#
#    if Intentos < 3:
#        print("contaseña incorrecta, intentelo otra vez")
#
#    else:
#         print("su tarjeta fue bloqueda por superar el numero de intentos permitidos")
#   
#else:
#    print("Bienvenido a su banco")
#break