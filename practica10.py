'''
Tema: Funciones
Fecha: 22 de septiembre del 2022
Autor: Isaac Rocha Torres
Link: https://www.youtube.com/watch?v=_nAuo8JsAcM  *args y **kwargs
Link: https://www.youtube.com/watch?v=8JpE9CwfOJc funciones lambda
'''

'''
Paso de Parámetros por valor o referencia 
'''
lista = ["Juan", "Pedro", "Luis", "Karina"]

# def imprimirlista(lista):
#     for nom in lista:
#         print(nom)
#     lista[0]="Juanito"
# imprimirlista(lista)

'''
Funciones con argumentos con valor por defecto
'''
# import mysql.connector
# lista = {}
#
# def conectarmysql(host="locslhost123",user="root",passw="",bd="opensource"):
#     try:
#         conexion = mysql.connector.connect(host=host,user=user,password=passw,database=bd)
#     except Exception as Error:
#         print("Error: ",Error)
#     else:
#         #Crear consulta a BD
#         mi_cursor = conexion.cursor()
#         try:
#             mi_cursor.execute("select id, nombre, precio from productos")
#         except mysql.connector.errors.ProgrammingError as e:
#             print("Error en la consulta: ",e)
#         except Exception as error:
#             print("ERROR: ",error)
#         else:
#             for reg in mi_cursor:
#                 clave, nombre,precio = reg
#                 prod = {}
#                 prod["ID: "] = clave
#                 prod["Nombre: "] = nombre
#                 prod["Precio: "] = str(precio)
#                 lista.append(prod)
#                 print(reg)
#             mi_cursor.close()
#             print(lista)
#         conexion.close
#
#
# conectarmysql(host="localhost")

# import mysql.connector
# lista = {}
#
# def conectarmysql(host,user,passw,bd):
#     try:
#         conexion = mysql.connector.connect(host=host,user=user,password=passw,database=bd)
#     except Exception as Error:
#         print("Error: ",Error)
#     else:
#         return conexion
#
# def datos(con,sql):
#     try:
#         mi_cursos = con.cursor()
#         mi_cursos.execute(sql)
#     except mysql.connector.errors.ProgrammingError as e:
#         print("Error en la consulta: ", e)
#     except Exception as error:
#         print("ERROR: ", error)
#     else:
#         for reg in mi_cursos:
#             clave, nombre, precio = reg
#             prod = {}
#             prod["ID: "] = clave
#             prod["Nombre: "] = nombre
#             prod["Precio: "] = str(precio)
#             lista.append(prod)
#             print(reg)
#         mi_cursos.close()
#     con.close
#
#
# cbd = conectarmysql(host="localhost")
# datos(cbd,"select nombre, precio from productos where precio < 5000")
'''
Funciones que retornan varios valores
'''
#def suma(a,b):
#    return a+b,a,b
#x,y,z = suma(10,20)
#print(x)
#print(y)
#print(z)



'''
Funciones lambda o anónimas, son de una sola linea, solo las ocupamos una sola vez.
1. Definir una función lambda con un ejemplo
saludar = lambda nombre: return f"Hola {nombre}"
2. Llamada de otras funciones dentro de una función lambda
3. Ordenar una lista
3. Pasarlas como parámetros a filter y map. 
   filter filtra elementos, toma dos parámetros: (una_funcion, lista)
   map por cada elemento de la lista llama al elemento y regresa el elemento ya modificado
'''

#saludo= lambda nombre: f"hola{nombre}"
#print(saludo("Juan"))

# Si es menor de edad regresar  edad = a 18 de lo contrario regresar la edad

#lista =[23,18,21,12,34,45,12,10,23]
#print(lista)

#lista_mayores = lambda  e:e if e>=18 else False

#for elemento in lista:
#    print(lista_mayores(elemento))
# Regresar los estudiantes aprobados, de lo contrario regresar un False


#def cuadrado(num):
 #   return num*num

#elevar_cuadrado = lambda x: cuadrado(x)

#for e in lista:
#    print(f"El cuadrado de {e} es {elevar_cuadrado(e)}")


lista = [(500, "Juan José", 18,98.8),
         (200, "Antonio", 26,68.8),
         (100, "Zacarias", 17, 100),
         (400, "Jeremias", 19, 00.8),
         (300, "Beatriz", 20, 87.8),
         ]

#print(lista)
#lista.sort()
#print(lista)

#lista.sort(key=lambda t:t[3])
#print(lista)

#aprovado=lambda t:t if t[3]>=69.0 else False

#for t in lista:
#    print(aprovado(t))


#lista_aprovados = list(filter(lambda t:t if t[3]>69.0 else False, lista))
#lista_NOaprovados = list(filter(lambda t:t if t[3]<69.0 else False, lista))
#print(lista_aprovados)
#print(lista_NOaprovados)

'''
def modificar_promedio(t):
    t[3]=70.0
    return t



print("antes de modificar la lista: ", lista)
lista_modificados = list(map(lambda t:t if t[3]>69.0 else modificar_promedio(t) , lista))
print(lista_modificados)
'''


'''
Argumentos arbitrarios. Se utiliza cuando no sabemos la cantidad de argumentos
que vamos a recibir
'''
#def funcion_n_parametros(*args):
#    for i in args:
#        print(type(i), "-->", i)

#funcion_n_parametros(10,48,True,89.9, 'Cadena', "Otra cadena")
'''
def descargar_archivo(tipo, *args):
    numero_args = len(args)
    if tipo == "video":
        if numero_args == 0:
            print(f"El formato seleccionado \n Tipo de archivo: {tipo}")
        elif numero_args == 1:
            print(f"El formato seleccionado \n Tipo de archivo: {tipo} \n Resolución:{args[0]}")
        elif numero_args == 2:
            print(f"El formato seleccionado \n Tipo de archivo: {tipo} \n Resolución:{args[0]} \n Fotogramas:{args[1]}")
    elif tipo == 'audio':
        print(f"El formato seleccionado \n Tipo de archivo: {tipo}")
    else:
        print(f"El formato no es válido")


descargar_archivo("video")
descargar_archivo("video", 488)
descargar_archivo("video",488, 32)
descargar_archivo("audio")

descargar_archivo("otro")
'''
'''
 y keyword arguments **kwargs es un diccionario con número de elementos arbitrario
'''

#def mi_filtro(ciudad, estado, cp):
#    return f"SELECT * FROM CLIENTES WHERE ciudad ='{ciudad}' AND estado='{estado}' AND cp={cp}"

def mi_filtro(**kwargs):
    query = "SELECT * FROM clientes"
    i=0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += f"{key} = '{value}'"
    query += ";"

    return query

print(mi_filtro(ciudad='Jiquilpan', cp=59518))