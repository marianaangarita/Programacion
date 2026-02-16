class Material():
    def __init__(self, titulo, autor, anio):
        self.titulo=titulo
        self.autor=autor
        self.anio_publicacion=anio
        self.prestado=False

    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_anio_publicacion(self):
        return self.anio_publicacion
    
    def get_prestado(self):
        return self.prestado
    
    def set_titulo(self,t):
        self.titulo=t
    def set_autor(self,a):
        self.autor=a
    def set_anio_publicacion(self, p):
        if p>=0:
            self.anio_publicacion=p
        else:
            return(f"El año de publicación no puede ser negativo")
        
    def set_prestado(self,p):
        self.prestado=p

    def prestar(self):
        if self.get_prestado()==False:
            self.set_prestado(True)
            print("Se ha prestado el material")
        else:
            print("El material ya estaba prestado")
    
    def devolver(self):
        if self.get_prestado()==True:
            self.set_prestado(False)
            print("Se ha devuelto el material")
        else:
            print("El material no estaba prestado")
    
    def mostrar_info(self):
        if self.get_prestado()==True:
            estado="Prestado"
        else:
            estado="Disponible"
        return(f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Año: {self.get_anio_publicacion()} | Estado: {estado}")

class Libro(Material):
    def __init__(self, titulo, autor, anio, pagina):
        super().__init__(titulo, autor, anio)
        self.num_paginas=pagina
    def get_num_paginas(self):
        return self.num_paginas
    def set_num_paginas(self,n):
        if n>0:
            self.num_paginas=n
        else:
            return("El número de páginas no puede ser negativo o cero.")
        
    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Número de páginas: {self.get_num_paginas()}")

class Revista(Material):
    def __init__(self, titulo, autor, anio, edicion):
        super().__init__(titulo, autor, anio)
        self.num_edicion=edicion
    
    def get_num_edicion(self):
        return self.num_edicion
    
    def set_num_edicion(self,e):
        if e>0:
            self.num_edicion=e
        else:
            return(f"El numero de edición no puede ser negativo o cero.")
    
    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Número de Edición: {self.get_num_edicion()}")
    
class Biblioteca():
    def __init__(self):
        self.materiales=[]
    
    def agregar_material(self, material):
        self.materiales.append(material)
        return(f"Se ha agregado: {material.get_titulo()} a la biblioteca")
    
    def mostrar_materiales(self):
        for material in self.materiales:
            print(material.mostrar_info())
    
    def buscar_por_titulo(self, titulo):
        for material in self.materiales:
            if material.get_titulo()==titulo:
                return(material.mostrar_info())
        return(f"El título {titulo} no existe en la biblioteca.")
        
biblioteca=Biblioteca()
libro=Libro("Python desde Cero", "Carlos", 2025, 350)
revista=Revista("Programación Hoy", "Mariana", 2001, 42)

print(biblioteca.agregar_material(libro))

print(biblioteca.agregar_material(revista))

biblioteca.mostrar_materiales()

libro.prestar()

biblioteca.mostrar_materiales()

libro_2=Libro("Programación para principiantes", "Jorge", 1990, 205)

print(libro_2.set_anio_publicacion(-2005))

print(biblioteca.buscar_por_titulo("Python desde Cero"))
