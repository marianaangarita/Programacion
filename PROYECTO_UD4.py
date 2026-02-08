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
        p = self.tablero[y][x]
        if p is None: 
            return "Vacío"
        else:
            return (f"({y},{x}):{p.get_nombre()}")
    
    def ver_pokemon(self, x, y):
        return self.tablero[y][x]
        
    def obtener_pokemon(self, x, y):
        #Devuelve el pokemon en la posición y lo elimina del mapa
        p = self.tablero[y][x]
        if p is not None:
            self.tablero[y][x] = None
        return p
               
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
    def __init__(self, x, y, limite):
        self.posX=x
        self.posY=y
        self.limite=limite

    def moverIzquierda(self):
        if self.posX > 0:
            self.posX -= 1
        else:
            print("¡Muro!")
            
    def moverDerecha(self):
        if self.posX <= self.limite-1:
            self.posX += 1
        else:
            print("¡Muro!")

    def moverAbajo(self):
        if self.posY > 0:
            self.posY -= 1
        else:
            print("¡Muro!")
            
    def moverArriba(self):
        if self.posY <= self.limite-1:
            self.posY += 1
        else:
            print("¡Muro!")

class Jugador(Personaje):
    def __init__(self, x, y, nombre, limite):
        super().__init__(x,y,limite)
        self.nombre=nombre
        self.inventario = []

    def capturar_pokemon(self, mapa):
        pokemon = mapa.obtener_pokemon(self.posX, self.posY)

        if pokemon is None:
            print("Aquí no hay ningún Pokémon.")
            return False

        probabilidad = (100 - pokemon.get_ps()) + 10
        dado = random.randint(1, 100)

        print(f"Probabilidad: {probabilidad}% | Dado: {dado}")

        if dado <= probabilidad:
            self.inventario.append(pokemon)
            print(f"¡Has capturado a {pokemon.get_nombre()}!")
            return True
        else:
            print(f"{pokemon.get_nombre()} se escapó...")
            # si falla, vuelve al mapa
            mapa.tablero[self.posY][self.posX] = pokemon
            return False

print(importarDatos("pokemons.txt"))
  

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
                mapa.mostrarMapaDetallado()
        case "J":
            if personaje:
                print("Solo puedes crear un personaje.")
            elif not mapa:
                print("¡Primero crea el mapa (M)!")
            else:
                x=int(input(f"Indica la posición x (0-{mapa.lado-1}): "))
                y=int(input(f"Indica la posición y (0-{mapa.lado-1}): "))
                if 0 <= x < mapa.lado and 0 <= y < mapa.lado:
                    nombre=input("Indica el nombre del jugador: ").lower()
                    personaje=Jugador(x, y, nombre, mapa.lado)
                    print(f"Jugador {nombre} creado.")
                    print(f"Posición: ({personaje.posY}, {personaje.posX})")
                else:
                    print("Coordenadas fuera del mapa.")
        case "W":
            if mapa and personaje:
                    personaje.moverIzquierda()
                    print(f"Posición: ({personaje.posY}, {personaje.posX})")
            else:
                print("Debes crear el mapa y personaje primero")
            
        case "D":
            if mapa and personaje:
                    personaje.moverDerecha()
                    print(f"Posición: ({personaje.posY}, {personaje.posX})")
            else:
                print("Debes crear el mapa y personaje primero")
        case "S":
            if mapa and personaje:
                    personaje.moverAbajo()
                    print(f"Posición: ({personaje.posY}, {personaje.posX})") 
            else:
               print("Debes crear el mapa y persoanje primero") 
        case "A":
            if mapa and personaje:
                    personaje.moverArriba()
                    print(f"Posición: ({personaje.posY}, {personaje.posX})") 
            else:
                print("Debes crear el mapa y persoanje primero") 
        case "C":
            if mapa and personaje:
                pokemon_actual = mapa.ver_pokemon(personaje.posX, personaje.posY)

                if pokemon_actual is None:
                    print("Aquí no hay ningún Pokémon.")

                else:
                    print(f"¡Has encontrado un {pokemon_actual.get_nombre()}! | PS: {pokemon_actual.get_ps()})")
                    print("1. Atacar (Bajar vida)")
                    print("2. Lanzar Pokéball")
                    accion = int(input("Elige (1 o 2): "))
                    
                    match accion:
                        case 1:
                            dano = random.randint(20, 50)
                            pokemon_actual.recibir_dano(dano)
                            print(f"¡Golpeado! Vida restante: {pokemon_actual.get_ps()}")
                        
                        case 2:
                            exito = personaje.capturar_pokemon(mapa)
                            if exito:
                                print("¡CAPTURADO CON ÉXITO!")
                            else:
                                print("¡Se ha escapado de la bola!")
                        case __:
                            print("Opción incorrecta.")
            else:
                print("Debes crear el mapa y personaje primero")
            
        case "E":
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción incorrecta")
        