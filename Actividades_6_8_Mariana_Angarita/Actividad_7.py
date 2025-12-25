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
    
    def set_titulo(self,titulo):
        self.titulo=titulo
    
    def set_autor(self, autor):
        self.autor=autor
    
    def set_genero(self, genero):
        self.genero=genero
    
    def set_paginas(self, paginas):
        self.paginas=paginas
    
