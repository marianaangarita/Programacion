'''
1. Crea el juego superior/inferior haciendo peticiones a la api https://www.deckofcardsapi.com/
2. Crea un sistema de vidas que cuando aciertes, continues y cuando falles la siguiente carta te reste una vida.
'''

import requests

import sys  # para parar el programa

acierto = 0

vidas = 10

respuesta = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

datos = respuesta.json()

id_mazo_final = datos["deck_id"]

def sacar_carta(id_mazo):
    response = requests.get(f"https://www.deckofcardsapi.com/api/deck/{id_mazo}/draw/?count=1")
    if response.status_code == 200:
        data = response.json()  
        cuantas_cartas_quedan = data["remaining"]
        if cuantas_cartas_quedan > 0:
            valor_carta=(data["cards"][0]["value"])
            match valor_carta:
                case "QUEEN":
                    valor_carta=12
                case "KING":
                    valor_carta=13
                case "JACK":
                    valor_carta=11
                case "ACE":
                    valor_carta=1
                case __:
                    valor_carta=int((data["cards"][0]["value"]))
            return valor_carta
    
        else:
            return None

    else:
        return("Error en la petición", response.status_code)
    
carta_actual=sacar_carta(id_mazo_final)

if carta_actual is None:
    print("¡Se han acabado las cartas del mazo! Juego terminado")
    sys.exit() # se para el programa
    
    
while vidas > 0:

    print(f"\n Tienes {vidas} vidas y llevas {acierto} aciertos.")

    print(f"La carta actual es: {carta_actual}")

    apuesta=input("¿Crees que la siguiente carta será mayor o menor que la primera?: ").lower()

    if apuesta not in ["mayor", "menor"]:
        print(" Por favor, escribe 'mayor' o 'menor'.")
        continue

    segunda_carta=sacar_carta(id_mazo_final)

    if segunda_carta is None:
        print("¡Se han acabado las cartas del mazo! Juego terminado")
        break
    
    if segunda_carta>carta_actual and apuesta=="mayor":
        acierto+=1
        print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! Número de vidas: {vidas}")    

    elif segunda_carta<carta_actual and apuesta=="menor":
        acierto+=1
        print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! Número de vidas: {vidas}")
           
    elif segunda_carta == carta_actual:
        print("¡Ha sido empate! no te suma aciertos ni fallos, toca probar la siguiente ronda!")

    else:
        vidas -= 1
        print(f"Fallaste... la segunda carta era: {segunda_carta}. Has acertado {acierto} veces. Número de vidas: {vidas}")
        
    carta_actual=segunda_carta


print("--- FIN DEL JUEGO ---")
print(f"Puntuación final: {acierto} aciertos.")
             
