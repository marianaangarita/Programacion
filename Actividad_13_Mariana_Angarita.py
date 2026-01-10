'''
Actividad 13: Vehículos
Crea una clase base llamada Vehiculo que tenga los atributos comunes a todos los vehículos, como el número de ruedas y la velocidad actual. Incluye un método para acelerar.
Luego crea una clase derivada llamada Coche que herede de Vehiculo. Agrega un atributo adicional para el número de puertas. Sobrescribe el método de acelerar para imprimir un mensaje específico para un coche.
Finalmente crea una clase derivada llamada Bicicleta que herede de Vehiculo. Agrega un atributo adicional para el tipo de bicicleta (montaña, carretera, etc.). Sobrescribe el método de acelerar para imprimir un mensaje específico para una bicicleta.

Ejemplo de ejecución y salida.
coche = Coche(ruedas=4, puertas=4)
bicicleta = Bicicleta(ruedas=2, tipo="Montaña")

coche.acelerar(30)
bicicleta.acelerar(15)
'''

class Vehiculo():
    def __init__(self, ruedas):
        self.ruedas=ruedas
        self.velocidad=0
    def acelerar(self,a):
        self.velocidad=self.velocidad+(a*1)
        print(f"La velocidad final del vehículo es {self.velocidad} m/s")
    
class Coche(Vehiculo):
    def __init__(self, ruedas, puertas):
        super().__init__(ruedas)
        self.puertas=puertas
    def acelerar(self,a):
        self.velocidad=self.velocidad+(a*1)
        print(f"La velocidad final del coche es {self.velocidad} m/s")
    def info(self):
        return (f" El coche tiene {self.ruedas} ruedas, y tiene una velocidad de {self.velocidad} m/s.")
    
class Bicicleta(Vehiculo):
    def __init__(self, ruedas, tipo):
        super().__init__(ruedas)
        self.tipo=tipo
    def acelerar(self,a):
        self.velocidad=self.velocidad+(a*1)
        print(f"La velocidad final de la bicicleta es {self.velocidad} m/s")
    def info(self):
        return (f" La bicicleta tiene {self.ruedas} ruedas, es de tipo {self.tipo}, y tiene una velocidad de {self.velocidad} m/s.")
    
coche = Coche(ruedas=4, puertas=4)
bicicleta = Bicicleta(ruedas=2, tipo="Montaña")
coche.acelerar(30)
bicicleta.acelerar(15)
print(bicicleta.info())
print(coche.info())