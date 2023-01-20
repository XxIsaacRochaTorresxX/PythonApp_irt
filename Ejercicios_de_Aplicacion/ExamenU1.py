

import json
def estudiantes():
    try:
        estudiantes = open("Estudiantes.prn","r")
        conjunto_estudiantes= set()
        lista_estudiantes = estudiantes.readlines()
        for x in lista_estudiantes[0:]:
            estudiante = x.split("\n")
            no_control = estudiante[0][0:8]
            nombre = estudiante[0][8:]
            tupla = (no_control, nombre)
            conjunto_estudiantes.add(tupla)
        print(conjunto_estudiantes)
        return conjunto_estudiantes
    except  FileNotFoundError:
        print("Archivo no encontrado")

def materias():
    materias = open("Kardex.txt","r")
    conjunto_materias= set()
    lista_materias = materias.readlines()
    for x in lista_materias[0:]:
        materia = x.split("\n")
        datos = materia[0].split('|')
        no_control2 = datos[0]
        nombre_materia = datos[1]
        calificacion = int(datos[2])
        conjunto_materias.add((no_control2,nombre_materia,calificacion))
    return  conjunto_materias
conjunto_materias = materias()
conjunto_estudiantes = estudiantes()
def regresa_materias_control(*args):
    listaMaterias = []
    try:
        argumentos = int(len(args));
        archivo = []
        if argumentos != 0 :
            no_control = args[0];
            for i in range(len(no_control)):
                print(no_control[i])
                materias=[]
                prom = 0
                contador = 0
                bandera = False
                for x in conjunto_estudiantes:
                     if x[0] == no_control[i]:
                         alumno1 = {}
                         print("Numero de control encontrado")
                         alumno1['Nombre'] = x[1]
                         for y in conjunto_materias:
                             if y[0]== x[0]:
                                 materia = {}
                                 materia["Nombre"] = y[1]
                                 materias.append(materia)
                         alumno1['Materias'] = materias
                         archivo.append(alumno1)
                         bandera = True
                if not bandera:
                 print("Alumno no encontrado")
                else:

                    print("Este es el archivo")
                    print(archivo)
                    with open('alumno.json', 'w') as file:
                        json.dump(archivo, file, indent=4)
        else:
            materias = []
            for x in conjunto_estudiantes:
                    alumno1 = {}
                    print("Numero de control encontrado")
                    alumno1['Nombre'] = x[1]
                    for y in conjunto_materias:
                        if y[0] == x[0]:
                            materia = {}
                            materia["Nombre"] = y[1]
                            materias.append(materia)
                    alumno1['Materias'] = materias
                    archivo.append(alumno1)
                    bandera = True
                    print("Este es el archivo")
                    print(archivo)
                    with open('alumno.json', 'w') as file:
                        json.dump(archivo, file, indent=4)
    except Exception:
        print("Se genero una excepcion desconocida")




regresa_materias_control()