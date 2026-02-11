class Curso():
    def __init__(self,c,n,h,p):
        self.codigo=c
        self.nombre=n
        self.hora=h
        self.precio=p
    
    def mostrar_info(self):
        return(f"Código: {self.codigo} | Nombre: {self.nombre} | Hora: {self.hora}h | Precio {self.precio}€")
    
    def calcular_precio(self):
        return(f"{self.precio} €")

class CursoOnline(Curso):
    def __init__(self, c, n, h, p, plataforma):
        super().__init__(c, n, h, p)
        self.plataforma=plataforma
    
    def mostrar_info(self):
        return (f"{super().mostrar_info()}| Plataforma: {self.plataforma}")

class CursoPresencial(Curso):
    def __init__(self, c, n, h, p, aula):
        super().__init__(c, n, h, p)
        self.aula=aula
    def calcular_precio(self):
        if self.hora>40:
            descuento=self.precio*0.15
            self.precio=self.precio+descuento
            return (f"{self.precio} €")
        else:
            return super().calcular_precio()

cursos={}

def agregar_curso(codigo,objeto):
    cursos[codigo]=objeto

def mostrar_cursos():
    for clave, valor in cursos.items():
        print(f"Código {clave}: {valor.mostrar_info()}")

def calcular_precio_final(codigo):
    for clave, valor in cursos.items():
        if clave==codigo:
            return valor.calcular_precio()
        
lista_menu=["AÑADIR CURSO", "MOSTRAR CURSOS", "CALCULAR PRECIO FINAL", ""]
def menu():
    print("*************************")
    print("MENÚ PRINCIPAL")
    print("*************************")
    



