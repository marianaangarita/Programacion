import random

cas_min=0
cas_max=5

class Planta():
    def __init__(self,nombre):
        self.posX=random.randint(cas_min,cas_max)
        self.posY=random.randint(cas_min,cas_max)
        self.nombre=nombre
        self.venenosa=False

class Planta_Venenosa(Planta):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.venenosa=True
    

class Animal():
    def __init__(self):
        self.posX=random.randint(cas_min,cas_max)
        self.posY=random.randint(cas_min,cas_max)
        self.vida=True

    def mostrar_pos(self):
        return (f"El animal está: {self.posX} X: {self.posY} Y")
    
    def mover_derecha(self):
        if self.posX>=cas_min and self.posX<=cas_max:
            self.posX=self.posX+1
            return self.mostrar_pos()
        else:
            return(f"No puedes desplazarte más allá del tablero")
    
    def mover_izquierda(self):
        if self.posX>=cas_min and self.posX<=cas_max:
            self.posX=self.posX-1
            return self.mostrar_pos()
        else:
            return(f"No puedes desplazarte más allá del tablero")
        
    def mover_arriba(self):
        if self.posY>=cas_min and self.posY<=cas_max:
            self.posY=self.poY+1
            return self.mostrar_pos()
        else:
            return(f"No puedes desplazarte más allá del tablero")
        
    def mover_abajo(self):
        if self.posY>=cas_min and self.posY<=cas_max:
            self.posY=self.posY-1
            return self.mostrar_pos()
        else:
            return(f"No puedes desplazarte más allá del tablero")
 
            
class Bosque():
    def __init__(self):
        self.tablero=[]
        self.opciones=["P","A","V","_"]

    def agregar_planta(self, planta):
        self.tablero.append(planta)
        return (f"Se ha agregado a la lista: {planta.nombre}")

    def crear_bosque(self):
        for i in range(cas_max):
            fila=[]
            for _ in range(cas_max):
                fila.append(random.choice(self.opciones))
            self.tablero.append(fila)
        return self.tablero
    
    def print_bosque(self):
        for fila in self.tablero:
            print(f"{fila}\n")

bosque=Bosque()
bosque.crear_bosque()
bosque.print_bosque()