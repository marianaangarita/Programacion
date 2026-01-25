'''
Contexto
Una empresa de alquiler de vehículos necesita un sistema para gestionar su flota. La aplicación debe aplicar los principios de la Programación Orientada a Objetos, herencia y encapsulación.

Requisitos del Programa
1. Clase Base: Vehiculo (Abstracción y Encapsulación)
Crea una clase llamada Vehiculo que represente cualquier medio de transporte de la empresa.

Atributos:

marca (string)

modelo (string)

matricula (string, debe ser único conceptualmente)

alquilado (bool, inicialmente False)

Métodos:

__init__: Inicializa todos los atributos.

Getters y Setters: Para los atributos que consideres necesarios.

alquilar(): Cambia el estado a alquilado. Si ya está alquilado, debe indicarlo.

devolver(): Cambia el estado a disponible.

mostrar_info(): Devuelve una cadena con el formato: "Vehículo: [Marca] [Modelo] | Matrícula: [Matricula] | Estado: [Alquilado/Disponible]".

2. Herencia Simple: Clases Coche y Moto
Crea dos clases hijas que hereden de Vehiculo.

Clase Coche

Atributo adicional: num_puertas (int).

Métodos: Sobrescribe mostrar_info() para incluir el número de puertas.

Clase Moto

Atributo adicional: cilindrada (int, cc).

Métodos: Sobrescribe mostrar_info() para incluir la cilindrada.

3. Clase de Gestión: Flota (Composición)
Crea una clase Flota que gestione la lista de vehículos.

Atributos: lista_vehiculos (lista vacía al inicio).

Métodos:

agregar_vehiculo(vehiculo): Añade un objeto a la lista.

mostrar_flota(): Recorre la lista y muestra la información de cada vehículo.

buscar_por_matricula(matricula): Busca un vehículo y muestra sus datos.

4. Menú Interactivo
El programa debe ejecutarse mediante un menú en consola (dentro de un while) que permita:

Crear y registrar un Coche.

Crear y registrar una Moto.

Mostrar toda la flota.

Alquilar un vehículo (buscando por matrícula).

Devolver un vehículo (buscando por matrícula).

Salir.
'''
class Vehiculo():
    def __init__(self, marca, modelo, matricula):
        self.marca=marca
        self.modelo=modelo
        self.matricula=matricula
        self.alquilado=False
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def get_matricula(self):
        return self.matricula
    
    def get_alquilado(self):
        return self.alquilado
    
    def set_marca(self, marca):
        self.marca=marca

    def set_modelo(self, modelo):
        self.modelo=modelo

    def set_matricula(self, matricula):
        self.matricula=matricula

    def set_alquilado(self, alquilado):
        self.alquilado=alquilado

    def alquilar(self):
        if self.get_alquilado()==False:
            self.set_alquilado(True)
            return (f"Se ha alquilado el vehículo con matrícula: {self.get_matricula()}")
        else:
            return(f"El vehículo con matricula: {self.get_matricula()}, ya estaba alquilado.")

    def devolver(self):
        if self.get_alquilado()==True:
            self.set_alquilado(False)
            return(f"Se ha devuelto el vehículo con matrícula: {self.get_matricula()}")
        else:
            return(f"El vehículo con matrícula: {self.get_matricula()}, no estaba alquilado.")
    
    def mostrar_info(self):
        estado=""
        if self.get_alquilado()==True:
            estado="Alquilado"
        else:
            estado="Disponible"   
        return(f"Vehículo: {self.get_marca()} {self.get_modelo()} | Matrícula: {self.get_matricula()} | Estado: {estado}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, matricula, puertas):
        super().__init__(marca, modelo, matricula)
        self.num_puertas=puertas
    
    def get_num_puertas(self):
        return self.num_puertas
    
    def set_num_puertas(self, p):
        self.num_puertas=p

    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Número de puertas: {self.get_num_puertas()}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, matricula, cilindrada):
        super().__init__(marca, modelo, matricula)
        self.cilindrada=cilindrada
    
    def get_cilindrada(self):
        return self.cilindrada
    
    def set_cilindrada(self, p):
        self.cilindrada=p
    
    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Cilindrada: {self.get_cilindrada()} cc")

class Flota():
    def __init__(self):
        self.lista_vehiculos=[]
    
    def agregar_vehiculo(self, vehiculo):
        existe=False
        for i in self.lista_vehiculos:
            if i.get_matricula()==vehiculo.get_matricula():
                existe=True
                return(f"El vehiculo con matrícula: {vehiculo.get_matricula()} ya estaba en la lista.")
        if existe==False:
            self.lista_vehiculos.append(vehiculo)
            return (f"Se ha agregado a la lista el vehículo con matrícula: {vehiculo.get_matricula()}.")
    
    def mostrar_flota(self):
        for i in self.lista_vehiculos:
            print(i.mostrar_info())
        
    
    def buscar_por_matricula(self, matricula):
        existe=False
        for i in self.lista_vehiculos:
            if i.get_matricula()==matricula:
                existe=True
                return(i.mostrar_info())
        if existe==False:
            return(f"El vehículo con matrícula: {matricula}, no está en la lista.")

            
        
salir=False
vehiculo=None
flota=Flota()
lista_menu=["CREAR Y REGISTAR COCHE", "CREAR Y REGISTRAR MOTO", "MOSTRAR FLOTA", "ALQUILAR VEHÍCULO", "DEVOLVER VEHÍCULO", "BUSCAR MATRÍCULA", "SALIR"]

def menu():
    print("***************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(lista_menu, 1):
        print(f"Pulsa {clave}: {valor}")
    print("***************************")

while not salir:
    menu()

    opcion=int(input("Escoge una opción: "))

    match opcion:
        case 1:
            print(f"Has elegido: {lista_menu[opcion-1]}")

            marca=input("Indica la marca del coche: ").lower()
            modelo=input("Indica el modelo: ").lower()
            matricula=input("Indica la matrícula: ").lower()
            puertas=int(input("Indica el número de puertas: "))
            if puertas>0:
                vehiculo=Coche(marca, modelo, matricula, puertas)
                print(flota.agregar_vehiculo(vehiculo))
            else:
                print("Datos incorrectos, no puedes poner puertas 0 o negativas.")

        case 2:
            print(f"Has elegido: {lista_menu[opcion-1]}")

            marca=input("Indica la marca de la moto: ").lower()
            modelo=input("Indica el modelo: ").lower()
            matricula=input("Indica la matrícula: ").lower()
            cilindrada=int(input("Indica la cilindrada: "))

            if cilindrada>0:
                vehiculo=Moto(marca, modelo, matricula, cilindrada)
                print(flota.agregar_vehiculo(vehiculo))
            else:
                print("Datos incorrectos, no puedes poner cilindradas 0 o negativas.")

        case 3:
            print(f"Has elegido: {lista_menu[opcion-1]}")
            if flota.lista_vehiculos:
                flota.mostrar_flota()
            else:
                print("Lista vacía, debes agregar primero un vehículo  a la lista.")

        case 4:
            print(f"Has elegido: {lista_menu[opcion-1]}")
            matricula=input("Indica la matrícula: ").lower()
            existe=False
            if flota.lista_vehiculos:
                for i in flota.lista_vehiculos:
                    if i.get_matricula()==matricula:
                        existe=True
                        print(i.alquilar())
                        break
                if existe==False:
                    print(f"El vehículo con matricula: {matricula}, no está en la lista.")
            else:
                print("Lista vacía, agrega un vehículo para poder usar esta opción.")

        case 5:
            print(f"Has elegido: {lista_menu[opcion-1]}")
            matricula=input("Indica la matrícula: ").lower()
            existe=False
            if flota.lista_vehiculos:
                for i in flota.lista_vehiculos:
                    if i.get_matricula()==matricula:
                        existe=True
                        print(i.devolver())
                        break
                if existe==False:
                    print(f"El vehículo con matrícula: {matricula}, no está en la lista.")
            else:
                print("Lista vacía, agrega un vehículo para poder usar esta opción.")

        case 6:
            print(f"Has elegido: {lista_menu[opcion-1]}")

            matricula=input("Indica la matrícula: ").lower()
            if flota.lista_vehiculos:
                print(flota.buscar_por_matricula(matricula))
            else:
                print("Lista vacía, debes agregar primero un vehículo a la lista.")
        case 7:
            print(f"Has elegido: {lista_menu[opcion-1]}")
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta. Pulsa del 1 al 6.")