'''
Crea un sistema bancario que te permita realizar ingresos de dinero en un cajero.
Pide al usuario cuánto dinero quiere ingresar y que lo introduzca por teclado.
Controla 3 posibles excepciones que puedan ocurrir y manéjalas.
Gestiona con un Finally un mensaje de finalización de la operación.
'''
class NumeroNegativoError(Exception):
    pass

def validar_numero(numero):
    if numero < 0 or numero<=1:
        raise NumeroNegativoError("La transferencia no puede ser negativa y tiene que ser mayor a 1.")

try:
    dinero=int(input("¿Cuánto dinero quieres ingresar?: "))
    validar_numero(dinero)

except NumeroNegativoError as e:
    print(e)

except TypeError:
    print("el valor no pueden ser palabras")

except Exception as e:
    print(f"Se produjo una excepción: {e}")

else:
    print("Operación realizada con éxito")

finally:
    print("Se ha finalizado la operación")