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

class PokemonAgua(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Agua.")

class PokemonFuego(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Fuego.")

class PokemonVolador(Pokemon):
    def __init__(self, nombre, tipo, ataque, defensa):
        super().__init__(nombre, tipo, ataque, defensa)

    def ataque_especial(self):
        return("Mi ataque especial es de Aire.")


almacen_pokemon=[]
def importarDatos(fichero):
    with open(fichero) as archivo:
        for linea in archivo:
            datos_pokemon=linea.split(",")
            nombre=datos_pokemon[0]
            tipo=datos_pokemon[1]
            ataque=datos_pokemon[2]
            defensa=datos_pokemon[3]

            cantidadPokemonAgua=0
            cantidadPokemonFuego=0
            cantidadPokemonPlanta=0
            cantidadPokemonVolador=0
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
            
            almacen_pokemon.append(p)

importarDatos("listado_pokemons.txt")

for i in almacen_pokemon:
    print(i.mostrar_info())

print(almacen_pokemon.count(cantidadPokemonPlanta))