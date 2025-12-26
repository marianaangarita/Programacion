'''
Crea una clase llamada Tablet para representar una tableta digital
Los atributos que debe contener son:
creador(cadena de texto)
tamano_pantalla (flotante)
num_cores (entero)
apps (lista de cadenas de texto)
status (False: apagado, True: encendido)
Los métodos que debe contener la clase son:
__init__(self, creador, tamano_pantalla, num_cores)
power_on(self)
Cambia el status de apagado a encendido
power_off(self)
Cambia el status de encendido a apagado
install_app(self, app) (no instalar la app si ya existe)
Añade una nueva app a la lista
uninstall_app(self, app)
Elimina la app de la lista.
'''

class Tablet():
    def __init__(self,creador,pantalla,cores):
        self.creador=creador
        self.tamano_pantalla=pantalla
        self.num_cores=cores
        self.apps=[]
        self.status=False
    
    def get_creador(self):
        return self.creador
    
    def get_tamano_pantalla(self):
        return self.tamano_pantalla
    
    def get_num_cores(self):
        return self.num_cores
    
    def get_apps(self):
        return self.apps
    
    def get_status(self):
        return self.status
    
    def info(self):
        return(f"Creador: {self.get_creador()}, Tamaño pantalla: {self.get_tamano_pantalla()}, Número de cores: {self.get_num_cores()}, Apps: {self.get_apps()}, Status: {self.get_status()}")
    
    def power_on(self):
        if self.status==False:
            self.status=True

    def power_off(self):
        if self.status==True:
            self.status=False
    
    def install_app(self,app):
        if app in self.apps:
            print("La app ya está en la lista")

        else:
            self.apps.append(app)
            print(f"La app {app} se ha instalado correctamente.")
        
    def uninstall_app(self,app):
        
        if app in self.apps:

            self.apps.remove(app)

            print(f"La app {app} se ha desinstalado correctamente")
        else:
            print("La app no se encuentra en la lista, no se puede deinstalar")



tablet1=Tablet("Steve Jobs", 13.5, 4)

print(tablet1.info())

tablet1.install_app("Procreate")

tablet1.install_app("Final Cut")

tablet1.install_app("Blender")

tablet1.uninstall_app("Final Cut")

tablet1.power_on()

print(tablet1.info())