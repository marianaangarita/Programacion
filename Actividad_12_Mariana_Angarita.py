'''
Actividad 12. Herencia y métodos específicos
Crea una clase base Animal con un método mover. Luego, crea dos clases derivadas Pajaro y Pez que hereden de Animal y tengan métodos adicionales como volar y nadar respectivamente. Además, a Pez deberás crearle su propio método mover para sobreescribir el general.
Añade un print a cada método para que se pueda observar su ejecución.

Ejemplo de ejecución y salida.
pajaro = Pajaro()
pez = Pez()

pajaro.mover()  # Salida: El animal se mueve de alguna manera
pajaro.volar()  # Salida: El pájaro vuela por el cielo
pez.mover()     # Salida: El animal se mueve de alguna manera
pez.nadar()     # Salida: El pez nada en el agua
'''

class Animal():
    @staticmethod
    def mover():
        print ("el animal se mueve saltando")
class Pajaro(Animal):
    @staticmethod
    def volar():
        print ("El pájaro vuela por el cielo")

class Pez(Animal):
    @staticmethod
    def mover():
        print ("el animal se mueve arrastrandose")
    @staticmethod
    def nadar():
        print ("El pez nada en el agua")

pajaro = Pajaro()
pez = Pez()
pajaro.mover()
pajaro.volar()
pez.mover()
pez.nadar()