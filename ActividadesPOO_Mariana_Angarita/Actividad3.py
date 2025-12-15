'''
Actividad 03. Clase Círculo
Crea una clase llamada Círculo que tenga los siguientes atributos:
Radio
La clase debe tener un constructor que inicialice el atributo con el valor que se pase como parámetro.

La clase debe tener un método llamado calcular_área() y calcular_longitud() que calcule el área y la longitud del círculo y lo devuelva.
'''
class Circulo():

    def __init__(self,r):
        self.radio=r
    
    def calcular_area(self):
        return (f"Área={3.1416*(self.radio)**2}")
    
    def calcular_longitud(self):
        return (f"Longitud={2*3.1416*(self.radio)}")

circulo1=Circulo(4)

print(circulo1.calcular_area())

print(circulo1.calcular_longitud())