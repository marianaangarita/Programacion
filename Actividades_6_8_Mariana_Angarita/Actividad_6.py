'''
Actividad 06. Clase Productos
Crear una clase en Python que represente un Producto. Los atributos de un producto serán su nombre, su precio y su descripción. Los métodos de la clase serán los siguientes:
__init__(): Crea un nuevo producto con los atributos especificados.
get_nombre(): Devuelve el nombre del producto.
get_precio(): Devuelve el precio del producto.
get_descripcion(): Devuelve la descripción del producto.
set_nombre(x): Modifica el nombre del producto.
set_precio(x): Modifica el precio del producto.
set_descripcion(x): Modifica la descripción del producto.
'''

class Producto():
    
    def __init__(self,n,p,d):
        self.nombre=n
        self.precio=p
        self.descripcion=d

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_descripcion(self):
        return self.descripcion
    
    def set_nombre(self,n):
        self.nombre=n

    def set_precio(self,p):
        self.precio=p

    def set_descripcion(self,d):
        self.descripcion=d


producto1=Producto("pendiente",20,"Pediente de plata con circonitas")

producto2=Producto("anillo",15,"anillo de plata con circonitas")

print(producto1.get_nombre())

producto1.set_nombre("collar")

print(producto1.get_nombre())

print(producto1.get_precio())

producto1.set_precio(5)

print(producto1.get_precio())