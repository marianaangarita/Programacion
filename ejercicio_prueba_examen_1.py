'''
Ejercicio 1: Sistema de Gestión de Envíos (Similar al Bancario)
Enfoque: Herencia, validaciones y lógica de negocio.

Contexto: Una empresa de logística necesita gestionar diferentes tipos de envíos.

Clase Base Paquete:

Atributos: destinatario, peso (kg), estado (inicialmente "En almacén").

Método calcular_costo(): Devuelve el precio base (ej: 5€ por el envío).

Método enviar(): Cambia el estado a "En camino" e imprime un mensaje.

Método entregar(): Solo funciona si está "En camino". Cambia estado a "Entregado".

Subclase PaqueteExpress (Hereda de Paquete):

Hereda todo, pero el costo es diferente: Precio base + 10€ de recargo por urgencia. (Sobrescribe calcular_costo).

Tiene un atributo extra en el constructor: hora_limite.

Subclase PaqueteFragil (Hereda de Paquete):

Tiene un atributo extra: seguro (booleano).

Sobrescribe calcular_costo(): Si tiene seguro, suma 20€ al precio base. Si no, precio normal.

Sobrescribe enviar(): Antes de cambiar el estado, debe imprimir "¡Atención! Manipular con cuidado".

Tu Misión: Crea un pequeño script que instancie un paquete de cada tipo, calcule sus costos y simule el proceso de envío y entrega.
'''

class Paquete():
    def __init__(self,destinatario, peso):
        self.destinatario=destinatario
        self.peso=peso
        self.estado="En almacén"

    def calcular_costo(self):
        envio=5
        precio_base=self.peso+envio
       
        return (f"El precio base del paquete con destinatario {self.destinatario} es de {precio_base}")
    
    def enviar(self):
        self.estado="En camino"
        return (f"El paquete con destinatario: {self.destinatario}, está {self.estado}.")
    
    def entregar(self):
        if self.estado=="En camino":
            self.estado="Entregado"
            return (f"El paquete con destinatario: {self.destinatario}, está {self.estado}.")
        
        if self.estado=="En almacén":
            return("El paquete aun no está listo para entregarse.") 

        if self.estado=="Entregado":
            return("El paquete ya ha sido entregado.")


class PaqueteExpress(Paquete):
    def __init__(self, destinatario, peso, hora_limite):
        super().__init__(destinatario, peso)
        self.hora_limite=hora_limite
     

    def calcular_costo(self):
        envio=5
        precio_base=self.peso+envio+10
        return (f"El precio base del paquete con destinatario {self.destinatario} es de {precio_base}")
    
    
class PaqueteFragil(Paquete):
    def __init__(self, destinatario, peso, seguro):
        super().__init__(destinatario, peso)
        self.seguro=seguro
        

    def calcular_costo(self):
        if self.seguro==True:
            envio=5
            precio_base=self.peso+envio+20
            return (f"El precio base del paquete con destinatario {self.destinatario} es de {precio_base}")
        else:
            return super().calcular_costo()
    
    def enviar(self):
        print("¡ATENCIÓN! Manipular con cuidado")
        return super().enviar()
    
paquete=Paquete("Carlos", 3)

print(paquete.calcular_costo())

print(paquete.enviar())

print(paquete.entregar())

express=PaqueteExpress("Ana", 5, 17)

print(express.calcular_costo())

print(express.enviar())

print(express.entregar())

fragil=PaqueteFragil("Luis", 10, True)

print(fragil.calcular_costo())

print(fragil.enviar())

print(fragil.entregar())