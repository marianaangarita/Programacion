'''
Actividad 02. Clase Rectángulo
Crea una clase llamada Rectángulo que tenga los siguientes atributos:
Base
Altura
La clase debe tener un constructor que inicialice los atributos con los valores que se pasen como parámetros.

La clase debe tener un método llamado calcular_área() que calcule el área del rectángulo y lo devuelva.

'''

class Rectangulo():

    def __init__(self, b, a):
        self.base=b
        self.altura=a
        
    def calcular_area(self):
        return (f"Área={self.base*self.altura}")

rectangulo1=Rectangulo(10,5)

print(rectangulo1.calcular_area())