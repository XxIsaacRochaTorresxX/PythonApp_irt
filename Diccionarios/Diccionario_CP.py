'''
Tema: Diccionarios, archivos y formato JSON
Fecha: 02 de septiembre del 2022
Autor: Isaac Rocha Torres
'''

'''
Ejercicio: Crear un diccionario con los códigos postales y su localidad del estado de San Luis Potosi,
           para ello descargue la tabla de códigos postales de la siguiente dirección: 
           https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx

           el formato del diccionario  tendra la forma:
           {109159: {'CP': '78000', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, 
           109160: {'CP': '78037', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, . . . }

           Genere una lista con los VALORES del diccionario anterior.
           Guarde en un archivo con formato JSON los resultados

           Consideraciones:
           1. El método split regresa un arreglo al separar una cadena en subcadenas.
           2. El municipio se encuentra en la posición 4.
           3. El estado se llama: "San Luis Potosí"
'''
import json

arch = open("CPdescarga.txt") #Abrimos el arch txt que contiene los códigos
renglones = arch.readlines() #lo convertimos en lines para separar
lista = {} # se crea la lista con la que se hará el json

for ren in renglones[2:]:
    ubicacion = {}
    ubi = ren.split(sep='|') #la separación para identificar los elementos es | de acuredo al arch
    if ubi[4] == 'San Luis Potosí': #Solamente nos interesa los que sean de San luis Potosi
        ubicacion["Codigo Postal"] = ubi[6]
        ubicacion["Municipio"] = ubi[3]
        ubicacion["Estado"] = ubi[4]
        lista[ubi[0]] = ubicacion #Agregamos
print(lista)

with open("lista.json", "w") as file: #Realizamos el json con la lista generada
    json.dump(lista, file, indent=4)
