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
        print(f"Cuenta {self.nombre} creada. Saldo {self.saldo}€.")

    def obtener_saldo(self):
        print(f"Saldo de la cuenta {self.nombre} = {self.saldo}€")
    
    def depositar(self,dinero):
        if dinero>0:
            self.saldo=self.saldo + dinero
            print("Depósito completado.")
        else:
            print("No puedes depositar una cantidad menor a 0€.")

    def retirar(self, dinero):
        if dinero>0:
            if dinero>self.saldo:
                print(f"Retiro interrumpido: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}€.")
                return False
            else:
                self.saldo=self.saldo-dinero
                print(f"Retiro de {dinero}€ completado.")
                return True
        else:
            print("No puedes retirar una cantidad menor a 0€.")
            return False

    def transferir(self, dinero, cuenta):
        if dinero>0:
            if dinero>self.saldo:
                print("Iniciando Transferencia...")
                print(f"Transferencia fallida: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}€.")
            else:
                print("Iniciando Transferencia...")
                if self.retirar(dinero):
                    cuenta.depositar(dinero)
                    print(f"Saldo de la cuenta {self.nombre} = {self.saldo}€")
                    print(f"Saldo de la cuenta {cuenta.nombre} = {cuenta.saldo}€")
                    print("Transferencia Completada!")
        else:
            print("No puedes transferir una cantidad menor a 0€.")

class CuentaRecompensas(CuentaBancaria):
    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)

    def depositar(self,dinero):
        if dinero>0:
            interes=dinero*0.05
            self.saldo=self.saldo + dinero + interes
            print("Depósito completado con recompensas de interés.")
        else:
            print("No puedes depositar una cantidad menor a 0€.")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, nombre, saldo):
        super().__init__(nombre, saldo)

    def retirar(self, dinero):
        if dinero>0:
            if dinero+5>self.saldo:
                print(f"Retiro interrumpido: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}€.")
                return False
            else:
                self.saldo=self.saldo-5-dinero
                print(f"Retiro de {dinero}€ completado con tarifa de retiro.")
                return True
        else:
            print("No puedes retirar una cantidad menor a 0€.")
            return False

    def transferir(self, dinero, cuenta):
        if dinero>0:
            if dinero+5>self.saldo:
                print("Iniciando Transferencia...")
                print(f"Transferencia fallida: Lo siento, la cuenta {self.nombre} solo tiene un saldo de {self.saldo}€.")
            else:
                print("Iniciando Transferencia...")
                if self.retirar(dinero):
                    cuenta.depositar(dinero)
                    print(f"Saldo de la cuenta {self.nombre} = {self.saldo}€")
                    print(f"Saldo de la cuenta {cuenta.nombre} = {cuenta.saldo}€")
                    print("Transferencia Completada!")
        else:
            print("No puedes transferir una cantidad menor a 0€.")
        

Cuenta1 = CuentaBancaria("Cliente1", 1000)
print("  ")

Cuenta1.obtener_saldo()
print("  ")

Cuenta1.retirar(10000)
print("  ")

Cuenta1.retirar(10)
print("  ")

Cuenta1.obtener_saldo()
print("  ")

Cuenta2 = CuentaBancaria("Cliente2", 2000)
print("  ")

Cuenta2.obtener_saldo()
print("  ")

Cuenta2.depositar(500)
print("  ")

Cuenta2.obtener_saldo()
print("  ")

Cuenta1.transferir(10000, Cuenta2) # Fallida
print("  ")

Cuenta2.transferir(100, Cuenta1) # Correcta
print("  ")

CuentaInteres = CuentaRecompensas("CuentaInteres", 1000)
print("  ")

CuentaInteres.obtener_saldo()
print("  ")

CuentaInteres.depositar(100)
print("  ")

CuentaInteres.obtener_saldo()
print("  ")

CuentaAhorros1 = CuentaAhorros("CuentaAhorros1", 1000)
print("  ")

CuentaAhorros1.obtener_saldo()
print("  ")

CuentaAhorros1.depositar(100)
print("  ")

CuentaAhorros1.obtener_saldo()
print("  ")

CuentaAhorros1.transferir(10000, Cuenta2)
print("  ")

CuentaAhorros1.transferir(1000, Cuenta2)

