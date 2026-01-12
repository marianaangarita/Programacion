'''
Vamos a crear un sistema simple de cuentas bancarias utilizando programación orientada a objetos en Python. Crea las siguientes clases:

CuentaBancaria (Clase CuentaBancaria):
Una clase base que representa una cuenta bancaria básica.
Debe contener los siguientes métodos:
Inicializar la cuenta
Obtener el saldo
Depositar dinero
Retirar dinero (manejando con control de errores)
Transferir dinero a otra cuenta (también controlando errores).

CuentaRecompensas (Subclase de CuentaBancaria):
Una subclase de CuentaBancaria que proporciona una recompensa de interés del 5% en los depósitos que hayan ingresado.

CuentaAhorros (Subclase de CuentaBancaria:
Una subclase de CuentaBancaria que agrega una tarifa de retiro de 5€ en cada transacción de retiro.

'''
class CuentaBancaria():
    def __init__(self,nombre,saldo):
        self.nombre=nombre
        self.saldo=saldo

    def inicializar_cuenta(self):
        return(f"Cuenta {self.nombre} creada. Saldo {self.saldo}€.")

    def obtener_saldo(self):
        return(f"Saldo de la cuenta {self.nombre} = {self.saldo}€")
    
    def depositar_dinero(self,dinero):
        self.saldo=self.saldo + dinero
        print("Depósito completado.")

    def retirar_dinero(self, dinero):
        if dinero>self.saldo:
            print(f"Retiro interrumpido: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}.")
        else:
            self.saldo=self.saldo-dinero
            print(f"Retiro de {dinero}€ completado.")

    def transferir_dinero(self, dinero, cuenta):
        if dinero>self.saldo:
            print("Iniciando Transferencia...")
            print(f"Transferencia fallida: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}.")
        else:
            print("Iniciando Transferencia...")
            self.retirar_dinero(dinero)
            cuenta.depositar_dinero(dinero)
            print(f"Retiro de {dinero}€ completado.")
            print(f"Saldo de la cuenta {self.nombre}= {self.saldo}€")
            print("Depósito Completado.")
            print(f"Saldo de la cuenta {cuenta.nombre}= {cuenta.saldo}€")
            print("Transferencia Completada!")

class CuentaRecompensas(CuentaBancaria):
    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)

    def depositar_dinero(self,dinero):
        interes=dinero*0.05
        self.saldo=self.saldo + dinero + interes
        print("Depósito completado con recompensas de interés.")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)

    def depositar_dinero(self,dinero):
        interes=dinero*0.05
        self.saldo=self.saldo + dinero + interes
        print("Depósito completado con recompensas de interés.")
    
    def retirar_dinero(self, dinero):
        if dinero+5>self.saldo:
            print(f"Retiro interrumpido: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}.")
        else:
            self.saldo=self.saldo-5-dinero
            print(f"Retiro de {dinero}€ completado con tarifa de retiro.")

    def transferir_dinero(self, dinero, cuenta):
        if dinero>self.saldo:
            print("Iniciando Transferencia...")
            print(f"Transferencia fallida: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}.")
        else:
            print("Iniciando Transferencia...")
            self.retirar_dinero(dinero)
            cuenta.depositar_dinero(dinero)
            print(f"Retiro de {dinero}€ completado con tarifa de retiro.")
            print(f"Saldo de la cuenta {self.nombre}= {self.saldo}€")
            print("Depósito Completado.")
            print(f"Saldo de la cuenta {cuenta.nombre}= {cuenta.saldo}€")
            print("Transferencia Completada!")