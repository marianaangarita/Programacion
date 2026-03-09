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

def mostrar_archivos():
    print("Archivos en el directorio actual:")
    print(os.listdir("."))

def organizar_archivos():
    extensiones={".txt":"Textos", ".jpg":"Imágenes", ".csv":"Datos"}
    for archivo in os.listdir("."):
        for ext, carpeta in extensiones.items():
            if archivo.endswith(ext):
                if not os.path.exists(carpeta):
                    os.mkdir(carpeta)
                shutil.move(archivo,carpeta)
                with open("log.txt", "a") as log:
                    log.write(f"Movido {archivo} a {carpeta}\n")
                    

