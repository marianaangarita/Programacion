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

if not os.path.exists("datos.json"):
    with open("datos.json", "w") as archivo:
        json.dump(extension_archivo, archivo)
   
with open("datos.json", "r") as archivo:
    datos=json.load(archivo)

def escribir_log(mensaje):
    with open("log.txt", "a") as archivoLog:
        now = datetime.now()
        formatted = now.strftime("[%Y-%m-%d %H:%M:%S]")
        archivoLog.write(f"{formatted} {mensaje}\n")
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
                            escribir_log(f"Movido {archivo} a {carpeta}")
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
                if listado.lower()==nombre_archivo.lower():
                    existe=True
                    archivoEliminado=os.path.join(ruta_actual,listado)
                    try:
                        os.remove(archivoEliminado)
                        escribir_log(f"Se ha borrado {nombre_archivo}, se encontraba en: {ruta_actual}")
                        break
                    except PermissionError:
                        print("El archivo está en uso o falta privilegios del administrador.")
            if existe==True:
                break
        if existe==False:
            print("No hay un archivo con ese nombre")
              
def busqueda_avanzada(nombre_archivo):
    existe=False
    for ruta_actual, subcarpetas, archivos in os.walk("."):
        for listado in archivos:
            if nombre_archivo.lower() in listado.lower():
                existe=True
                print(f"{listado}, se encuentra en: {ruta_actual}")         
    if existe==False:
        print("No hay un archivo con ese nombre")


def copia_seguridad(archivo):
    existe=False
    contador=0
    if not os.path.exists("backup"):
            os.mkdir("backup")
    for ruta_actual, subcarpetas, archivos in os.walk("."):
        if not ruta_actual.startswith("./backup"):
            for listado in archivos:
                if listado.lower()==archivo.lower():
                    existe=True
                    copiaSeguridad=os.path.join(ruta_actual,listado)
                    nombre, extension=os.path.splitext(archivo)
                    archivoDuplicado= os.path.join("backup", f"{nombre}_copia{contador}{extension}")

                    while os.path.exists(archivoDuplicado):
                        contador+=1
                        archivoDuplicado= os.path.join("backup", f"{nombre}_copia{contador}{extension}")
                    
                    shutil.copy(f"{copiaSeguridad}",f"backup/{nombre}_copia{contador}{extension}")
                    print(f"Se ha hecho una copia de seguridad a {nombre}_copia{contador}{extension}")
                    escribir_log(f"Se ha creado una copia de seguridad de {nombre}_copia{contador}{extension} a backup") 
                    break
            if existe==True:
                break
    if existe==False:
        print("No hay un archivo con ese nombre")   

def restaurar_copia_seguridad(nombre_archivo):
    copiaSeguridad= os.path.join("backup", nombre_archivo)
    if os.path.isfile(copiaSeguridad):
        destino= os.path.join(".",nombre_archivo)
        if os.path.exists(destino):
            nombre, extension =os.path.splitext(nombre_archivo)
            shutil.move(copiaSeguridad,f"./{nombre}_restaurado{extension}")
            print(f"Se ha restaurado el archivo: {nombre}_restaurado{extension}, en el directorio actual")

            escribir_log(f"Se ha restaurado el archivo {nombre_archivo}_restaurado en el directorio actual.") 
            
        else:
            shutil.move(copiaSeguridad,".")
            print(f"Se ha restaurado el archivo: {nombre_archivo}, en el directorio actual")
            escribir_log(f"Se ha restaurado el archivo {nombre_archivo}_restaurado en el directorio actual.")
    else:
        print(f"{nombre_archivo} no está en la carpeta backup")
    

def gestion_permisos():
    try:
        with open("base_de_datos.csv", "r") as archivo:
            next(archivo)
    except FileNotFoundError:
        usuario="admin" 
        contrasena="admin"      
        with open("base_de_datos.csv", "w") as archivo:
            archivo.write("usuario,password\n")
            archivo.write(f"{usuario},{contrasena}")
            
    while True:
        usuario=input("Indica tu usuario: ").lower()
        contrasena=input("Indica tu contraseña: ")
        with open("base_de_datos.csv", "r") as archivo:
            next(archivo)
            for linea in archivo:
                comprobacion=linea.split(",")
                if comprobacion[0]==usuario and comprobacion[len(comprobacion)-1].strip()==contrasena:
    
                    print("Acceso concedido, tienes permisos de administrador")
                    return True
            print("Usuario o contraseña no válidos, vuelve a intentarlo")
    

gestion_permisos()     
while not salir:
    menu()
    try:
        opcion=int(input("Escoge una opción: "))
        match opcion:
            case 1:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                organizar_archivos()
            case 2:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                try:
                    nombre_archivo=input("Indica el nombre del archivo: ").strip()
                    busqueda_avanzada(nombre_archivo)
                except Exception as e:
                    print(f"Error inesperado: {e}")
            case 3:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                try:
                    archivo=input("indica el archivo que deseas hacer copia de seguridad: ").strip()
                    copia_seguridad(archivo)
                except Exception as e:
                    print(f"Error inesperado: {e}")
            case 4:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                try:
                    nombreArchivo=input("Indica el nombre de archivo: ").strip()
                    restaurar_copia_seguridad(nombreArchivo)
                except Exception as e:
                    print(f"Error inesperado: {e}")
            case 5:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                try:
                    archivo_nombre=input("Indica un nombre de archivo: ").strip()
                    eliminar_archivo(archivo_nombre)
                except Exception as e:
                    print(f"Error inesperado: {e}")
            case 6:
                print(f"Has elegido: {opciones_menu[opcion-1]}")
                salir=True
                print("Has salido del programa")
            case __:
                print("Opción incorrecta, escoge del 1 al 6")

    except ValueError:
        print("Opción no válida, escoge un número")


        
        

    
