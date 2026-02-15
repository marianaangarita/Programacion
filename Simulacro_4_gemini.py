'''
Contexto:
Una cadena hotelera necesita un programa en Python para gestionar las reservas de sus habitaciones. Existen diferentes tipos de habitaciones, pero todas comparten características comunes.

Ejercicio 1 - Clase Base (2 puntos)
Crea una clase llamada Habitacion con los siguientes atributos:

numero (identificador, clave del diccionario)

huesped (nombre de la persona)

dias (cantidad de días de estancia)

precio_noche (precio base por noche)

Métodos:

mostrar_info(): Muestra la información de la habitación.

calcular_total(): Devuelve el coste total de la estancia (días * precio_noche).

Ejercicio 2 - Herencia (3 puntos)
A partir de la clase Habitacion, crea las siguientes clases hijas:

HabitacionSuite (hereda de Habitacion):

Atributo adicional: jacuzzi (booleano: True/False).

Sobrescribe mostrar_info(): Para incluir si tiene jacuzzi o no.

Sobrescribe calcular_total(): Si tiene jacuzzi, se suma un plus fijo de 50€ al total de la estancia (no por noche, sino al total).

HabitacionLargaEstancia (hereda de Habitacion):

Atributo adicional: descuento (un entero, por ejemplo, 10 para 10%).

Sobrescribe mostrar_info(): Para mostrar el porcentaje de descuento.

Sobrescribe calcular_total(): Si la estancia (dias) es mayor a 7 días, se aplica el porcentaje de descuento al precio total. Si son 7 días o menos, no se aplica descuento.

Ejercicio 3 - Diccionario (1 punto)
Crea un diccionario llamado hotel = {} donde la clave será el número de habitación y el valor será el objeto creado.

Ejercicio 4 - Funciones y Menú (4 puntos)
Implementa un menú con las siguientes opciones que llamen a sus respectivas funciones:

Registrar Habitación: Pide los datos al usuario. Debe preguntar qué tipo de habitación es (Normal, Suite o Larga Estancia) y pedir los atributos específicos según el caso. Guarda el objeto en el diccionario.

Mostrar Habitaciones: Recorre el diccionario y muestra la info de todas.

Calcular Precio Final: Pide un número de habitación y muestra cuánto debe pagar el huésped (usando el método calcular_total).

Salir.
'''

class Habitacion():
    def __init__(self, num, huesped, dias, precio):
        self.numero=num
        self.huesped=huesped
        self.dia=dias
        self.precio_noche=precio

    def get_numero(self):
        return self.numero
    def get_huesped(self):
        return self.huesped
    def get_dia(self):
        return self.dia
    def get_precio(self):
        return self.precio_noche
    def set_numero(self,n):
        self.numero=n
    def set_huesped(self,h):
        self.huesped=h
    def set_dia(self,d):
        self.dia=d
    def set_precio_noche(self,p):
        self.precio_noche=p
    
    def mostrar_info(self):
        return(f" Huésped: {self.get_huesped()} | Días: {self.get_dia()} | Precio Noche: {self.get_precio()}")
    
    def calcular_total(self):
        return self.get_dia()*self.get_precio()

class HabitacionSuite(Habitacion):
    def __init__(self, num, huesped, dias, precio, jacuzzi):
        super().__init__(num, huesped, dias, precio)
        self.jacuzzi=jacuzzi

    def get_jacuzzi(self):
        return self.jacuzzi
    def set_jacuzzi(self, j):
        self.jacuzzi=j

    def mostrar_info(self):
        if self.get_jacuzzi()==True:
            hay_jacuzzi="Si"
        else:
            hay_jacuzzi="No"
        return (f"{super().mostrar_info()} | Jacuzzi: {hay_jacuzzi}")
    
    def calcular_total(self):
        if self.get_jacuzzi()==True:
            return (super().calcular_total()) + 50
        else:
            return (super().calcular_total())

class HabitacionLargaEstancia(Habitacion):
    def __init__(self, num, huesped, dias, precio, descuento):
        super().__init__(num, huesped, dias, precio)
        self.descuento=descuento

    def get_descuento(self):
        return self.descuento
    
    def set_descuento(self,d):
        self.descuento=d

    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Descuento: {self.get_descuento()}%")
    
    def calcular_total(self):
        if self.get_dia()>7:
            descuento=(self.get_dia()*self.get_precio())*(self.get_descuento()/100)
            precio_final=(self.get_dia()*self.get_precio())-descuento
            return precio_final

        else:
            return super().calcular_total()
    
hotel={}
salir=False
opcion_menu=["REGISTRAR HABITACIÓN", "MOSTRAR HABITACIONES", "CALCULAR PRECIO FINAL", "SALIR"]

def menu():
    print("*************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(opcion_menu, 1):
        print(f"Pulsa {clave}: {valor}")
    print("*************************")

def registrar_habitacion(numero,objeto):
    if numero in hotel:
        return(f"La habitación con código: {numero} ya estaba en la base de datos.")
    else:
        hotel[numero]=objeto
        return(f"Has agregado la habitación {numero} a la BBDD.")

def mostrar_habitaciones():
    for clave, valor in hotel.items():
        print(f"Número {clave}:{valor.motrar_info()}")

def calcular_precio_final(numero):
    if numero in hotel:
        return hotel[numero].calcular_total()
    else:
        return(f"La habitación con código: {numero}, no está en la BBDD.")
   
while not salir:
    menu()
    opcion=int(input("Escoge una opción: "))

    match opcion:
        case 1:
            print(f"Has escogido: {opcion_menu[opcion-1]}")
            numero=int(input("Indica el número de la habitación: "))
            huesped=input("Indica el nombre del huésped: ").lower()
            dias=int(input("Indica la cantidad de dias de estancia: "))
            precio=float(input("Indica el precio base por noche: "))
            tipo=input("Indica tipo de habitación Normal(N)/Suite(S)/Larga Estancia(L): ").upper()
            match tipo:
                case "N":
                    hab=Habitacion(numero, huesped, dias, precio)
                    print(registrar_habitacion(hab.get_numero(),hab))
                case "S":
                    jacuzzi=bool(input("¿Tiene jacuzzi? (True/False): "))
                    hab=HabitacionSuite(numero, huesped, dias, precio, jacuzzi)
                    print(registrar_habitacion(hab.get_numero(),hab))
                case "L":
                    descuento=int(input("Indica la cantidad de descuento: "))
                    hab=HabitacionLargaEstancia(numero, huesped, dias, precio, descuento)
                    print(registrar_habitacion(hab.get_numero(),hab))
                case __:
                    print("Opción incorrecta")
        case 2:
            print(f"Has escogido: {opcion_menu[opcion-1]}")
            mostrar_habitaciones()
        case 3:
            print(f"Has escogido: {opcion_menu[opcion-1]}")
            num=int(input("Indica el número de la habitación: "))
            print(calcular_precio_final(num))
        case 4:
            print(f"Has escogido: {opcion_menu[opcion-1]}")
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción incorrecta, pulsa del 1 al 4")