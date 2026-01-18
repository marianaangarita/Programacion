import random

max_tablero=5
min_tablero=0

class Pocion():
    def __init__(self, nombre):
        self.nombre=nombre
        self.posX=random.randint(0,5)
        self.posY=random.randint(0,5)
        print(f"Poción {self.nombre} está en las coordenadas {self.posX} X:{self.posY} Y")

    def mismaPosicion(self, personaje):
        if self.posX==personaje.posX and self.posY==personaje.posY:
            print(f"Has obtenido la poción {self.nombre}")
            return True  
        
obj1=Pocion("Poción_1")
obj2=Pocion("Poción_2")
obj3=Pocion("Poción_3")

Pociones=[obj1, obj2, obj3]       

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

            if self.posX==5 and self.posY==5:
                self.salir=True
                print("Has llegado a la casilla de meta. HAS GANADO!!")
                return self.salir
            
            if self.posX==0 and self.posY==0:
                self.resistencia=self.resistencia+10
            if Pociones:
                for p in Pociones:
                    if p.mismaPosicion(self):
                        Pociones.remove(p)
                        self.resistencia=self.resistencia+10
                        break
                    
            
        else:
            self.salir=True
            print("GAME OVER, te has quedado sin resistencia.")
            return self.salir
        print(f"(X: {self.posX}, Y:{self.posY}). Resistencia= {self.resistencia}")

    def arriba(self):
        if self.resistencia>0:
            if self.posY>=max_tablero:
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
            if self.posY<=min_tablero:
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
            if self.posX<=min_tablero:
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
            if self.posX>=max_tablero:
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
            if x>max_tablero or x<min_tablero or y<min_tablero or y>max_tablero:
                print("No te puedes desplazar fuera del tablero")
            else:
                self.posX=x
                self.posY=y
                self.resistencia=self.resistencia-5
                self.mostrarPosicion()
        elif self.resistencia<=5:
            print("No tienes resistencia suficiente para usar el teletransporte.")
        if self.resistencia<=0:
            self.salir=True
            print("GAME OVER...te has quedado sin resistencia")
            return self.salir
        
    def verificarEncuentro(self, enemigo):
        if self.resistencia>0:
            if self.posX==enemigo.posX and self.posY==enemigo.posY:
                self.resistencia=self.resistencia-5
                print(f"Has encontrado a {enemigo.nombre}, has ganado.")
                self.salir=True
                return self.salir

      
            
p=Persona(1.80,"Carlos", 10,0,0)

enemigo=Persona(1.5,"Drácula",10,random.randint(0,5), random.randint(0,5))

menu_opciones={"w": "Mover arriba", "s": "Mover abajo", "a": "Mover izquierda", "d": "Mover derecha", "t":"Teletransporte"}

def menu():
    print("MENÚ PRIMCIPAL")
    print("*********************************")
    for clave, valor in menu_opciones.items():
        print(f"Pulsa {clave}:{valor}")
    print("*********************************")

while not p.salir:
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
        case "t":
            x=int(input("Escoge la coordenada x: "))
            y=int(input("Escoge la coordenada y: "))

            p.teletransporte(x,y)
            p.verificarEncuentro(enemigo)

        case other:
            p.salir=True
            print("GAME OVER, tecla errónea")