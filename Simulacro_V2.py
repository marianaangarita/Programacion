def leer_texto(ruta_fichero):
    with open(ruta_fichero, "r") as archivo:
        LecturaArchivo= archivo.read()
        ArchivoSinComas = LecturaArchivo.replace(",","")
        ArchivoSinPuntos = ArchivoSinComas.replace(".","")
        ArchivoEnMinusculas = ArchivoSinPuntos.lower()
        ListaArchivo = ArchivoEnMinusculas.split(" ")
        return ListaArchivo

print(leer_texto("./archivo.txt"))

def calcular_frecuencias(lista_palabras):
    dic={}
    for palabra in lista_palabras:
        if palabra in dic:
            dic[palabra]+=1
        else:
            dic[palabra]=1
    return dic

print(calcular_frecuencias(leer_texto("./archivo.txt")))

def generar_ranking(diccionario_frecuencias):
    tuplas_ordenadas = sorted(diccionario_frecuencias.items(), key=lambda x: x[1], reverse=True)
    return(tuplas_ordenadas)

print(generar_ranking(calcular_frecuencias(leer_texto("./archivo.txt"))))