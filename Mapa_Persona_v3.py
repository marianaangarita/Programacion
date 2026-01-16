import random

max_tablero=5
min_tablero=0


class Persona():
    def __init__(self,altura,nombre,resistencia,posX,posY):
        self.altura=altura
        self.nombre=nombre
        self.resistencia=resistencia
        self.posX=posX
        self.posY=posY
        self.salir=False
        print(f"(Personaje creado, nombre: {self.nombre} Posición: X: {self.posX}, Y:{self.posY}). Resistencia= {self.resistencia}")

    def mostrarPosicion(self):
        if self.resistencia>0:
            if self.posX==0 and self.posY==0:
                self.resistencia=self.resistencia+10
        else:
            self.salir=True
            print("GAME OVER, te has quedado sin resistencia.")
            return self.salir
        print(f"(X: {self.posX}, Y:{self.posY}). Resistencia= {self.resistencia}")

    def arriba(self):
        if self.resistencia>0:
            if self.posY>max_tablero:
                print("No puedes subir más, has llegado al límite del tablero.")
            else:
                self.posY=self.posY+1
                self.resistencia=self.resistencia-1
                self.mostrarPosicion()
        else:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
    
    def abajo(self):
        if self.resistencia>0:
            if self.posY<min_tablero:
                print("No puedes bajar más, has llegado al límite del tablero.")
            else:
                self.posY=self.posY-1
                self.resistencia=self.resistencia-1
                self.mostrarPosicion()
        else:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
    
    def izquierda(self):
        if self.resistencia>0:
            if self.posX<min_tablero:
                print("No puedes ir más a la izquierda, has llegado al límite del tablero.")
            else:
                self.posX=self.posX-1
                self.resistencia=self.resistencia-1
                self.mostrarPosicion()
        else:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
        
    def derecha(self):
        if self.resistencia>0:
            if self.posX>max_tablero:
                print("No puedes ir más a la derecha, has llegado al límite del tablero.")
            else:
                self.posX=self.posX+1
                self.resistencia=self.resistencia-1
                self.mostrarPosicion()
        else:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
    
    def teletransporte(self,x,y):
        if self.resistencia>5:
            if self.posX>max_tablero or self.posX<min_tablero or self.posY<min_tablero or self.posY>max_tablero:
                print("No te puedes desplazar fuera del tablero")
            else:
                self.posX=x
                self.posY=y
                self.resistencia=self.resistencia-5
                self.mostrarPosicion()
        if self.resistencia<=5:
            print("No tienes resistencia suficiente para usar el teletransporte.")
        if self.resistencia<=0:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
        
    def verificarEncuentro(self, enemigo):
        if self.resistencia>0:
            if self.posX==enemigo.posX and self.posY==enemigo.posY:
                self.resistencia=self.resistencia-5
                print(f"Has encontrado a {enemigo.nombre}")
                self.salir=True
                return self.salir
        
            
p=Persona(1.80,"Carlos", 10,0,0)

enemigo=Persona(1.5,"Drácula",10,random.randint(0,5), random.randint(0,5))

menu_opciones={"w": "Mover arriba", "s": "Mover abajo", "a": "Mover izquierda", "d": "Mover derecha"}

def menu():
    for clave, valor in menu_opciones.items:
        print(f"Pulsa {clave}:{valor}")


while not salir:
    menu()
    opcion=input("Escoge una opción: ").lower()

    match opcion:
        case "w":
            p.arriba()
            p.verificarEncuentro(enemigo)
        case "s":
            p.abajo()
            p.verificarEncuentro(enemigo)
        case "a":
            p.izquierda()
            p.verificarEncuentro(enemigo)
        case "d":
            p.derecha()
            p.verificarEncuentro(enemigo)
        case other:
            salir=True
            print("GAME OVER, tecla errónea")