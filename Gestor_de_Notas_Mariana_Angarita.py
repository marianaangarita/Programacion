'''
Objetivo: Crear un sistema de almacenamiento y consulta de calificaciones de alumnos utilizando archivos CSV.
Pasos:
Crea un fichero notas.csv con la siguiente estructura:Nombre,Asignatura,Nota
María,Matemáticas,8.5
Pedro,Física,7.2
Implementa una opción para agregar nuevas notas al archivo.
Implementa una opción para calcular la media de todas las notas.
Implementa una opción para mostrar las notas de un alumno en específico.
Asegúrate de que el programa maneje errores si el fichero no existe o está vacío.
'''

salir=False
opciones_menu=["AGREGAR NUEVAS NOTAS", "CALCULAR LA MEDIA", "VER NOTAS DE UN ALUMNO", "SALIR"]

def menu():
    print("MENÚ PRINCIPAL")
    print("**************************")
    for clave, valor in enumerate(opciones_menu,1):
        print(f"Pulsa {clave}: {valor}")
    print("**************************")

def agregar_notas(nombre, asignatura, nota):
    with open("notas.csv", "a") as archivo:
        archivo.write(f"{nombre},{asignatura},{nota}\n")

def media():
    notas=0
    total_notas=0
    with open("notas.csv", "r") as archivo:
        for linea in archivo:
            partes=linea.split(",")
        for partes[len(partes)-1] in archivo:
            


