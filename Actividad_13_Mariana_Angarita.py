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
        Velocidad_final=self.velocidad+(a*1)
        return(f"La velocidad final del vehículo es {Velocidad_final} m/s")
    
class Coche(Vehiculo):
    def __init__(self, ruedas, puertas):
        super().__init__(ruedas)
        self.puertas=puertas
    def acelerar(self,a):
        Velocidad_final=self.velocidad+(a*1)
        return(f"La velocidad final del coche es {Velocidad_final} m/s")
    
class Bicicleta(Vehiculo):
    def __init__(self, ruedas, tipo):
        super().__init__(ruedas)
        self.tipo=tipo
    def acelerar(self,a):
        Velocidad_final=self.velocidad+(a*1)
        return(f"La velocidad final de la bicicleta es {Velocidad_final} m/s")
    
coche = Coche(ruedas=4, puertas=4)
bicicleta = Bicicleta(ruedas=2, tipo="Montaña")
print(coche.acelerar(30))
print(bicicleta.acelerar(15))