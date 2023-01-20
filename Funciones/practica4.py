'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Isaac Rocha Torres
'''

'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''
from funciones_practica4 import *

pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]


ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

def menu_principal():
    while True:
        print(" =======================  Menú Principal =================================")
        print(" 1. Agregar pasajero ")
        print(" 2. Agregar ciudad ")
        print(" 3. Ciudad a la que viaja un pasajero ")
        print(" 4. Cantidad de pasajeros que viajan a la Ciudad ")
        print(" 5. A que estado viaja el pasajero ")
        print(" 6. Cantidad de pasajeros que viajan a un Estado ")
        print(" 7. Salir ")

        opcion = int(input("Dame tu opcion: "))

        # Evaluar la variable opcion
        if opcion == 1:
            print (" Agregar Pasajeros ")
            agregar_pasajeros(pasajeros)
            print(pasajeros)
        elif opcion == 2:
            print(" Agregar Ciudades ")
            agregar_ciudades(ciudades)
            print(ciudades)
        elif opcion == 3:
            print(" Ciudad a la que viaja el pasajero ")
            clave = int(input("Dame la clave del pasajero: "))
            ciudad = buscar_ciudad(clave,pasajeros)
            print(" El Pasajero: ", clave, " viaja a la ciudad de: ", ciudad )
        elif opcion == 4:
            print(" Cantidad de pasajeros que viajan a una ciudad ")
            ciudad = input ("Dame la ciudad: ")
            print("La cantidad de pasajeros que viajan a la ciudad: ", ciudad, " son: ",contar_pasajeros(ciudad,pasajeros))
        elif opcion == 5:
            print(" Estado al que viaja un pasajero " )
            clave = int(input("Dame la clave del pasajero: "))
            print(" El estado al que viaja es: ", regresa_estado(clave, pasajeros, ciudades))
        elif opcion == 6:
            pass
        elif opcion == 7:
            break
        else:
            print(" Opción no válida ")

# Mandar llamar el menu principal
menu_principal()


'''@isaakiin'''