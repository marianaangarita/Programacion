'''
Actividad 01. Clase persona
Crea una clase llamada Persona que tenga los siguientes atributos:
Nombre
Apellidos
Edad
Sexo
La clase debe tener un constructor que inicialice los atributos con los valores que se pasen como parámetros.
'''

class Persona():
    

    def __init__(self,n,a,e,s):
        self.nombre=n
        self.apellidos=a
        self.edad=e
        self.sexo=s


persona1=Persona("María","Salvá",27,"Mujer")

print(persona1.nombre)