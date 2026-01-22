class Animal():
    def __init__(self, nombre, especie, edad, peso, sonido):
        self.nombre=nombre
        self.especie=especie
        if edad>=0: self.edad=edad
        if peso>0: self.peso=peso
        self.sonido=sonido

    def get_nombre(self):
        return self.nombre
    
    def get_especie(self):
        return self.especie
    
    def get_edad(self):
        return self.edad
    
    def get_peso(self):
        return self.peso
    
    def get_sonido(self):
        return self.sonido
    
    def set_nombre(self,n):
        self.nombre=n
        return self.nombre
    
    def set_especie(self,e):
        self.especie=e
        return self.especie
    
    def set_edad(self,edad):
        if edad>=0:
            self.edad=edad
            return self.edad
        else:
            return("No puedes poner edad negativa.")
    def set_peso(self,peso):
        if peso>0:
            self.peso=peso
            return self.peso
        else:
            return("No puedes poner peso negativo")
        
    def set_sonido(self, sonido):
        self.sonido=sonido
        return self.sonido
    
    def hacer_sonido(self):
        return (f" El animal emite: {self.sonido}.")
    
    def mostrar_info(self):
        return (f" {self.get_nombre()} de la especie: {self.get_especie()}- Edad: {self.get_edad()} años- Peso: {self.get_peso()} Kg")
    

class Clinica():
    def __init__(self):
        self.lista_pacientes=[]

    def ingresar_animal(self,animal):
        self.lista_pacientes.append(animal)
        return (f"{animal} se ha agregado a la lista.")
    
    
    def mostrar_pacientes(self):
        if self.lista_pacientes:
            for i in self.lista_pacientes:
                print(f"{i.mostrar_info()} y hace: {i.get_sonido()}.")
        else:
            print(f"Lista vacía, ingrese animal antes de mostrar pacientes.")

    
    def buscar_nombre(self,nombre):
        encontrado=False
        if self.lista_pacientes:
            for i in self.lista_pacientes:
                if i.nombre==nombre:
                    encontrado=True
                    return(f"{i.mostrar_info()} y hace: {i.get_sonido()}")
            if encontrado==False:
                return(f"El animal {nombre} no existe en la lista.")
        else:
            return(f"Lista vacía, ingrese animal antes de mostrar pacientes.")
    
    def mostrar_especie(self):
        lista_especie=[]
        if self.lista_pacientes:
            for i in self.lista_pacientes:
                if i.especie not in lista_especie:
                    lista_especie.append(i.especie)
            return(f"Las especies que hay en la clínica son: {lista_especie}")
        else:
            return("Lista vacía, rellene la lista antes de usar esta opción")
        
animal=None
clinica=Clinica()

salir=False

lista=["CREAR ANIMAL", "INGRESAR ANIMAL CLÍNICA", "BUSCAR ANIMAL CLÍNICA", "MOSTRAR ESPECIES CLÍNICA", "SALIR" ]
def menu():
    print("***********************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(lista, 1):
        print(f"Pulsa {clave}: {valor}")
    print("***********************")

while not salir:
    menu()

    opcion=int(input("Escoge una opción: "))

    match opcion:
        case 1:
            print(f"Has elegido: {lista[opcion-1]}")
            nombre=input("Escoge un nombre: ").lower()
            especie=input("Indica la especie: ").lower()
            edad=int(input("Indica la edad: "))
            peso=float(input("Indica el peso: "))
            sonido=input("Que sonido hace el animal: ").lower()

            animal=Animal(nombre, especie, edad, peso, sonido)

        case 2:
            print(f"Has elegido: {lista[opcion-1]}")
            if animal:
                print(clinica.ingresar_animal(animal))
            else:
                print("Debes crear un animal para ingresarlo en la lista")

        case 3:
            print(f"Has elegido: {lista[opcion-1]}")
            ani=input("Indica el nombre del animal: ").lower()

            print(clinica.buscar_nombre(ani))
            
        case 4:
            print(f"Has elegido: {lista[opcion-1]}")

            print(clinica.mostrar_especie())
        case 5:
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta, escoge del 1 al 5.")
