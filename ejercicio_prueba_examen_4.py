"""
Ejercicio 2: "Torneo de Gladiadores por Turnos"
Concepto: Este ejercicio refuerza la gestión de "saldos" (vida/maná) como en el banco, pero en un bucle de combate interactivo como el juego de rol, añadiendo la complejidad de un sistema de turnos.
Requisitos de las Clases:
1. Clase Gladiador (Base):
    ◦ Atributos: nombre, vida (100), energia (50).
    ◦ Métodos:
        ▪ atacar(objetivo): Resta energía (coste 10) y quita vida al objetivo (daño base 15). Si no hay energía, no ataca.
        ▪ descansar(): Recupera 20 de energía pero no ataca en ese turno.
        ▪ esta_vivo(): Devuelve True si la vida > 0.
2. Clase Mago (Subclase):
    ◦ Hereda de Gladiador. Añade atributo mana (100).
    ◦ Método curar(): Gasta 30 de maná para recuperar 20 de vida a sí mismo (similar al depósito bancario con interés).
    ◦ Sobrescribe atacar: Puede lanzar "Bola de fuego" que gasta maná en vez de energía y hace más daño (25).
3. Clase Guerrero (Subclase):
    ◦ Hereda de Gladiador. Añade atributo furia (0).
    ◦ Habilidad pasiva: Cada vez que recibe daño, su furia aumenta.
    ◦ Sobrescribe atacar: Si su furia es > 50, hace el doble de daño y la furia se reinicia.
Requisitos del Programa Principal (Bucle más complejo):
• Crea un objeto Jugador (elige clase Mago o Guerrero) y un Enemigo (asignado por la máquina).
• Bucle de Combate (while jugador.esta_vivo() and enemigo.esta_vivo()):
    ◦ Turno Jugador: Menú para elegir acción (Atacar, Curar/Habilidad, Descansar). Validar si tiene recursos (maná/energía) para hacerlo.
    ◦ Turno Enemigo: Lógica simple (si vida < 20 intenta curarse/descansar, si no, ataca) usando random para variar.
    ◦ Feedback: Imprimir en cada turno los "saldos" (Vida, Energía, Maná) de ambos, similar a consultar saldo en el banco.
    ◦ Al final, declara el ganador.

--------------------------------------------------------------------------------
Claves para aprobar (Basado en tus fuentes)
1. Validaciones de Estado: Tanto en el banco ("no puedes retirar más de lo que tienes") como en el movimiento ("no puedes moverte sin resistencia"), la clave es el uso de if dentro de los métodos antes de modificar los atributos.
    ◦ Ejemplo: if self.bateria >= costo: ... else: print("Batería insuficiente")
2. El Bucle Infinito y Salida: Recuerda la estructura del Paso 6 del movimiento 2D. Usa while True: para mantener el programa vivo y break o sys.exit() para condiciones de derrota/victoria.
3. Interacción entre Objetos: El examen será difícil porque los objetos interactúan.
    ◦ En el banco: Cuenta1.transferir(monto, Cuenta2).
    ◦ En el juego: verificarEncuentro(self, enemigo).
    ◦ Práctica: Asegúrate de saber pasar un objeto como parámetro a un método de otro objeto (ej. robot.atacar(otro_robot)).
4. Uso de super(): Si te piden herencia y constructores avanzados (como inicializar atributos extra en la subclase), usa super().__init__(...) para asegurar que la clase padre se inicializa bien.
¿Quieres que desarrolle el código solución de alguno de estos dos para que veas la implementación exacta?
"""
import random

class Gladiador():
    def __init__(self, nombre):
        self.nombre=nombre
        self.vida=100
        self.energia=50

    def atacar(self, objetivo):
        if self.energia>=10:
            self.energia=self.energia-10
            objetivo.vida=objetivo.vida-15
            return (f" Ahora tienes de energia: {self.energia}. Tu objetivo tiene de vida: {objetivo.vida}.")
        else:
            return(f"No tienes suficiente vida para atacar.")
        
    def descansar(self):
        self.energia=self.energia+20
        return (f"Ahora tienes de energia: {self.energia}")
    
    def esta_vivo(self):
        if self.vida>0:
            return True
        else:
            return False
        
class Mago(Gladiador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.mana=100

    def curar(self):
        if self.mana>=30:
            self.mana=self.mana-30
            self.vida=self.vida+20
            return (f"Te has curado. Vida: {self.vida}, Mana: {self.mana} ")
        
    def atacar(self, objetivo):
        if self.mana>=10:
            self.mana=self.mana-10
            objetivo.vida=objetivo.vida-25
            return (f" Lanzas BOLA de FUEGO!!. Ahora tienes de mana: {self.mana}. Tu objetivo tiene de vida: {objetivo.vida}.")
        else:
            return(f"No tienes suficiente mana para atacar.")
        
class Guerrero(Gladiador):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.furia=0
    
    def atacar(self, objetivo):
        if self.furia>50:
            if self.energia>=10:
                self.energia=self.energia-10
                self.furia=0
                objetivo.vida=objetivo.vida-30
                return (f" FURIA DESATADA!!. Ahora tienes de energia: {self.energia}. Tu furia es de: {self.furia}. Tu objetivo tiene de vida: {objetivo.vida}.")
            else:
                return(f"No tienes suficiente vida para atacar.")
        else:
            if self.energia>=10:
                self.energia=self.energia-10
                objetivo.vida=objetivo.vida-15
                return (f" Ahora tienes de energia: {self.energia}. Tu objetivo tiene de vida: {objetivo.vida}.")
            else:
                return(f"No tienes suficiente vida para atacar.")
            
jugador=Guerrero("Guerrero")

enemigo=random(Mago("Enemigo_mago"), Guerrero("Enemigo_guerrero"))

dic_menu={"a":"ATACAR", "c": "CURAR/HABILIDAD", "d": "DESCANSAR" }

def menu():
    print("*************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in dic_menu:
        print(f"Pulsa {clave}: {valor}")
    print("*************************")

while jugador.esta_vivo() and enemigo.esta_vivo():
    menu()

    opcion=input("Escoge una opción: ").lower()

    match opcion:
        case "a":
            
        case "c":
        
        case "d":
        
        case other:
            print("Te has equivocado de letra.")


