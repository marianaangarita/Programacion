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
        archivo.close()

def media():
    notas=0
    total_notas=0
    try:
        with open("notas.csv", "r") as archivo:
            next(archivo)
            for linea in archivo:
                partes=linea.split(",")
                notas=notas+float(partes[len(partes)-1])
                total_notas=total_notas+1
            try:
                media=notas/total_notas
                print(f"La media total es: {media}")
            except ZeroDivisionError:
                print("No se puede dividir por cero, primero añade datos al fichero.")
            archivo.close()
    except FileNotFoundError:
        print("El archivo no se ha encontrado, o no existe")
        

def notas_alumno(nombre):
    existe=False
    try:
        with open("notas.csv", "r") as archivo:
            for linea in archivo:
                nombre_alumno=linea.split(",")
                if nombre_alumno[0]==nombre:
                    existe=True
                    print(f"{nombre_alumno[len(nombre_alumno)-2]}:{nombre_alumno[len(nombre_alumno)-1]}")
            if existe == False:
                print(f"El alumno: {nombre}, no existe en el fichero.")
            archivo.close()
    except FileNotFoundError:
        print("El archivo no se ha encontrado, o no existe")


while not salir:
    menu()
    try:
        opcion=int(input("Escoge una opción: "))
    except ValueError:
        print("Opción no válida, Pulsa del 1 al 4.")
    match opcion:
        case 1:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            try:
                nombre=input("Indica el nombre: ").capitalize()
                asignatura=input("Indica la asignatura: ").capitalize()
                nota=float(input("Indica la nota: "))
            except ValueError:
                print("Opción no válida")
            agregar_notas(nombre, asignatura, nota)
        case 2:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            media()
        case 3:
            print(f"Has elegido: {opciones_menu[opcion-1]}")
            try:
                nombre=input("Indica el nombre: ").capitalize()
            except ValueError:
                print("Opción no válida")
            notas_alumno(nombre)
        case 4:
            salir=True
            print("Has salido del programa")
        case __:
            print("opción incorrecta.")


            

        



