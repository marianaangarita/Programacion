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
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Potencia: {self.potencia} CV, Color: {self.color}, Matriculación: {self.matriculacion}, Siguiente revisión: {self.siguiente_revision} ")
    
    def acelerar(self):
        self.potencia = self.potencia + 10
        return(f"Potencia aumentada a {self.potencia} CV")
    
    def frenar(self):
        self.potencia = self.potencia-10
        return(f"Potencia descelerada a {self.potencia} CV")
    
    def itv(self):
        año_actual=2025
        año_desde_matricualcion=año_actual-self.matriculacion

        if año_desde_matricualcion<=4:
            self.siguiente_revision= self.matriculacion + 4

        elif 4<año_desde_matricualcion<=8:
            self.siguiente_revision= año_actual + 2 

        elif año_desde_matricualcion>8:
            self.siguiente_revision= año_actual + 1

        return self.siguiente_revision


coche1=Coche("Renault","Clio", 150,"Azul", 2024, 2026)

print(coche1.mostrar())

print(coche1.acelerar())

print(coche1.itv())

print(coche1.mostrar())