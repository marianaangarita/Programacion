'''
Definir una clase llamada Personaje.

La clase Personaje debe tener los siguientes atributos:
nombre: una cadena de caracteres que representa el nombre del personaje.
salud: un número entero que representa la salud del personaje.
ataque: un número entero que representa el ataque del personaje.
defensa: un número entero que representa la defensa del personaje.


La clase Personaje debe tener los siguientes métodos:
init(): un método constructor que inicializa los atributos del personaje.
atacar(personaje): un método que ataca a otro personaje, reduciendo su salud.


Crear  dos objetos Personaje, uno para el jugador y otro para el enemigo.

Programa un bucle que permita al jugador atacar al enemigo y viceversa hasta que uno de los dos muera.

Debes utilizar la función randint() para generar números aleatorios que representen el daño causado por los ataques.
'''
import random

class Personaje():
    def __init__(self,nombre,salud,ataque,defensa):
        self.nombre=nombre
        self.salud=salud
        self.ataque=ataque
        self.defensa=defensa
    
    def get_salud(self):
        return self.salud
    
    def set_salud(self, s):
        self.salud=s
    
    def set_ataque(self):
        self.ataque=random.randint(1,10)
        
    def atacar(self,personaje):
        personaje.salud = personaje.salud-self.ataque

    def info(self):
        return(f"Nombre: {self.nombre}, Salud: {self.salud}, Ataque: {self.ataque}, Defensa: {self.defensa}")

personaje1=Personaje("Mariana", 20, 2, 10)

enemigo1=Personaje("Carlos", 25, 3, 10)


while personaje1.get_salud()>0 and enemigo1.get_salud()>0:

    print(enemigo1.info())

    print(personaje1.info())

    lucha=input("Deseas atacar al enemigo (S/N): ").upper()

    match lucha:

        case 'S':
            personaje1.set_ataque()
            personaje1.atacar(enemigo1)
            print(enemigo1.get_salud())

            if enemigo1.get_salud()>0:
                print("El enemigo ataca")
                enemigo1.set_ataque()
                enemigo1.atacar(personaje1)
                print(personaje1.get_salud())

                if personaje1.get_salud()>0:
                    print("Que siga el combate")
                
                else:
                    print("Lo siento...has perdido")

            else:
                enemigo1.set_salud(0)

                print("¡Has ganado!")

            
        case 'N':
            personaje1.set_salud(0)
            print("Has salido del programa")

    