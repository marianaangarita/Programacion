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
            

