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
        return valor_carta
    else:
        return("Error en la petición", response.status_code)
    
print(sacar_carta())

acierto=0
salir=False

while not salir:
    primera_carta=sacar_carta()
    segunda_carta=sacar_carta()

    print(f"La primera carta es {primera_carta}")
    apuesta=input("¿Crees que la siguiente carta será mayor o menor que la segunda?: ").lower()

    if primera_carta>segunda_carta and apuesta=="mayor":
        acierto+=1
        print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! ")
        continue
    if primera_carta<segunda_carta and apuesta=="menor":
        acierto+=1
        print(f"Has acertado, la segunda carta era {segunda_carta}, sigues jugando! ")
        continue
    else:
        salir=True
        print(f"Fallaste... has acertado {acierto} veces")


             
