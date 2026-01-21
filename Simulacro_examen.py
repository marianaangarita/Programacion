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
        return (f" El {self.especie} con hace: {self.sonido}.")
    
    def mostrar_info(self):
        return (f" {self.get_nombre()} de la especie: {self.get_especie()}- Edad: {self.get_edad()} años- Peso: {self.get_peso} Kg")
    

class Clinica():
    def __init__(self):
        self.lista_pacientes=[]

    def ingresar_animal(self,animal):
        for i in self.lista_pacientes:
            if i==animal:
                return(f"{animal} ya está en la lista.")
        self.lista_pacientes.append(animal)
        return (f"{animal} se ha agregado a la lista.")
    
    
    def mostrar_pacientes(self):
        if self.lista_pacientes:
            for i in self.lista_pacientes:
                print(f"{i.mostrar_info()} y hace: {i.get_sonido()}.")
        else:
            return (f"Lista vacía, ingrese animal antes de mostrar pacientes.")

    
    def buscar_nombre(self,nombre):
        if self.lista_pacientes:
            for i in self.lista_pacientes:
                if i.nombre==nombre:
                    print(f"{i.mostrar_info()} y hace: {i.get_sonido()}")
        else:
            return (f"Lista vacía, ingrese animal antes de mostrar pacientes.")
        
perro=Animal("Rex", "perro", 3, 5.2, "guau")

gato=Animal("Luna", "gato", 2, 3.3, "miau")

clinica=Clinica()

salir=False

lista=["CREAR ANIMAL", "INGRESAR ANIMAL CLÍNICA", "BUSCAR ANIMAL CLÍNICA", "MOSTRAR ESPECIES CLÍNICA", "SALIR" ]
def menu():
    print("***********************")
    print("MENÚ PRINCIPAL")
    for clave, valor in enumerate(1, lista):
        print(f"Pulsa {clave}: {valor}")
    print("***********************")

while not salir:
    menu()

    opcion=int(input("Escoge una opción: "))

    match opcion:
        case 1:
            
            nombre=input("Escoge un nombre: ").lower()
            especie=input("Indica la especie: ").lower()
            edad=int(input("Indica la edad: "))
            peso=float(input("Indica el peso: "))
            sonido=input("Que sonido hace el animal: ").lower()

            animal=Animal(nombre, especie, edad, peso, sonido)

        case 2:
        case 3:
        case 4:
        case 5:
            salir=True
            print("Has salido del programa.")
        case other:
            print("Opción incorrecta, escoge del 1 al 5.")
