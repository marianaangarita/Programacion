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
    def __init__(self,creador,pantalla,cores,apps,status):
        self.creador=creador
        self.tamano_pantalla=pantalla
        self.num_cores=cores
        self.apps=[]
        self.status=True
    
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
            print("La app se ha instalado correctamente.")
        
    def uninstall_app(self,app):
        
        if app in self.apps:

            self.apps.remove(app)

            print("La app se ha desinstalado correctamente")
        else:
            print("La app no se encuentra en la lista, no se puede deinstalar")