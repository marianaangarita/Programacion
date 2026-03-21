import os
import shutil
import json
from datetime import datetime

salir=False
opciones_menu=["ORGANIZAR DOCUMENTOS", "BÚSQUEDA AVANZADA DE ARCHIVOS", "COPIA DE SEGURIDAD", "RESTAURAR COPIA DE SEGURIDAD","ELIMINAR ARCHIVO", "SALIR"]
def menu():
    print("MENÚ PRINCIPAL")
    print("********************************")
    for clave, valor in enumerate(opciones_menu,1):
        print(f"Pulsa {clave}: {valor}")
    print("********************************")

extension_archivo={"xls":"Facturas","docx":"Contratos", "pdf":"Informes", "txt":"Backups"}

with open("datos.json", "w") as archivo:
    json.dump(extension_archivo, archivo)

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

def eliminar_archivo(nombre_archivo):
    existe=False
    if nombre_archivo != "log.txt" and nombre_archivo != "datos.json":
        for ruta_actual, subcarpetas, archivos in os.walk("."):
            for listado in archivos:
                if listado==nombre_archivo:
                    existe=True
                    archivoEliminado=os.path.join(ruta_actual,listado)
                    os.remove(archivoEliminado)
                    with open("log.txt", "a") as archivoLog:
                        now = datetime.now()
                        formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
                        archivoLog.write(f"{formatted} Se ha borrado {nombre_archivo}, se encontraba en: {ruta_actual}\n")
                    break
            if existe==True:
                break
        if existe==False:
            print("No hay un archivo con ese nombre")
              
def busqueda_avanzada(nombre_archivo):
    existe=False
    for ruta_actual, subcarpetas, archivos in os.walk("."):
        for listado in archivos:
            if listado==nombre_archivo:
                existe=True
                print(f"{nombre_archivo}, se encuentra en: {ruta_actual}")
        if existe==True:
            break
    if existe==False:
        print("No hay un archivo con ese nombre")


def copia_seguridad(archivo):
    if archivo != "log.txt" and archivo != "datos.json":
        if not os.path.exists("backup"):
            os.mkdir("backup")
        shutil.copy(f"{archivo}",f"backup/{archivo}")
        print("Se ha hecho una copia de seguridad")
        with open("log.txt", "a") as archivoLog:
            now = datetime.now()
            formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
            archivoLog.write(f"{formatted} Se ha creado una copia de seguridad de {archivo} a backup\n")

def restaurar_copia_seguridad(nombre_archivo):
    copiaSeguridad= os.path.join("backup", nombre_archivo)
    if os.path.isfile(copiaSeguridad):
        destino= os.path.join(".",nombre_archivo)
        if os.path.exists(destino):
            extension= nombre_archivo.split(".")
            shutil.move(copiaSeguridad,f"./{extension[0]}_restaurado.{extension[len(extension)-1]}")
            print(f"Se ha restaurado el archivo: {nombre_archivo}_restaurado, en el directorio actual")
            with open("log.txt", "a") as archivoLog:
                now = datetime.now()
                formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
                archivoLog.write(f"{formatted} Se ha restaurado el archivo {nombre_archivo}_restaurado en el directorio actual.\n")
        else:
            shutil.move(copiaSeguridad,".")
            print(f"Se ha restaurado el archivo: {nombre_archivo}, en el directorio actual")
            with open("log.txt", "a") as archivoLog:
                now = datetime.now()
                formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
                archivoLog.write(f"{formatted} Se ha restaurado el archivo {nombre_archivo} en el directorio actual.\n")
    else:
        print(f"{nombre_archivo} no está en la carpeta backup")
    

def gestion_permisos():
    identificado=False
    usuario=input("Indica tu usuario: ").lower()
    contrasena=input("Indica tu contraseña: ")
    with open("base_de_datos.csv", "r") as archivo:
        next(archivo)
        for linea in archivo:
            comprobacion=linea.split(",")
            if comprobacion[0]==usuario and comprobacion[len(comprobacion)-1].strip()==contrasena:
                identificado=True
                print("Acceso concedido, tienes permisos de administrador")
                return True
        if identificado==False:
            print("Usuario o contraseña no válidos, vuelve a intentarlo")
            return False
           

if gestion_permisos():
    while not salir:
        menu()
        opcion=int(input("Escoge una opción: "))

        match opcion:
            case 1:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                organizar_archivos()
            case 2:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                nombre_archivo=input("Indica el nombre del archivo: ")
                busqueda_avanzada(nombre_archivo)
            case 3:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                archivo=input("indica el archivo que deseas hacer copia de seguridad: ")
                copia_seguridad(archivo)
            case 4:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                nombreArchivo=input("Indica el nombre de archivo: ")
                restaurar_copia_seguridad(nombreArchivo)
            case 5:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                archivo_nombre=input("Indica un nombre de archivo: ")
                eliminar_archivo(archivo_nombre)
            case 6:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                salir=True
                print("Has salido del programa")
            case __:
                print("Opción incorrecta")
else:
    print("Usuario o contraseña no válidos, vuelve a intentarlo")

        
        

    
