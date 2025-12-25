'''
Actividad 07. Clase Libros
En esta actividad, vamos a crear una clase en Python que represente un libro. La clase debe tener los siguientes atributos:
titulo: El título del libro.
autor: El autor del libro.
genero: El género del libro.
paginas: El número de páginas del libro.


Además, la clase debe tener los siguientes métodos:
init(self, titulo, autor, genero, paginas): El método constructor de la clase.
get_titulo(self): El método que devuelve el título del libro.
get_autor(self): El método que devuelve el autor del libro.
get_genero(self): El método que devuelve el género del libro.
get_paginas(self): El método que devuelve el número de páginas del libro.
set_titulo(self, titulo): El método que establece el título del libro.
set_autor(self, autor): El método que establece el autor del libro.
set_genero(self, genero): El método que establece el género del libro.
set_paginas(self, paginas): El método que establece el número de páginas del libro.
'''

class Libro():
    def __init__(self,titulo,autor,genero,paginas):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.paginas=paginas
    
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_genero(self):
        return self.genero
    
    def get_paginas(self):
        return self.paginas
    
    def info(self):
        return (f"Titulo: {self.get_titulo()}, Autor: {self.get_autor()}, Género: {self.get_genero()}, Número de Páginas: {self.get_genero()}")
    
    def set_titulo(self,titulo):
        self.titulo=titulo
    
    def set_autor(self, autor):
        self.autor=autor
    
    def set_genero(self, genero):
        self.genero=genero
    
    def set_paginas(self, paginas):
        self.paginas=paginas
    
menu=["ATRIBUTOS LIBRO", "INFO", "SALIR"]

lista_libros=[]

def catalogo_libros():
    for indice, valor in enumerate(lista_libros):
        return(f"Pulsa {indice}: {valor}")

def menu_principal():

    print("***************************")

    print("MENÚ PRINCIPAL")

    for indice,valor in enumerate(menu,1):
        return(f"Pulsa {indice}: {valor}")
    
    print("***************************")

salir=False

while not salir:
    menu_principal()

    opcion=int(input("Elige una opción: "))

    match opcion:

        case 1:

            print(f"Has elegido {menu[opcion-1]}")

            titulo=input("Indica el título del libro: ").lower()
            autor=input("Indica el autor del libro").lower()
            genero=input("Indica el género del libro: ").lower()
            paginas=int(input("Indica el número de páginas del libro: "))

            libro=Libro(titulo,autor,genero,paginas)

            lista_libros.append(libro)

        case 2:
            print(f"Has elegido {menu[opcion-1]}")

            if len(lista_libros)>0:
                libro_elegido=int(input("Elige una opción: "))
            else:
                print("Lista vacía, ve primero a la opción 1")

        case 3:
            print(f"Has elegido {menu[opcion-1]}")
        case other:
            print("Opción no válida, pulsa 1, 2 o 3")


