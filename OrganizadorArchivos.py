'''
Objetivo: Desarrollar un script que organice los archivos en subdirectorios según su tipo. Utiliza las librerías OS, shutil y json.
Pasos:
El programa debe listar los archivos en el directorio actual.
Debe mover los archivos a carpetas específicas según su extensión (.txt → Textos, .jpg → Imágenes, .csv → Datos).
Si la carpeta correspondiente no existe, debe crearla antes de mover los archivos
Debe generar un fichero log.txt registrando cada archivo movido.
Maneja errores si un archivo ya existe en la carpeta destino o si ocurre un problema de permisos.
'''
import os
import shutil
import json
salir=False

def mostrar_archivos():
    print("Archivos en el directorio actual:")
    print(os.listdir("."))

configJson={".txt":"Textos", ".jpg":"Imágenes", ".csv":"Datos"}
with open("config.json", "w") as archivo:
    json.dump(configJson, archivo)

with open("config.json", "r") as archivoJson:
    config=json.load(archivoJson)

def organizar_archivos():
    
    for archivo in os.listdir("."):
        if os.path.isfile(archivo) and archivo != "log.txt" and archivo != "config.json":
            for ext, carpeta in config.items():
                if archivo.endswith(ext):
                    if not os.path.exists(carpeta):
                        os.mkdir(carpeta)
                    try:
                        shutil.move(archivo,carpeta)
                        with open("log.txt", "a") as archivoLog:
                            archivoLog.write(f"Movido {archivo} a {carpeta}\n")
                    except FileExistsError:
                        print("El nombre del archivo ya existe en la carpeta")
                    except PermissionError:
                        print("El archivo está en uso o falta privilegios del administrador.")
      

opciones_menu=["MOSTRAR ARCHIVOS", "ORGANIZAR ARCHIVOS", "SALIR"]

def menu():
    print("MENÚ PRINCIPAL")
    print("********************************")
    for clave, valor in enumerate(opciones_menu,1):
        print(f"Pulsa {clave}: {valor}")
    print("********************************")

while not salir:
    menu()
    opciones=int(input("Indica una opción: "))
    match opciones:
        case 1:
            print(f"Has elegido: {opciones_menu[opciones-1]}")
            mostrar_archivos()
        case 2:
            print(f"Has elegido: {opciones_menu[opciones-1]}")
            organizar_archivos()
        case 3:
            print(f"Has elegido: {opciones_menu[opciones-1]}")
            salir=True
            print("Has salido del programa.")
        case __:
            print("Opción incorrecta, pulsa del 1 al 3.")
