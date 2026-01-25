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
        if self.get_prestado()==False:
            self.set_prestado(True)
            return(f"Se ha prestado el libro: {self.get_titulo()}, prestado: {self.get_prestado()}")
        else:
            return("El libro ya está prestado.")
        
    def devolver(self):
        if self.get_prestado()==True:
            self.set_prestado(False)
            return(f"Se ha devuelto el libro: {self.get_titulo()}, prestado: {self.get_prestado()}")


    def mostrar_info(self):
        prestado=""
        if self.get_prestado()==True:
            prestado="Prestado"
        if self.get_prestado()==False:
            prestado="Disponible"
        return(f"Libro: {self.get_titulo()}, autor:{self.get_autor()}, año de publicación: {self.get_anio_publicacion()}, prestado: {prestado}")
    
class Libro(Material):
    def __init__(self, titulo, autor, anio, paginas):
        super().__init__(titulo, autor, anio)
        self.num_paginas=paginas
    def get_num_paginas(self):
        return self.num_paginas
    def set_num_paginas(self,num):
        self.num_paginas=num
    def mostrar_info(self):
        return(f"{super().mostrar_info()}, número de páginas: {self.get_num_paginas()}")
    
class Revista(Material):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self.num_edicion=num_edicion

    def get_num_edicion(self):
        return self.num_edicion
    
    def set_num_edicion(self, edicion):
        self.num_edicion=edicion

    def mostrar_info(self):
        return(f"{super().mostrar_info()}, número de edición: {self.get_num_edicion()}")
    
class Biblioteca():
    def __init__(self):
        self.materiales=[]

    def agregar_material(self,material):
        existe=False
        for i in self.materiales:
            if i.get_titulo()==material.get_titulo() and i.get_autor()==material.get_autor() and i.get_anio_publicacion()==material.get_anio_publicacion():
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
                if i.get_titulo()==titulo:
                    existe=True
                    return(f"{i.mostrar_info()}")
            if existe==False:
                return(f"El título: {titulo} no existe en la lista.")
        else:
            return("Lista vacía, llena la lista antes de mostrar materiales.")
    
biblioteca=Biblioteca()

salir=False

libro=None
revista=None

lista_menu=["CREAR LIBRO", "CREAR UNA REVISTA", "AGREGAR MATERIAL", "MOSTRAR MATERIAL", "BUSCAR POR TÍTULO", "PRESTAR MATERIAL", "DEVOLVER MATERIAL", "CAMBIAR TÍTULO", "CAMBIAR AUTOR", "CAMBIAR AÑO DE PUBLICACIÓN", "SALIR"]

def menu():
    print("******************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(lista_menu, 1):
        print(f"Pulsa {clave}: {valor}")
    print("******************************")

while not salir:
    menu()
    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print(f"Has escogido {lista_menu[opcion-1]}")
            titulo=input("Indica el título del libro: ").lower()
            autor=input("Indica el autor del libro: ").lower()
            anio=int(input("Indica el año de publicación: "))
            paginas=int(input("Indica el número de páginas: "))
            if anio>=0 and paginas>0:
                libro=Libro(titulo, autor, anio, paginas)
            else:
                print("Los datos introducidos no son correctos, el año y las páginas no pueden ser negativos.")
        case 2:
            print(f"Has escogido {lista_menu[opcion-1]}")
            titulo=input("Indica el título del libro: ").lower()
            autor=input("Indica el autor del libro: ").lower()
            anio=int(input("Indica el año de publicación: "))
            edicion=int(input("Indica el número de edición: "))
            if anio>=0 and edicion>0:
                revista=Revista(titulo, autor, anio, edicion)
            else:
                print("Los datos introducidos no son correctos, el año y la edición no pueden ser negativos.")
        case 3:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                print(biblioteca.agregar_material(libro))
            if revista:
                print(biblioteca.agregar_material(revista))
            else:
                print("Debes crear una revista o libro antes de agregarlo a la biblioteca.")
        case 4:
            print(f"Has escogido {lista_menu[opcion-1]}")
            print(biblioteca.mostrar_materiales())
        case 5:
            print(f"Has escogido {lista_menu[opcion-1]}")
            t=input("Que título buscas: ").lower()
            print(biblioteca.buscar_por_titulo(t))
        case 6:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                print(libro.prestar())
            if revista:
                print(revista.prestar())
            else:
                print("Debes crear una revista o un libro primero.")
        case 7:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                print(libro.devolver())
            if revista:
                print(revista.devolver())
            else:
                print("Debes crear una revista o un libro primero.")
        case 8:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                t=input("Indica el nuevo título: ").lower()
                print(libro.set_titulo(t))
            if revista:
                t=input("Indica el nuevo título: ").lower()
                print(revista.set_titulo(t))
            else:
                print("Debes crear una revista o un libro primero.")
        case 9:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                a=input("Indica el nuevo autor: ").lower()
                print(libro.set_autor(a))
            if revista:
                a=input("Indica el nuevo autor: ").lower()
                print(revista.set_autor(a))
            else:
                print("Debes crear una revista o un libro primero.")
        case 10:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if libro:
                p=int(input("Indica el nuevo año de publicación: "))
                print(libro.set_anio_publicacion(p))
            if revista:
                p=int(input("Indica el nuevo año de publicación: "))
                print(revista.set_anio_publicacion(p))
            else:
                print("Debes crear una revista o un libro primero.")
        case 11:
            print(f"Has escogido {lista_menu[opcion-1]}")
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta. Pulsa del 1 al 11.")
