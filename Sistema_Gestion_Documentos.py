import os
import shutil
import json
from datetime import datetime

salir=False
opciones_menu=["ORGANIZAR DOCUMENTOS", "BÚSQUEDA AVANZADA DE ARCHIVOS", "GESTIÖN COPIAS SEGURIDAD"]
def menu():
    print("MENÚ PRINCIPAL")
    print("********************************")
    for clave, valor in enumerate(opciones_menu,1):
        print(f"Pulsa {clave}: {valor}")
    print("********************************")

extension_archivo={".xls":"Facturas",".docx":"Contratos", ".pdf":"Informes", ".txt":"Backups"}

with open("datos.json", "w") as archivo:
    json.dump("extension_archivo","archivo")

with open("datos.json", "r") as archivo:
    datos=json.load(archivo)

def organizar_archivos():
    for archivo in os.listdir("."):
        if os.path.isfile(archivo) and archivo != "log.txt" and archivo != "datos.json":
            for ext, carpeta in datos.items():
                partes=archivo.split(".")
                if partes[len(partes)-1]==ext:
                    if not os.path.exists(carpeta):
                        os.mkdir(carpeta)
                    try:
                        destino= os.path.join(carpeta, archivo)
                        if os.path.exists(destino):
                            print("El archivo ya existe en la carpeta destino")
                            break
                        else:
                            shutil.move(archivo,carpeta)
                            with open("log.txt", "a") as archivoLog:
                                now = datetime.now()
                                formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
                                archivoLog.write(f"{formatted} Movido {archivo} a {carpeta}\n")
                            break
                    except FileExistsError:
                        print("El nombre del archivo ya existe en la carpeta")
                    except PermissionError:
                        print("El archivo está en uso o falta privilegios del administrador.")

            
def busqueda_avanzada():

def copia_seguridad():

def gestion_permisos():
    usuario=input("Indica tu usuario: ").lower()
    contrasena=input("Indica tu contraseña: ")
    with open("base_deDatos.csv", "r") as archivo:
        next(archivo)
        for linea in archivo:
            comprobacion=linea.split(",")
            if comprobacion[0]==usuario and comprobacion[len(comprobacion)-1]==contrasena:
                print("Acceso concedido, tienes permisos de administrador")
                break
            else:
                print("Usuario o contraseña no válidos, vuelve a intentarlo")
                continue
            



