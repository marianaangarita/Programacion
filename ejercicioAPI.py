'''
1. Crea el juego superior/inferior haciendo peticiones a la api https://www.deckofcardsapi.com/
2. Crea un sistema de vidas que cuando aciertes, continues y cuando falles la siguiente carta te reste una vida.
'''

import requests

def sacar_carta(id_mazo):
    response = requests.get(f"https://www.deckofcardsapi.com/api/deck/{id_mazo}/draw/?count=1")
    if response.status_code == 200:
        data = response.json()  
        #cuantas_cartas_quedan = data["remaining"]
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
    
    #if cuantas_cartas_quedan == 0:

    else:
        return("Error en la petición", response.status_code)
    

acierto = 0
vidas = 10

respuesta = requests.get("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

datos = respuesta.json()



id_mazo_final = datos["deck_id"]

carta_actual=sacar_carta(id_mazo_final)

while vidas > 0:

    print(f"\n Tienes {vidas} y llevas {acierto} aciertos.")

    print(f"La carta actual es: {carta_actual}")

    apuesta=input("¿Crees que la siguiente carta será mayor o menor que la primera?: ").lower()

    segunda_carta=sacar_carta(id_mazo_final)

    try:
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

    except ValueError:
        print("Opcion no válida vuelve a intentarlo")
        continue


             
