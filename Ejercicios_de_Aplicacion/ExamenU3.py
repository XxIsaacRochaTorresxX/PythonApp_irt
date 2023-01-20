'''
Isaac Rocha Torres
'''

import json
from crudmysql import MySQL
from caja import Password
from env import variables
ar=[]
tupla=[]

#///el metodo está más abajo///#

def Alumnos():
    archivo = open("Estudiantes.prn", "r")
    for x in archivo:
        ar.append(x[0:8])
        ar.append(x[8:].replace("\n",""))
        tupla.append(tuple(ar))
        ar.clear()
    archivo.close()
    #print(tupla)
    # print(tupla)
    return tupla
Coj=set()
def Materias():
    MA = open("Kardex.txt", "r")
    matr = []
    lis = []

    for x in MA:
        lis = x.split("|")
        matr.append(lis[0])
        matr.append(lis[1])
        matr.append(lis[2].replace("\n", ""))
        Coj.add(tuple(matr))
        matr.clear()
    # print(Coj)
    MA.close()
    return (Coj)
def Usuarios():          #Ejercicio 1
    archivo = open("usuarios.txt", "r")
    usuarios = set()
    for linea in archivo:
        d2 = linea.split(" ")
        usuarios.add((d2[0], d2[1], d2[2]))
    return usuarios

def cargar_datos():
    obj_estudiante=MySQL(variables)
    lista_estudiante=Alumnos()
    print(lista_estudiante)
    obj_estudiante.conectar_mysql()
    for ctrl,nom in lista_estudiante:
        sql=f"INSERT INTO estudiantes() values('{ctrl}','{nom}');"
        print(sql)
        obj_estudiante.consulta_sql(sql)
    # print(lista_estudiante)
    obj_estudiante.desconectar_mysql()

def cargar_Kardex():
    obj_estudiante = MySQL(variables)
    lista_karnex=Materias()
    #print(Materias())
    obj_estudiante.conectar_mysql()
    for ctrl,NomMateria,cali in lista_karnex:
        sql = f"INSERT INTO kardex(control,materia,calificacion) values('{ctrl}','{NomMateria}',{cali});"
        obj_estudiante.consulta_sql(sql)
        print(sql)
    obj_estudiante.desconectar_mysql()


#////////////SELECCIONES///////////////#

kardex=[]
alumnos=[]

def consultar_estudiante(ctrl):
    obj_MySQL = MySQL(variables)  # *********************************
    print(" == JSON GENERADO ==")
    ctrl = ctrl

    sql_materias = "SELECT E.nombre, K.materia, K.calificacion " \
                   "FROM estudiantes E, kardex K " \
                   f"WHERE E.control = K.control and E.control='{ctrl}';"
    #print(sql_materias)

    resp = obj_MySQL.consulta_sql(sql_materias)
    if resp:
        #print("Estudiante: ", resp[0][0])
        k_alumno = {}

        for mat in resp:
            k_alumno['Nombre'] = mat[0]
            materia = {}
            materia["Nombre: "] = mat[1]
            materia["calificacion: "] = str(mat[2])
            kardex.append(materia)
        k_alumno['Materias: ']= kardex
        #print("Materia: ", mat[1], " Calificación: ", mat[2])
    else:
        print(f"El estudiante con Número de control: {ctrl} NO existe")
    alumnos.append(k_alumno)
    with open('Final' + '.json', 'w') as file:
        json.dump(alumnos, file, indent=4)



def solicitar_usuario():
    user = input("Ingresa el número de control a utilizar: ")
    return user


#///CONSULTAR/#
consultar_estudiante(solicitar_usuario())
