'''
Contexto: Programar un robot aspiradora (Roomba) que se mueve en una habitación de 5x5 (coordenadas 0 a 4).

Clase Robot:

Atributos:

nombre

bateria: Empieza en 100.

bolsa_basura: Empieza en 0 (capacidad máxima 10).

pos_x, pos_y: Empieza en (0,0).

Método mostrar_estado(): Imprime posición, batería restante y cuánto ha llenado la bolsa.

Movimiento:

Métodos moverse(direccion) ("norte", "sur", "este", "oeste").

Reglas:

Gasta 5 de batería por movimiento.

No puede salir del mapa (0-4).

Si la batería es 0, Game Over.

Acción Especial: limpiar()

Solo se puede hacer si hay batería. Gasta 10 de batería.

Aumenta bolsa_basura en 2 puntos.

Regla crítica: Si bolsa_basura llega a 10, el robot se detiene y dice "Depósito lleno, vuelva a la base". No puede moverse ni limpiar hasta vaciarlo.

Acción Especial: vaciar_deposito()

Solo funciona si está en la casilla (0,0) (la base de carga).

Pone bolsa_basura a 0 y recarga la bateria al 100%.

Tu Misión:

Genera "manchas de suciedad" aleatorias (o fijas) en el mapa (puedes usar una lista de tuplas ej: [(1,2), (3,3)]).

Haz un bucle while que pida al usuario qué hacer (moverse, limpiar, salir).

Si limpia donde hay una "mancha", elimínala de la lista y felicita al usuario.
'''
import random
salir=False
min_tablero=0
max_tablero=4
class Robot():
    def __init__(self, nombre):
        self.nombre=nombre
        self.bateria=100
        self.bolsa_basura=0
        self.posX=0
        self.posY=0
        (f"La roomba {self.nombre}, se encuentra en la posicion: {self.posX}: X, {self.posY}: Y, batería: {self.bateria}, bolsa de basura: {self.bolsa_basura}")

    def mostrar_estado(self):
        if lista_mancha:
            for m in lista_mancha:
                if m.limpiar_mancha(self):
                    self.limpiar()
                    lista_mancha.remove(m)
                    break
        return(f"La roomba {self.nombre}, se encuentra en la posicion: {self.posX}: X, {self.posY}: Y, batería: {self.bateria}, bolsa de basura: {self.bolsa_basura}")
    
    def mover_norte(self):
        if self.posY>=max_tablero:
            return("No puedes subir más al norte.")
        else:
            self.posY=self.posY+1
            self.bateria=self.bateria-5
            self.mostrar_estado()

    def mover_sur(self):
        if self.posY<=min_tablero:
            return("No puedes bajar más al sur.") 
        else: 
            self.posY=self.posY-1
            self.bateria=self.bateria-5
            self.mostrar_estado()

    def mover_este(self):
        if self.posX>=max_tablero:
            return("No puedes ir más al este.") 
        else:
            self.posX=self.posX+1
            self.bateria=self.bateria-5
            self.mostrar_estado()

    def mover_oeste(self):
        if self.posX<=min_tablero:
            return("No puedes ir más al oeste.") 
        else:
            self.posX=self.posX-1
            self.bateria=self.bateria-5
            self.mostrar_estado()

    def limpiar(self):
        if self.bateria>10:
            self.bateria=self.bateria-10
            self.bolsa_basura=self.bolsa_basura+2
            self.mostrar_estado()
            if self.bolsa_basura>=10:
                print("Depósito lleno, vuelva a la base.")

        elif self.bateria<=10:
            print("No tienes suficiente batería para limpiar.")

    def vaciar_deposito(self):
        if self.posX==0 and self.posY==0:
            self.bolsa_basura=0
            self.bateria=100
            self.mostrar_estado()
        else:
            print("No puedes vaciar el depósito.")

class Manchas():
    def __init__(self, nombre):
        self.nombre=nombre
        self.posX=random.randint(0,4)
        self.posY=random.randint(0,4)
        (f"La mancha {self.nombre}, se encuentra en la posicion: {self.posX}: X, {self.posY}: Y")
    
    def limpiar_mancha(self, rumba):
        if self.posX==rumba.posX and self.posY==rumba.posY:
            print(f"¡Has encontrado la mancha {self.nombre}!")
            return True            
            
        
mancha_1=Manchas("mancha_1")

mancha_2=Manchas("mancha_2")

mancha_3=Manchas("mancha_3")

lista_mancha=[mancha_1, mancha_2, mancha_3]