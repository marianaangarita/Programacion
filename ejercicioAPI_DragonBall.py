import requests
import random

def peticionAPI():
    id=random.randint(1,44)
    url="https://dragonball-api.com/api/characters/"+str(id)
   
    peticion=requests.get(url)
    datos=peticion.json()
    personaje={"nombre":datos["name"], "poder":random.randint(1,10000)}
    return personaje

def batalla(p1,p2):
    if(p1["poder"]>p2["poder"]):
        return p1
    elif(p1["poder"]==p2["poder"]):
        if (random.randint(1,2)==1):
            return p1
        else:
            return p2
    else:
        return p2

J1=peticionAPI()
J2=peticionAPI()
J3=peticionAPI()
J4=peticionAPI()

print(J1)
print(J2)
print(J3)
print(J4)

finalista1=batalla(J1,J2)
print(f"El primer finalista es {finalista1}")
finalista2=batalla(J3,J4)
print(f"El segundo finalista es {finalista2}")
ganador=batalla(finalista1,finalista2)
print(f"El ganador del torneo es: {ganador}")