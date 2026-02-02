import random

min_cas=0
max_cas=5
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
        self.tablero=[[random.choice(almacen_pokemons) for x in range(min_cas, self.lado)] for y in range(min_cas, self.lado)]
        
        
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

    def moverIzquierda(self):
        if self.posX>=min_cas and self.posX<=max_cas:
            posX=posX-1
            return posX
        else:
            return(f"No pudes salirte del tablero")
        
    def moverDerecha(self):
        if self.posX>=min_cas and self.posX<=max_cas:
            posX=posX+1
            return posX
        else:
            return("No puedes salirte del tablero")

    def moverArriba(self):
        if self.posY>=min_cas and self.posY<=max_cas:
            posY=posY+1
            return posY
        else:
            return("No puedes salirte del tablero")
        
    def moverAbajo(self):
        if self.posY>=min_cas and self.posY<=max_cas:
            posY=posY-1
            return posY
        else:
            return("No puedes salirte del tablero")

class Jugador(Personaje):
    def __init__(self, x, y, nombre):
        super().__init__(x, y)
        self.nombre=nombre
    
    def capturar_pokemon(self, pokemon):
        pokemon_capturado=[]
        mapa.tablero.remove(pokemon)
        pokemon_capturado.append(pokemon)
        #los pokemons en el mapa, los saco de la lista y los meto en la nueva lista pokemon_capturado

        return(f"Has capturado al pokemon: {pokemon.get_nombre()}")
    

opciones_menu={"M":"CREAR MAPA", "J":"CREAR JUGADOR", "W":"IZQUIERDA", "D": "DERECHA", "S":"ABAJO", "A":"ARRIBA", "C":"CAPTURAR POKEMON", "S":"SALIR"}

def menu():
    print("********************************")
    print("MENÚ PRINCIPAL")
    for clave, valor in opciones_menu.items():
        print(f"Pulsa {clave}:{valor}")
    print("********************************")

personaje=None
mapa=None

while not salir:
    menu()
    opcion=input("Escoge una opción: ").upper()

    match opcion:
        case "M":
            if mapa:
                print("Solo puedes crear un mapa.")
            else:
                lado=int(input("¿Cuántos lados tiene el mapa?: "))
                mapa=Mapa(lado)
        case "J":
            if personaje:
                print("Solo puedes crear un personaje.")
            else:
                x=int(input("Indica la posición x: "))
                y=int(input("Indica la posición y: "))
                nombre=input("Indica el nombre del jugador: ").lower()
                personaje=Jugador(x, y, nombre)
        case "W":
            personaje.moverIzquierda()
        case "D":
            personaje.moverDerecha()
        case "S":
        case "A":
        case "C":
        case "S":
            salir=True
            print("Has salido del programa")
        case __:
            print("Opción incorrecta")
        