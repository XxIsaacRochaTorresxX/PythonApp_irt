import json

def Estudiantes():

    arch = "Estudiantes.prn"
    try:
        fh = open(arch, 'r') #Abrimos el archivo
        estudent = set()
        lista_estudent = fh.readlines()

        for i in lista_estudent[0:]:
            estudiante = i.split("\n")
            ctrl1 = estudiante[0][0:8]
            nombre = estudiante[0][8:]
            tupla_est = (ctrl1, nombre) #Hacemos las tuplas
            estudent.add(tupla_est)
    except:
        print("El archivo no existe")
        quit(0)
    return estudent

def Materias():
    try:
        arch = "Kardex.txt"
        fk = open(arch, 'r') #abrimos el archivos
        materias= set()
        lista_materias = fk.readlines()
        mat=[]
        for i in lista_materias[0:]:
            materia = i.split("\n")
            datos = materia[0].split('|')
            ctrl2 = datos[0]
            nomMat = datos[1]
            mat.append(nomMat)
            calif = int(datos[2])
            materias.add((ctrl2,nomMat,calif)) #Hacemos las tuplas
    except:
        print("No existe el archivo")
        quit(0)
    return materias


kardex=[]
alumnos=[]

def func_principal(*args):

    if len(args) == 0:
        print("No se ingresó ningún número de control")
        print(todos_alumnos())
    else:
        leng = args
        o= 0
        print(leng)
        for i in leng:
            no_ctrl = args[o]
            o=o+1
            flag = False
            prom = 0

            for ren in Estudiantes(): # aquí mandarlo llamar
                if ren[0] == no_ctrl:
                    k_alumno = {}

                    k_alumno['Nombre'] = ren[1]
                    for dat in Materias():
                     if dat[0]== ren[0]:
                            materia = {}
                            materia["Nombre: "] = dat[1]
                            kardex.append(materia)
                            prom += int(dat[2]) #Se crean las estructuras
                    k_alumno['Materias: '] = kardex
                    flag = True
            alumnos.append(k_alumno)
            if not flag:
                print("Alumno no encontrado")
            else:
                with open('Lista2'+'.json', 'w') as file:
                    json.dump(alumnos, file, indent=4)

archivo = []
def todos_alumnos():
    for ren in Estudiantes():  # aquí mandarlo llamar
            k_alumno = {}

            k_alumno['Nombre'] = ren[1]
            for dat in Materias():
                if dat[0] == ren[0]:
                    materia = {}
                    materia["Nombre: "] = dat[1]
                    kardex.append(materia)
            k_alumno['Materias: '] = kardex
            alumnos.append(k_alumno)

    with open('Lista General' + '.json', 'w') as file:
        json.dump(alumnos, file, indent=4)


############3

def todos_alumno():
    for x in Estudiantes():
        alumno1 = {}
        alumno1['Nombre'] = x[1]
        for y in Materias():
            if y[0] == x[0]:
                materia = {}
                materia["Nombre"] = y[1]
                kardex.append(materia)
        alumno1['Materias'] = kardex
        archivo.append(alumno1)
        #bandera = True

    with open('General.json', 'w') as file:
        json.dump(archivo, file, indent=4)


func_principal()