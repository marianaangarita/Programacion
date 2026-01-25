'''
Contexto
Una empresa de alquiler de vehículos necesita un sistema para gestionar su flota. La aplicación debe aplicar los principios de la Programación Orientada a Objetos, herencia y encapsulación.

Requisitos del Programa
1. Clase Base: Vehiculo (Abstracción y Encapsulación)
Crea una clase llamada Vehiculo que represente cualquier medio de transporte de la empresa.

Atributos:

marca (string)

modelo (string)

matricula (string, debe ser único conceptualmente)

alquilado (bool, inicialmente False)

Métodos:

__init__: Inicializa todos los atributos.

Getters y Setters: Para los atributos que consideres necesarios.

alquilar(): Cambia el estado a alquilado. Si ya está alquilado, debe indicarlo.

devolver(): Cambia el estado a disponible.

mostrar_info(): Devuelve una cadena con el formato: "Vehículo: [Marca] [Modelo] | Matrícula: [Matricula] | Estado: [Alquilado/Disponible]".

2. Herencia Simple: Clases Coche y Moto
Crea dos clases hijas que hereden de Vehiculo.

Clase Coche

Atributo adicional: num_puertas (int).

Métodos: Sobrescribe mostrar_info() para incluir el número de puertas.

Clase Moto

Atributo adicional: cilindrada (int, cc).

Métodos: Sobrescribe mostrar_info() para incluir la cilindrada.

3. Clase de Gestión: Flota (Composición)
Crea una clase Flota que gestione la lista de vehículos.

Atributos: lista_vehiculos (lista vacía al inicio).

Métodos:

agregar_vehiculo(vehiculo): Añade un objeto a la lista.

mostrar_flota(): Recorre la lista y muestra la información de cada vehículo.

buscar_por_matricula(matricula): Busca un vehículo y muestra sus datos.

4. Menú Interactivo
El programa debe ejecutarse mediante un menú en consola (dentro de un while) que permita:

Crear y registrar un Coche.

Crear y registrar una Moto.

Mostrar toda la flota.

Alquilar un vehículo (buscando por matrícula).

Devolver un vehículo (buscando por matrícula).

Salir.
'''

