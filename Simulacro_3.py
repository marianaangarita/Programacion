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
            precio_final=self.precio+descuento
            return (f"{precio_final} €")
        else:
            return super().calcular_precio()
    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Aula: {self.aula}")

cursos={}

def agregar_curso(codigo,objeto):
    cursos[codigo]=objeto
    return (f"Se ha añadido {objeto.nombre} a la BBDD.")

def mostrar_cursos():
    for clave, valor in cursos.items():
        print(f"Código curso {clave}: {valor.mostrar_info()}")

def calcular_precio_final(codigo):
    existe=False
    for clave, valor in cursos.items():
        if clave==codigo:
            existe=True
            return (f"El precio final es: {valor.calcular_precio()}€")
    if existe==False:
        return(f"El curso con código {codigo} no está en la BBDD.")

        
salir=False
lista_menu=["AÑADIR CURSO", "MOSTRAR CURSOS", "CALCULAR PRECIO FINAL", "SALIR"]
def menu():
    print("*************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(lista_menu,1):
        print(f"Pulsa {clave}:{valor}")
    print("*************************")
    
while not salir:
    menu()
    opcion=int(input("Escoge una opción: "))
    match opcion:
        case 1:
            print(f"Has escogido: {lista_menu[opcion-1]}")
            codigo=int(input("Indica el código del curso: "))
            nombre=input("Indica el nombre del curso: ").lower()
            hora=int(input("Indica cuantas horas tiene el curso: "))
            precio=float(input("Indica el precio del curso: "))
            modalidad=input("Es un curso Online(O) o presencial(P) pulsa (O/P):").upper()
            match modalidad:
                case "O":
                    plataforma=input("indica en que plataforma se imparte: ").lower()
                    curso=CursoOnline(codigo, nombre, hora, precio, plataforma)
                    print(agregar_curso(curso.codigo, curso))
                case "P":
                    aula=int(input("Indica el número del aula donde se imparte: "))
                    curso=CursoPresencial(codigo, nombre, hora, precio, aula)
                    print(agregar_curso(curso.codigo, curso))
                case __:
                    print("Opción incorrecta, pulsa O o P")             
        case 2:
            print(f"Has escogido: {lista_menu[opcion-1]}")
            if cursos:
                mostrar_cursos()
            else:
                print("BBDD vacía, primero añade cursos y despues usa esta opción.")
        case 3:
            print(f"Has escogido: {lista_menu[opcion-1]}")
            codigo_curso=int(input("Indica el código del curso: "))
            print(calcular_precio_final(codigo_curso))
        case 4:
            print(f"Has escogido: {lista_menu[opcion-1]}")
            salir=True
            print("Has salido del programa.")
        case __:
            print("Opción incorrecta, pulsa del 1 al 4.")


