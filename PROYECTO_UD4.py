import random
almacen_pokemons=[]
salir=False

class Pokemon():
    def __init__(self, nombre, tipo, ataque, defensa):
        self.nombre=nombre
        self.tipo=tipo
        self.ataque=ataque
        self.defensa=defensa
        self.ps=100
    def get_nombre(self):
        return self.nombre
    def get_tipo(self):
        return self.tipo
    def get_ataque(self):
        return self.ataque
    def get_defensa(self):
        return self.defensa
    def get_ps(self):
        return self.ps
    def set_ps(self, p):
        self.ps=p
    def recibir_dano(self, cantidad):
        self.ps -= cantidad
        if self.ps < 0:
            self.ps = 0
    def mostrar_info(self):
        return(f" Nombre: {self.get_nombre()} | Tipo: {self.get_tipo()} | Ataque: {self.get_ataque()} | Defensa: {self.get_defensa()} | Puntos salud: {self.get_ps()}")

class PokemonPlanta(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return ("Mi ataque especial es de Planta.")
    
    def mensaje_tipo(self):
        return("¡ideal contra Pokémon de Agua!")

class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Agua.")
    
    def mensaje_tipo(self):
        return("ten cuidado con los de tipo Fuego.")

class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Fuego.")
    
    def mensaje_tipo(self):
        return("ten cuidado con los de tipo Agua.")

class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Aire.")
    
    def mensaje_tipo(self):
        return("¡ideal contra pokemon Planta!")


def importarDatos(fichero):
    cantidadPokemonAgua=0
    cantidadPokemonFuego=0
    cantidadPokemonPlanta=0
    cantidadPokemonVolador=0
    cantidadTotal=0

    with open(fichero) as archivo:
        for linea in archivo:
            datos_pokemon=linea.split(",")
            nombre=datos_pokemon[0]
            tipo=datos_pokemon[1].rstrip().capitalize()
            ataque=int(datos_pokemon[2])
            defensa=int(datos_pokemon[3])

            match tipo:
                case "Agua":
                    p=PokemonAgua(nombre, tipo, ataque, defensa)
                    cantidadPokemonAgua=cantidadPokemonAgua+1
                    
                case "Fuego":
                    p=PokemonFuego(nombre, tipo, ataque, defensa)
                    cantidadPokemonFuego=cantidadPokemonFuego+1
                    
                case "Volador":
                    p=PokemonVolador(nombre, tipo, ataque, defensa)
                    cantidadPokemonVolador=cantidadPokemonVolador+1
                    
                case "Planta":
                    p=PokemonPlanta(nombre, tipo, ataque, defensa)
                    cantidadPokemonPlanta=cantidadPokemonPlanta+1
                case _:
                    print("Tipo desconocido, saltando Pokémon")
                    p = None
            if p:
                almacen_pokemons.append(p)
                cantidadTotal+=1
        return(f"Se ha registrado en el sistema: {cantidadTotal} Pokemons. \n * Cantidad Pokemon Agua: {cantidadPokemonAgua} \n * Cantidad Pokemon Fuego: {cantidadPokemonFuego} \n * Cantidad Pokemon Volador: {cantidadPokemonVolador} \n * Cantidad Pokemon Planta: {cantidadPokemonPlanta}")
    
def comprobacion_datos():
    for i in almacen_pokemons:
        print(f"{i.get_nombre()} es un Pokémon de tipo {i.get_tipo()}, {i.mensaje_tipo()}")


class Mapa():
    def __init__(self, lado):
        self.lado=lado
        self.tablero=[[random.choice(almacen_pokemons) for x in range(0, self.lado)] for y in range(0, self.lado)]
        
        
    def coordenada(self,y, x):
        # y=fila x=columna
        return (f"({y},{x}):{self.tablero[y][x].get_nombre()}")

               
    def mostrarMapa(self):
        for y in range(0, self.lado):
            for x in range(0, self.lado):
                print(f"({y},{x})", end=" ") 
            print(" ")

    def mostrarMapaDetallado(self):
         for y in range(0, self.lado):
            for x in range(0, self.lado):
                print(f"{self.coordenada(y,x)}", end=" ") 
            print(" ")
        

class Personaje():
    def __init__(self, x, y):
        self.posX=x
        self.posY=y
        self.limite=mapa.lado

    def moverIzquierda(self):
        if self.posX > 0:
            self.posX -= 1
        else:
            print("¡Muro!")
            
    def moverDerecha(self):
        if self.posX <= self.limite:
            self.posX += 1
        else:
            print("¡Muro!")

    def moverAbajo(self):
        if self.posY > 0:
            self.posY -= 1
        else:
            print("¡Muro!")
            
    def moverArriba(self):
        if self.posY <= self.limite:
            self.posY += 1
        else:
            print("¡Muro!")

class Jugador(Personaje):
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre=nombre
        self.inventario = []
        
    def capturar_pokemon(self, pokemon):
        probabilidad = (100 - pokemon.ps) + 10 
        dado = random.randint(0, 100)
        print(f"Probabilidad de éxito: {probabilidad}% (Dado: {dado})")
        
        if dado <= probabilidad:
            self.inventario.append(pokemon)
            mapa.tablero[self.posY][self.posX] = None
            return True
        else:
            return False
    

opciones_menu={"M":"CREAR MAPA", "J":"CREAR JUGADOR", "W":"IZQUIERDA", "D": "DERECHA", "S":"ABAJO", "A":"ARRIBA", "C":"CAPTURAR POKEMON", "E":"SALIR"}

def menu():
    print("********************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in opciones_menu.items():
        print(f"Pulsa {clave}:{valor}")
    print("********************************")

personaje=None
mapa=None

while not salir:
    print("¡Bienvenido al simulador de entrenador Pokemon!")
    if personaje:
        print(f"Posición: ({personaje.posY}, {personaje.posX})")
    menu()
    opcion=input("Escoge una opción: ").upper()

    match opcion:
        case "M":
            if mapa:
                print("Solo puedes crear un mapa.")
            else:
                lado=int(input("¿Cuántos lados tiene el mapa?: "))
                mapa=Mapa(lado)
                print("Se ha generado un mapa con pokemons aleatorios.")
                print("¡Prepárate para explorarlo!")
                print(mapa.mostrarMapaDetallado())
        case "J":
            if personaje:
                print("Solo puedes crear un personaje.")
            else:
                x=int(input("Indica la posición x: "))
                y=int(input("Indica la posición y: "))
                nombre=input("Indica el nombre del jugador: ").lower()
                personaje=Jugador(x, y, nombre)
        case "W":
            if mapa and personaje:
                    personaje.moverIzquierda()
            else:
                print("Debes crear el mapa y personaje primero")
            
        case "D":
            if mapa and personaje:
                    personaje.moverDerecha()
            else:
                print("Debes crear el mapa y personaje primero")
        case "S":
            if mapa and personaje:
                    personaje.moverAbajo() 
            else:
               print("Debes crear el mapa y persoanje primero") 
        case "A":
            if mapa and personaje:
                    personaje.moverArriba() 
            else:
                print("Debes crear el mapa y persoanje primero") 
        case "C":
            if mapa and personaje:

                pokemon_actual = mapa.tablero[personaje.posY][personaje.posX]
                
                if pokemon_actual is None:
                    print("Aquí no hay nada.")

                else:
                    print(f"¡Has encontrado un {pokemon_actual.get_nombre()}! (PS: {pokemon_actual.get_ps()})")
                    print("1. Atacar (Bajar vida)")
                    print("2. Lanzar Pokéball")
                    accion = int(input("Elige (1 o 2): "))
                    
                    match accion:
                        case 1:
                            dano = random.randint(20, 40)
                            pokemon_actual.recibir_dano(dano)
                            print(f"¡Golpeado! Vida restante: {pokemon_actual.get_ps()}")
                        
                        case 2:
                            capturado = personaje.intentar_captura(pokemon_actual, mapa)
                            if capturado:
                                print("¡CAPTURADO CON ÉXITO!")
                            else:
                                print("¡Se ha escapado de la bola!")
            else:
                print("Debes crear el mapa y personaje primero")
            
        case "E":
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción incorrecta")
        