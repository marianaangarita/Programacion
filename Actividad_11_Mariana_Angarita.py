'''
Actividad 11. Herencia múltiple
Crea una clase Persona con atributos como nombre y edad. Luego, crea una clase Empleado que herede de Persona y tenga un atributo adicional para el salario.
Comprueba su funcionamiento imprimiendo los atributos de un empleado.

Ejemplo de ejecución y salida.
empleado1 = Empleado("Juan", 30, 50000)
print(empleado1.nombre, empleado1.edad, empleado1.salario)

'''
class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario=salario

empleado1 = Empleado("Juan", 30, 50000)
print(empleado1.nombre, empleado1.edad, empleado1.salario)