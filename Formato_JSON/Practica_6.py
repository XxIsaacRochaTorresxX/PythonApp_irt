import json

def Estudiantes():

    arch = "Estudiantes.txt"
    fh = open(arch, 'r') #Abrimos el archivo
    estudent = set()
    lista_estudent = fh.readlines()

    for i in lista_estudent[0:]:
        estudiante = i.split("\n")
        ctrl1 = estudiante[0][0:8]
        nombre = estudiante[0][8:]
        tupla_est = (ctrl1, nombre) #Hacemos las tuplas
        estudent.add(tupla_est)
    return estudent

def Materias():

    arch = "Kardex.txt"
    fk = open(arch, 'r') #abrimos el archivos
    materias= set()
    lista_materias = fk.readlines()

    for i in lista_materias[0:]:
        materia = i.split("\n")
        datos = materia[0].split('|')
        ctrl2 = datos[0]
        nomMat = datos[1]
        calif = int(datos[2])
        materias.add((ctrl2,nomMat,calif)) #Hacemos las tuplas
    return materias


kardex=[]

no_ctrl = input("¿Qúe número de control desea buscar?: ")
flag = False
prom = 0
cont = 0

for ren in Estudiantes(): # aquí mandarlo llamar
    if ren[0] == no_ctrl:
        k_alumno = {}
        print("Numero de control encontrado")
        k_alumno['Nombre'] = ren[1]
        for dat in Materias():
            if dat[0]== ren[0]:
                materia = {}
                materia["Nombre: "] = dat[1]
                materia["Promedio: "] = dat[2]
                kardex.append(materia)
                prom += int(dat[2]) #Se crean las estructuras
        k_alumno['Materias: '] = kardex
        k_alumno['Promedio General: '] = int(prom / len(kardex))
        flag = True

if not flag:
    print("Alumno no encontrado")
else:
    with open(no_ctrl+'.json', 'w') as file:
        json.dump(k_alumno, file, indent=4)

    '''

    6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
       indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
       {
            "Bandera": True,
            "Usuario": "Leonardo Martínez González",
            "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
       }

       ó

       {
            "Bandera": False,
            "Usuario": "",
            "Mensaje": "No existe el Usuario"
       }

       ó

        {
            "Bandera": False,
            "Usuario": "Leonardo Martínez González",
            "Mensaje": "Contraseña incorrecta"
       }
    '''