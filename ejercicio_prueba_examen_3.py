'''
Parte 1: La Abstracción (El Contrato)
Debes crear una clase base llamada Vehiculo.

Requisito "Difícil": Debe ser una Clase Abstracta (usa from abc import ABC, abstractmethod).

Atributos: matricula, modelo, precio_base_dia, alquilado (booleano, por defecto False).

Métodos Concretos:

__init__: Constructor estándar.

mostrar_info(): Muestra los datos básicos.

Método Abstracto:

calcular_alquiler(dias): Obliga a las hijas a definir cómo calculan el precio final.

Parte 2: Las Clases Hijas (La Lógica Específica)
Crea tres clases que hereden de Vehiculo. Cada una calcula el precio de forma distinta (Polimorfismo):

CocheLujo:

Atributo extra: caballos (potencia).

calcular_alquiler: (Precio base + 10€) * días. Además, si tiene más de 300 caballos, suma un extra único de 50€ al total.

FurgonetaCarga:

Atributo extra: kg_capacidad.

calcular_alquiler: (Precio base * días) + (0.5€ por cada kg de capacidad).

CocheElectrico:

calcular_alquiler: Precio base * días. Pero tiene un descuento del 30% sobre el total por ser ecológico.

Parte 3: La Clase Gestora (El Cerebro)
Crea una clase Flota.

Atributo: lista_vehiculos (una lista vacía al inicio).

Métodos:

agregar_vehiculo(vehiculo): Añade un objeto a la lista.

alquilar_vehiculo(matricula): Busca el vehículo por matrícula.

Si no existe: Error.

Si ya está alquilado: Dice "Ya ocupado".

Si está libre: Cambia alquilado a True e imprime confirmación.

El Reto Final: calcular_ingresos_potenciales(dias): Recorre toda la lista de vehículos (sean coches, furgonetas, etc.) y suma cuánto dinero ganaríamos si alquiláramos todos durante ese número de días.
'''

import abc

class Vehiculo(metaclass=abc.ABCMeta):
    def __init__(self, matricula, modelo, precio):
        self.matricula=matricula
        self.modelo=modelo
        self.precio_base=precio
        self.alquilado=False

    def info(self):
        return(f"El vehículo con matrícula: {self.matricula}, modelo: {self.modelo}, y precio base: {self.precio_base}")
    
    @abc.abstractmethod
    def calcular_alquiler(self, dias):
        pass

class CocheLujo(Vehiculo):
    def __init__(self, matricula, modelo, precio, caballos):
        super().__init__(matricula, modelo, precio)
        self.caballos=caballos
    
    def calcular_alquiler(self, dias):
        if self.caballos<=300:

            alquiler=(self.precio_base + 10)*dias
        else:
            alquiler=((self.precio_base + 10)*dias)+50

        return alquiler
class FurgonetaCarga(Vehiculo):
    def __init__(self, matricula, modelo, precio, capacidad):
        super().__init__(matricula, modelo, precio)
        self.capacidad=capacidad
    
    def calcular_alquiler(self, dias):
        alquiler=(self.precio_base*dias)+(0.5*self.capacidad)
        return alquiler
    
class CocheElectrico(Vehiculo):
    def __init__(self, matricula, modelo, precio):
        super().__init__(matricula, modelo, precio)

    def calcular_alquiler(self, dias):
        descuento=(self.precio_base*dias)*0.3
        alquiler=(self.precio_base*dias)-descuento
        return alquiler
         
class Flota():
    def __init__(self):
        self.lista_vehiculos=[]
    
    def agregar_vehiculo(self, vehiculo):
        if vehiculo in self.lista_vehiculos:
            return(f"El vehículo {vehiculo}, ya está en la lista.")
        else:
            self.lista_vehiculos.append(vehiculo)
            return (f"Se ha agregado a la lista el vehiculo {vehiculo}")

    def alquilar_vehiculo(self, matricula):
        if not matricula in self.lista_vehiculos:
            return(f"El vehículo con matrícula {matricula}, no se encuentra en la base de datos.")
        
        if matricula.alquilado==True:
            return(f"El vehículo con matrícula {matricula}, ya está ocupado.")
        
        if matricula.alquilado==False:
            matricula.alquilado=True
            return(f"Has alquilado el vehículo con matrícula {matricula}.")



