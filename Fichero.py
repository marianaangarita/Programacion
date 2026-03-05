'''
Objetivo: Desarrollar un programa que registre accesos a un sistema en un fichero de logs y luego analice el historial.
Pasos:
Crea un fichero llamado accesos.log si no existe.
Cada vez que el programa se ejecute, debe pedir al usuario su nombre y registrar la fecha y hora del acceso en el fichero en formato:
[2025-02-05 14:30:00] Usuario: Juan
Implementa una opción para listar todos los accesos registrados (Mejora: solo muestra los usuarios únicos).
Implementa una opción para mostrar cuántas veces ha accedido cada usuario.
Implementa una opción para copiar el fichero de acceso.log en otro cuyo nombre escriba el usuario.
'''
from datetime import datetime
now = datetime.now()
formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")

salir=False
opciones_menu=["VER USUARIOS", "VECES QUE A ACCEDIDO EL USUARIO", "COPIAR FICHERO", "SALIR"]
def menu():
    print("MENÚ PRINCIPAL")
    print("**********************************")
    for clave, valor in enumerate(1,opciones_menu):
        print(f"Pulsa {clave}:{valor}")
    print("**********************************")

while not salir:
    nombre=input("Indica tu nombre: ").capitalize()

    with open("accesos.log", "a") as archivo:
        archivo.write(f"{formatted} Usuario: {nombre}\n")
        archivo.close()
    menu()

    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
        case 2:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
        case 3:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
        case 4:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción Incorrecta")

