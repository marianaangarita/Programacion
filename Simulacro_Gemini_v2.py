'''
Simulacro de Examen: La Biblioteca
Contexto: Se requiere una aplicación de consola para gestionar el inventario de libros.

1. Clase Base: Libro (Abstracción y Encapsulación)
Crea una clase que represente un libro.

Atributos:

titulo (string)

autor (string)

genero (string) - (Esto será el equivalente a "especie")

paginas (int)

precio (float)

Métodos:

Constructor: Inicializa los atributos.

Getters y Setters:

Asegura que paginas no sea negativo.

Asegura que precio sea mayor que 0.

mostrar_info(): Devuelve una cadena con los datos del libro.

2. Clase de Gestión: Biblioteca (Composición)
Crea una clase que gestione la lista de libros.

Atributo: catalogo (lista vacía al inicio).

Métodos:

agregar_libro(libro): Añade un objeto Libro a la lista.

mostrar_catalogo(): Muestra la info de todos los libros.

buscar_por_titulo(titulo): Busca un libro y lo muestra (¡Cuidado con el mensaje de "no encontrado"!).

mostrar_generos(): Muestra los géneros que hay en la biblioteca sin repetir (lógica de lista auxiliar).

3. El Menú Interactivo
Un bucle while con las opciones:

Crear Libro (pide datos al usuario).

Ingresar Libro en Biblioteca (valida que exista el objeto).

Buscar Libro.

Mostrar Géneros disponibles.

Salir.
'''

class Libro():
    def __init__(self, titulo, autor, genero, paginas, precio):
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        if paginas>0: self.paginas=paginas 
        else: self.paginas=1
        if precio>0: self.precio=precio 
        else: self.precio=1.1

    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_genero(self):
        return self.genero
    def get_paginas(self):
        return self.paginas
    def get_precio(self):
        return self.precio
    def set_titulo(self, titulo):
        self.titulo=titulo
    def set_autor(self, autor):
        self.autor=autor
    def set_genero(self, genero):
        self.genero=genero
    def set_paginas(self, paginas):
        if paginas>0:
            self.paginas=paginas
        else:
            print("No puedes poner páginas negativas")

    def set_precio(self, precio):
        if precio>0:
            self.precio=precio
        else:
            print("No puedes poner precio negativo.")
    
    def mostrar_info(self):
        return(f" El libro con título: {self.get_titulo()}, del autor: {self.get_autor()}, pertenece al género: {self.get_genero()}, tiene: {self.get_paginas()} páginas, y cuesta: {self.get_precio()} €.")
    
class GestionBiblioteca():
    def __init__(self):
        self.catalogo=[]
    
    def agregar_libro(self, libro):
        for i in self.catalogo:
            if i.titulo==libro.titulo and i.autor==libro.autor:
                return(f"El libro: {libro.titulo} ya está en el catálogo.")
        self.catalogo.append(libro)
        return(f"Se ha añadido {libro.get_titulo()} al catálogo.")
    
    def mostrar_catalogo(self):
        if self.catalogo:
            for i in self.catalogo:
                print({i.mostrar_info()})
        else:
            print("Lista vacía, tiene que agregar libros al catálogo.")
    
    def buscar_por_titulo(self, titulo):
        encontrado=False
        if self.catalogo:
            for i in self.catalogo:
                if i.titulo==titulo:
                    encontrado=True
                    return(f"{i.mostrar_info()}")
            if encontrado==False:
                return("Libro no encontrado, no existe en el catálogo.")
        else:
            return("Lista vacía, tiene que agregar libros al catálogo.")
    
    def mostrar_generos(self):
        lista_generos=[]
        if self.catalogo:
            for i in self.catalogo:
                if i.genero not in lista_generos:
                    lista_generos.append(i.genero)
            return(f" Los géneros que hay en el catálogo son: {lista_generos}")
        else:
            return("Lista vacía, tiene que agregar libros al catálogo.")
        
biblioteca=GestionBiblioteca()
    
salir=False

libro=None

lista_menu=["CREAR LIBRO", "INGRESAR LIBRO BIBLIOTECA", "BUSCAR LIBRO", "MOSTRAR GÉNEROS DISPONIBLES", "MOSTRAR CATÁLOGO", "SALIR"]

def menu():
    print("***********************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(lista_menu, 1):
        print(f"Pulsa {clave}: {valor}")
    print("***********************")

while not salir:
    menu()
    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            titulo=input("Escribe el título del libro: ").lower()
            autor=input("Indica el autor: ").lower()
            genero=input("Indica el género: ").lower()
            pagina=int(input("Indica el número de páginas: "))
            precio=float(input("Indica el precio del libro: "))

            libro=Libro(titulo, autor, genero, pagina, precio)
        case 2:
            if libro:
                print(biblioteca.agregar_libro(libro))
            else:
                print("Primero tienes que crear un libro para agregarlo al catálogo.")
        case 3:
            titulo=input("Que título buscas: ").lower()
            print(biblioteca.buscar_por_titulo(titulo))
        case 4:
            print(biblioteca.mostrar_generos())
        case 5:
            biblioteca.mostrar_catalogo()
        case 6:
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta, escoge del 1 al 6.")
