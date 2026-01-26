class Persona():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        self.activo=True
    
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_activo(self):
        return self.activo
    def set_nombre(self, n):
        self.nombre=n
    def set_edad(self,e):
        if e>=0:
            self.edad=e
        else:
            print("No puede poner edad negativa.")
    def set_activo(self, a):
        self.activo=a
    
    def dar_baja(self):
        if self.get_activo()==True:
            self.set_activo(False)
            return(f"La persona: {self.get_nombre()} se ha dado de baja")
        else:
            return(f"La persona con nombre {self.get_nombre()} ya estaba dada de baja")
    
    def dar_alta(self):
        if self.get_activo()==False:
            self.set_activo(True)
            return(f"La persona: {self.get_nombre()} se ha dado de alta")
        else:
            return(f"La persona con nombre: {self.get_nombre()} ya estaba dada de alta.")
    
    def mostrar_info(self):
        estado=""
        if self.get_activo()==True:
            estado="Activo"
        else:
            estado="Inactivo"
        return(f"Nombre: {self.get_nombre()} | Edad: {self.get_edad()} | Estado: {estado}")
    
class Socio(Persona):
    def __init__(self, nombre, edad, cuota):
        super().__init__(nombre, edad)
        self.tipo_cuota=cuota

    def get_tipo_cuota(self):
        return self.tipo_cuota
    
    def set_tipo_cuota(self, cuota):
        self.tipo_cuota=cuota

    def mostrar_info(self):
        return(f"{super().mostrar_info()} | Tipo cuota: {self.get_tipo_cuota()}")
    
class Entrenador(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad=especialidad
    
    def get_especialidad(self):
        return self.especialidad
    
    def set_especialidad(self, espe):
        self.especialidad=espe
    
    def mostrar_info(self):
        return (f"{super().mostrar_info()} | Especialidad: {self.get_especialidad()}")

class Gimnasio():
    def __init__(self):
        self.personas=[]

    def agregar_persona(self, persona):
        for i in self.personas:
            if i.get_nombre()==persona.get_nombre() and i.get_edad()==persona.get_edad():
                return (f"La persona: {persona.get_nombre()} ya estaba en la lista.")
        self.personas.append(persona)
        return(f"Se ha añadido a la lista la persona con nombre: {persona.get_nombre()}")
    
    def mostrar_personas(self):
        if self.personas:
            for i in self.personas:
                print(i.mostrar_info())
        else:
            print(f"Lista vacía, primero debes agregar personas a la lista.")
    
    def buscar_por_nombre(self, nombre):
        existe=False
        for i in self.personas:
            if i.get_nombre()==nombre:
                existe=True
                return(i)
        if existe==False:
            return None
      

gimnasio=Gimnasio()

persona=None

salir=False

lista_menu=["CREAR SOCIO", "CREAR ENTRENADOR", "MOSTRAR PERSONAS", "DAR DE BAJA", "DAR DE ALTA", "BUSCAR PERSONA", "SALIR"]

def menu():
    print("*************************")
    print("MENÚ PRINCIPAL")
    print("*************************")
    for clave, valor in enumerate(lista_menu, 1):
        print(f"Pulsa {clave}: {valor}")
    print("*************************")

while not salir:
    menu()

    opciones=int(input("Escoge una opción: "))

    match opciones:
        case 1:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")

            nombre=input("Indica el nombre: ").lower()
            edad=int(input("Indica la edad: "))
            cuota=input("Indica la cuota: ").lower()

            if edad>=0:
                persona=Socio(nombre, edad, cuota)
                print(gimnasio.agregar_persona(persona))
            else:
                print("Datos incorrectos, no puedes poner la edad negativa.")

        case 2:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            nombre=input("Indica el nombre: ").lower()
            edad=int(input("Indica la edad: "))
            especialidad=input("Indica la especialidad: ").lower()

            if edad>=0:
                persona=Entrenador(nombre, edad, especialidad)
                print(gimnasio.agregar_persona(persona))
            else:
                print("Datos incorrectos, no puedes poner la edad negativa.")

        case 3:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            gimnasio.mostrar_personas()

        case 4:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            if gimnasio.personas:

                nombre=input("Indica el nombre: ").lower()
                persona_correcta=gimnasio.buscar_por_nombre(nombre)
                if persona_correcta:
                    print(persona_correcta.dar_baja())
                else:
                    print(f"La persona: {nombre}, no está en la lista.")
            else:
                print(f"Lista vacía, primero debes agregar personas a la lista.")

        case 5:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            if gimnasio.personas:
                nombre=input("Indica el nombre: ").lower()
                persona_correcta=gimnasio.buscar_por_nombre(nombre)
                if persona_correcta:
                    print(persona_correcta.dar_alta())
                else:
                    print(f"La persona: {nombre}, no está en la lista.")
            else:
                print(f"Lista vacía, primero debes agregar personas a la lista.")

        case 6:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            if gimnasio.personas:
                nombre=input("Indica el nombre: ").lower()
                persona_correcta=gimnasio.buscar_por_nombre(nombre)
                if persona_correcta:
                    print(persona_correcta.mostrar_info())
                else:
                    print(f"La persona: {nombre}, no está en la lista.")
            else:
                print(f"Lista vacía, primero debes agregar personas a la lista.")

        case 7:
            print(f"Has seleccionado: {lista_menu[opciones-1]}")
            salir=True
            print("Has salido del programa")

        case other:
            print("Opción incorrecta, pulsa del 1 al 7.")










