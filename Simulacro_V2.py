def leer_texto(ruta_fichero):
    with open(ruta_fichero, "r") as archivo:
        LecturaArchivo= archivo.read()
        ArchivoSinComas = LecturaArchivo.replace(",","")
        ArchivoSinPuntos = ArchivoSinComas.replace(".","")
        ArchivoEnMinusculas = ArchivoSinPuntos.lower()
        ListaArchivo = ArchivoEnMinusculas.split(" ")
        return ListaArchivo

print(leer_texto("./archivo.txt"))
