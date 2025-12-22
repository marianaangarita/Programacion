'''
Actividad 05. Clase Coche

Crea una clase llamada Coche que tenga los siguientes atributos:
marca: una cadena de caracteres
modelo: una cadena de caracteres
potencia: un número entero
color: una cadena de caracteres
matriculacion: número entero
siguiente_revision: número entero
Define también los siguientes métodos:
mostrar(): muestra los datos del coche
acelerar(): incrementa la potencia del coche en 10 caballos
frenar(): decrementa la potencia del coche en 10 caballos
itv(): devuelve la fecha de la siguiente revisión teniendo en cuenta que se pasa la primera vez a los 4 años, después 2 años, otros 2 años y finalmente cada 1 año.
'''


class Coche():
    marca=""
    modelo=""
    potencia=""
    color=""
    matriculacion=""
    siguiente_revision=""

    def __init__(self,mar,mo,po,co,ma,si):
        self.marca=mar
        self.modelo=mo
        self.potencia=po
        self.color=co
        self.matriculacion=ma
        self.siguiente_revision=si

    def mostrar(self):
        return (f"Marca:{self.marca}, Modelo:{self.modelo}, Potencia:{self.potencia}CV, Color:{self.color}, Matriculación: {self.matriculacion}, Siguiente revisión: {self.siguiente_revision} año")
    
    def acelerar(self):
        return self.potencia = self.potencia +10
    
    def frenar(self):
        return self.potencia = potencia-10
    
    def itv(self):
        if 2025==self.matriculacion:
            self.siguiente_revision=4
        if 2029<self.matriculacion<=2033:
            self.siguiente_revision=2
        if self.matriculacion>2033:
            self.siguiente_revision=1
        return self.siguiente_revision


coche1=Coche("Renault","Clio", 2025,"Azul",3)
