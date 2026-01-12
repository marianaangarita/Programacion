import random

class Persona():
    def __init__(self,altura,nombre,resistencia,posX,posY):
        self.altura=altura
        self.nombre=nombre
        self.resistencia=resistencia
        self.posX=posX
        self.posY=posY

    def mostrarPos(self):
        if self.posX==0 and self.posY==0:
            self.resistencia=self.resistencia+10
        print(f"(X: {self.posX}, Y:{self.posY}). Resistencia= {self.resistencia}")

    def arriba(self):
        if self.resistencia>0:
            if self.posY>=5:
                print("No puedes subir más, has llegado al límite del tablero.")
            else:
                self.posY=self.posY+1
                self.resistencia=self.resistencia-1
                self.mostrarPos()

    def abajo(self):
        if self.resistencia>0:
            if self.posY<=0:
                print("No puedes bajar más, has llegado al límite del tablero.")
            else:
                self.posY=self.posY-1
                self.resistencia=self.resistencia-1
                self.mostrarPos()

    def izquierda(self):
        if self.resistencia>0:
            if self.posX<=0:
                print("No puedes ir más a la izquierda, has llegado al límite del tablero.")
            else:
                self.posX=self.posX-1
                self.resistencia=self.resistencia-1
                self.mostrarPos()

    def derecha(self):
        if self.resistencia>0:
            if self.posX>=5:
                print("No puedes ir más a la derecha, has llegado al límite del tablero.")
            else:
                self.posX=self.posX+1
                self.resistencia=self.resistencia-1
                self.mostrarPos()

    def teletransporte(self,x,y):
        if self.resistencia>5:
            if self.posX>=5 or self.posX<=0 or self.posY<=0 or self.posY>=5:
                print("No te puedes desplazar fuera del tablero")
            else:
                self.posX=x
                self.posY=y
                self.resistencia=self.resistencia-5
                self.mostrarPos()
        

salir=False

p=Persona(1.80,"Mariana", 10,0,0)
p.mostrarPos()

enemigo=Persona(1.5,"Drácula",10,random.randint(0,5), random.randint(0,5))

opciones=["ARRIBA","ABAJO","IZQUIERDA","DERECHA","TELETRANSPORTE", "SALIR"]

def menu():
    print("************************")
    print("MENÚ PRINCIPAL")
    for indice, opcion in enumerate(opciones,1):
        print(f"Pulsa {indice}: {opcion}")
    print("************************")

while not salir:
    menu()

    eleccion=int(input("Escoge una opción: "))

    match eleccion:
        case 1:
            p.arriba()
        case 2:
            p.abajo()
        case 3:
            p.izquierda()
        case 4:
            p.derecha()
        case 5:
            x=int(input("Escoge la nueva posición X"))
            y=int(input("Escoge la nueva posición Y"))
            p.teletransporte(x,y)
        case 6:
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta, pulsa del 1 al 5.")
