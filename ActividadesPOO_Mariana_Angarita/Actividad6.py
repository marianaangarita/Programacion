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
from datetime import datetime

class Coche():
 
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
       
    
    def frenar(self):
        self.potencia = self.potencia-10

    
    def itv(self):
        año_actual=datetime.now().year

        antiguedad=año_actual-self.matriculacion

        if antiguedad<4:
            self.siguiente_revision= self.matriculacion + 4

        elif 4<=antiguedad<6:
            self.siguiente_revision= self.matriculacion + 6
        elif 6<=antiguedad<8:
            self.siguiente_revision= self.matriculacion + 8
        elif antiguedad>=8:
            self.siguiente_revision= año_actual + 1

        return self.siguiente_revision
    
def mostrarCoches(lista):
    for i in lista:
        print(i.mostrar())

lista_coches=[]

salir=False

opciones=["CREAR OBJETO", "FRENAR", "ACELERAR", "MOSTRAR", "SALIR"]

def menu_principal():
    print("***************")
    print("Menú Principal")
    for indice,valor in enumerate (opciones,1):
        print(f"Pulsa {indice}: {valor}")
    print("***************")

def modificar_coche():
    for indice, valor in enumerate (lista_coches):
        print(f"Pulsa {indice}: {valor.mostrar()}")
    
    


while not salir:


    menu_principal()
    programa=int(input("Elige una de las siguientes opciones: "))

    match programa:

        case 1:

            m=input("¿Qué marca es el coche?: ").lower()
            mo=input("¿Qué modelo es el coche?: ").lower()
            po=int(input("¿Cuánta potencia tiene el coche?: "))
            co=input("¿De qué color es el coche?: ").lower()
            ma=int(input("¿Cuándo fue el año de matriculación del coche?: "))
            s=0
        
            cochecito=Coche(m,mo,po,co,ma,s)
            cochecito.itv()
            lista_coches.append(cochecito)
    
        case 2:
            if len(lista_coches)>0:
                modificar_coche()
                coche_elegido=int(input("¿Qué coche quieres modificar?: "))
                lista_coches[coche_elegido].frenar()
                print("Has reducido los caballos del coche")
            else:
                print("Lista vacía, primero selecciona la opción 1")

        case 3:
            if len(lista_coches)>0:
                modificar_coche()
                coche_elegido=int(input("¿Qué coche quieres modificar?"))
                lista_coches[coche_elegido].acelerar()
                print("Has aumentado los caballos del coche")
            else:
               print("Lista vacía, primero selecciona la opción 1") 

        case 4:
            if len(lista_coches)>0:
                mostrarCoches(lista_coches)  
            else:
              print("Lista vacía, primero selecciona la opción 1")   

        case 5:
            salir=True
            print("Has salido del programa")
        
        case other:
            print("Opción incorrecta")
        

    
        


    
