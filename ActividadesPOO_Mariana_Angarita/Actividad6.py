'''
Actividad 06. Lista de coches
Crea un programa que cree una lista de coches. Cada coche debe tener los siguientes datos:
marca
modelo
potencia
color
matriculacion: número entero
siguiente_revision: número entero
Define también los siguientes métodos:          
mostrar(): muestra los datos del coche
acelerar(): incrementa la potencia del coche en 10 caballos
frenar(): decrementa la potencia del coche en 10 caballos
itv(): devuelve la fecha de la siguiente revisión teniendo en cuenta que se pasa la primera vez a los 4 años, después 2 años, otros 2 años y finalmente cada 1 año.


El programa debe pedir los datos de cada coche al usuario y luego mostrarlos.
'''

class Coche():
    marca=""
    modelo=""
    potencia=""
    color=""
    matriculacion=""
    siguiente_revision=""

    def __init__(self,m,mo,po,co,ma,s):
        self.marca=m
        self.modelo=mo
        self.potencia=po
        self.color=co
        self.matriculacion=ma
        self.siguiente_revision=s
    
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
    

m=input("¿Qué marca es el coche?: ").lower()
mo=input("¿Qué modelo es el coche?: ").lower()
po=int(input("¿Cuánta potencia tiene el coche?: "))
co=input("¿De qué color es el coche?: ").lower()
ma=int(input("¿Cuándo fue el año de matriculación del coche?: "))
s=int(input("¿Cuál es la fecha de la siguiente revisión?: "))


coche1=Coche(m,mo,po,co,ma,s)

coche2=Coche(m,mo,po,co,ma,s)

coche3=Coche(m,mo,po,co,ma,s)