import random

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




almacen_pokemons=[]

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
    

print(importarDatos("listado_pokemons.txt"))

def comprobacion_datos():
    for i in almacen_pokemons:
        print(f"{i.get_nombre()} es un Pokémon de tipo {i.get_tipo()}, {i.mensaje_tipo()}")

comprobacion_datos()

class Mapa():
    def __init__(self, lado):
        self.lado=lado
        self.tablero=[]
        self.tablero.append(random.choice(almacen_pokemons))

    
    def coordenada(self, x, y):
        
    
    def mostrarMapa(self):
    
    def mostrarMapaDetallado(self):
