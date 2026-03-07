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
import shutil
import os
from datetime import datetime

salir=False
opciones_menu=["VER USUARIOS", "VECES QUE A ACCEDIDO EL USUARIO", "COPIAR FICHERO", "SALIR"]
def menu():
    print("MENÚ PRINCIPAL")
    print("**********************************")
    for clave, valor in enumerate(opciones_menu,1):
        print(f"Pulsa {clave}: {valor}")
    print("**********************************")

def usuarios():
    with open ("accesos.log", "r") as archivo:
        for linea in archivo:
            partes=linea.split("Usuario: ")
            print(f"{partes[1].strip()}")

def registros():
    conteo_archivo={}
    with open ("accesos.log", "r") as archivo:
        for linea in archivo:
            partes=linea.split("Usuario: ")
            usuario=partes[1].strip()
            if not usuario in conteo_archivo:
                    conteo_archivo[usuario]=1
            else:
                    conteo_archivo[usuario]+=1
        return conteo_archivo

while not salir:
    nombre=input("Indica tu nombre: ").capitalize()

    with open("accesos.log", "a") as archivo:
        now = datetime.now()
        formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
        archivo.write(f"{formatted} Usuario: {nombre}\n")

    menu()

    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            usuarios()
        case 2:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            print(registros())
        case 3:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            nombre_archivo=input("Indica el nuevo nombre del archivo: ").lower()
            if not os.path.exists("proyecto"):
                os.mkdir("proyecto")
            shutil.copy("accesos.log",f"proyecto/{nombre_archivo}.log")
        case 4:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción Incorrecta")


    
