import requests

def sacar_carta():
    response = requests.get("https://www.deckofcardsapi.com/api/deck/new/draw/?count=2")
    if response.status_code == 200:
        data = response.json()  
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
        return("Error en la petición", response.status_code)
    

acierto=0
salir=False

while not salir:
    primera_carta=sacar_carta()
    segunda_carta=sacar_carta()

    print(f"La primera carta es {primera_carta}")
    apuesta=input("¿Crees que la siguiente carta será mayor o menor que la primera?: ").lower()
    try:
        if segunda_carta>primera_carta and apuesta=="mayor":
            acierto+=1
            print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! ")
            continue
        if segunda_carta<primera_carta and apuesta=="menor":
            acierto+=1
            print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! ")
            continue
        else:
            salir=True
            print(f"Fallaste... has acertado {acierto} veces")
    except ValueError:
        print("Opcion no válida vuelve a intentarlo")
        continue


             
