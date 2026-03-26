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
    tuplas_ordenadas =[]
    lista=[]
    for clave, valor in diccionario_frecuencias.items():
        if valor not in lista:
            lista.append(valor)
    lista.sort()
    lista.reverse()
    for i in lista:
        for clave, valor in diccionario_frecuencias.items():
            if i==valor:
                tuplas_ordenadas.append((clave,valor))
    
    return(tuplas_ordenadas)

print(generar_ranking(calcular_frecuencias(leer_texto("./archivo.txt"))))

def exportar_ranking_csv(ranking, nombre_fichero):
    with open (nombre_fichero,"w") as archivo:
        contenido= archivo.write("palabra, frecuencia\n")
        for i in ranking:
            datos = archivo.write(f"{i[0]},{i[1]}\n")

exportar_ranking_csv(generar_ranking(calcular_frecuencias(leer_texto("./archivo.txt"))),"./cositas.csv")

