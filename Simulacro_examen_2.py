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
        self.anio_publicacion=anio
    
        
    def set_prestado(self,p):
        self.prestado=p   

    def prestar(self):
        prestado=""
        if self.get_prestado()==False:
            self.set_prestado(True)
            prestado="Prestado"
            return(f"Se ha prestado el material: {self.get_titulo()}, estado: {prestado}")
        else:
            return("El material ya está prestado.")
        
    def devolver(self):
        prestado=""
        if self.get_prestado()==True:
            self.set_prestado(False)
            prestado="Disponible"
            return(f"Se ha devuelto el material: {self.get_titulo()}, estado: {prestado}")
        else:
            return("El material no está prestado")


    def mostrar_info(self):
        prestado=""
        if self.get_prestado()==True:
            prestado="Prestado"
        if self.get_prestado()==False:
            prestado="Disponible"
        return(f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Año: {self.get_anio_publicacion()} | Estado: {prestado}")
    
class Libro(Material):
    def __init__(self, titulo, autor, anio, paginas):
        super().__init__(titulo, autor, anio)
        self.num_paginas=paginas
    def get_num_paginas(self):
        return self.num_paginas
    def set_num_paginas(self,num):
        self.num_paginas=num
    def mostrar_info(self):
        return(f"{super().mostrar_info()} | Número de páginas: {self.get_num_paginas()}")
    
class Revista(Material):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self.num_edicion=num_edicion

    def get_num_edicion(self):
        return self.num_edicion
    
    def set_num_edicion(self, edicion):
        self.num_edicion=edicion

    def mostrar_info(self):
        return(f"{super().mostrar_info()} | Número de edición: {self.get_num_edicion()}")
    
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

        if self.materiales:
            for i in self.materiales:
                print(i.mostrar_info())    
        else:
            print("Lista vacía, llena la lista antes de mostrar materiales.")

    def buscar_por_titulo(self,titulo):
        existe=False
        if self.materiales:
            for i in self.materiales:
                if i.get_titulo()==titulo:
                    existe=True
                    return(i.mostrar_info())
            if existe==False:
                return(f"El título: {titulo} no existe en la lista.")
        else:
            return("Lista vacía, llena la lista antes de mostrar materiales.")
    
biblioteca=Biblioteca()

salir=False

material=None

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
            titulo=input("Indica el título: ").lower()
            autor=input("Indica el autor: ").lower()
            anio=int(input("Indica el año de publicación: "))
            paginas=int(input("Indica el número de páginas: "))
            if anio>=0 and paginas>0:
                material=Libro(titulo, autor, anio, paginas)
            else:
                print("Los datos introducidos no son correctos, el año y las páginas no pueden ser negativos.")
        case 2:
            print(f"Has escogido {lista_menu[opcion-1]}")
            titulo=input("Indica el título: ").lower()
            autor=input("Indica el autor: ").lower()
            anio=int(input("Indica el año de publicación: "))
            edicion=int(input("Indica el número de edición: "))
            if anio>=0 and edicion>0:
                material=Revista(titulo, autor, anio, edicion)
            else:
                print("Los datos introducidos no son correctos, el año y la edición no pueden ser negativos.")
        case 3:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                print(biblioteca.agregar_material(material))
            else:
                print("Debes crear una revista o libro antes de agregarlo a la biblioteca.")
        case 4:
            print(f"Has escogido {lista_menu[opcion-1]}")
            biblioteca.mostrar_materiales()
        case 5:
            print(f"Has escogido {lista_menu[opcion-1]}")
            t=input("Que título buscas: ").lower()
            print(biblioteca.buscar_por_titulo(t))
        case 6:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                print(material.prestar())
            else:
                print("Debes crear una revista o un libro primero.")
        case 7:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                print(material.devolver())
            else:
                print("Debes crear una revista o un libro primero.")
        case 8:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                t=input("Indica el nuevo título: ").lower()
                material.set_titulo(t)
                print(material.get_titulo())
            else:
                print("Debes crear una revista o un libro primero.")
        case 9:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                a=input("Indica el nuevo autor: ").lower()
                material.set_autor(a)
                print(material.get_autor())
            else:
                print("Debes crear una revista o un libro primero.")
        case 10:
            print(f"Has escogido {lista_menu[opcion-1]}")
            if material:
                p=int(input("Indica el nuevo año de publicación: "))
                if p>=0:
                    material.set_anio_publicacion(p)
                    print(material.get_anio_publicacion())
                else:
                    print("No puedes poner un año negativo")
            else:
                print("Debes crear una revista o un libro primero.")
        case 11:
            print(f"Has escogido {lista_menu[opcion-1]}")
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta. Pulsa del 1 al 11.")
