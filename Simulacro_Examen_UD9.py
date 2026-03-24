
def leer_texto(ruta_fichero):
    with open(ruta_fichero, "r") as archivo:
        contenido=archivo.read()
        fichero_sinpuntos=contenido.replace(".", "")
        fichero_sinSignos=fichero_sinpuntos.replace(",","")
        fichero_minusculas=fichero_sinSignos.lower()
        lista_archivo=fichero_minusculas.split(" ")
        return(lista_archivo)

print(leer_texto("./archivo.txt"))

def calcular_frecuencias(lista_palabras):
    dic={}
    for clave in lista_palabras:
        if clave in dic:
            dic[clave]+=1
        else:
            dic[clave]=1
    return dic

print(calcular_frecuencias(leer_texto("./archivo.txt")))

def generar_ranking(diccionario_frecuencias):
    tuplas=[]
    for clave, valor in diccionario_frecuencias.items():
        tuplas.append((clave,valor))
    tuplas_ordenadas=tuplas.sorted(reverse=True)
    return tuplas_ordenadas
        
print(generar_ranking(calcular_frecuencias(leer_texto("./archivo.txt"))))
