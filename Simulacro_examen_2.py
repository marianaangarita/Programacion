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
    def set_titulo(self, titulo):
        self.titulo=titulo
    def set_autor(self, autor):
        self.autor=autor
    def set_anio_publicacion(self,anio):
        if anio>=0:
            self.anio_publicacion=anio
        else:
            return("No puedes poner un año negativo")
        
    def set_prestado(self,p):
        self.prestado=p   

    def prestar(self):
        if self.get_prestado==False:
            self.set_prestado(True)
            return(f"Se ha prestado el libro: {self.get_titulo()}, prestado: {self.get_prestado()}")
        else:
            return("El libro ya está prestado.")
        
    def devolver(self):
        if self.get_prestado==True:
            self.set_prestado(False)
            return(f"Se ha prestado el libro: {self.get_titulo()}, prestado: {self.get_prestado()}")


    def mostrar_info(self):
        return(f"Libro: {self.get_titulo()}, autor:{self.get_autor()}, año de publicación: {self.get_anio_publicacion()}, prestado: {self.get_prestado()}")
    
class Libro(Material):
    def __init__(self, titulo, autor, anio, paginas):
        super().__init__(titulo, autor, anio)
        self.num_paginas=paginas
    def get_num_paginas(self):
        return self.num_paginas
    def set_num_paginas(self,num):
        self.num_paginas=num
    def mostrar_info(self):
        return(f"Libro: {self.get_titulo()}, autor:{self.get_autor()}, año de publicación: {self.get_anio_publicacion()}, prestado: {self.get_prestado()}, número de páginas: {self.get_num_paginas()}")
    
class Revista(Material):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self.num_edicion=num_edicion

    def get_num_edicion(self):
        return self.num_edicion
    
    def set_num_edicion(self, edicion):
        self.num_edicion=edicion

    def mostrar_info(self):
        return(f"Libro: {self.get_titulo()}, autor:{self.get_autor()}, año de publicación: {self.get_anio_publicacion()}, prestado: {self.get_prestado()}, número de edición: {self.get_num_edicion()}")
    
class Biblioteca():
    def __init__(self):
        self.materiales=[]

    def agregar_material(self,material):
        existe=False
        for i in self.materiales:
            if i.titulo==material.titulo and i.autor==material.autor and i.anio_publicacion==material.anio_publicacion:
                existe=True
                return(f"El material: {material.get_titulo()}, ya está en la lista.")
        if existe==False:
            self.materiales.append(material)
            return(f"Se ha agregado el material: {material.get_titulo()}")
    
    def mostrar_materiales(self):
        lista=[]
        if self.materiales:
            for i in self.materiales:
                lista.append(i.mostrar_info())
            return lista     
        else:
            return("Lista vacía, llena la lista antes de mostrar materiales.")

    def buscar_por_titulo(self,titulo):
        existe=False
        if self.materiales:
            for i in self.materiales:
                if i.titulo==titulo:
                    existe=True
                    return(f"{i.mostrar_info()}")
            if existe==False:
                return(f"El título: {titulo} no existe en la lista.")
        else:
            return("Lista vacía, llena la lista antes de mostrar materiales.")
    
