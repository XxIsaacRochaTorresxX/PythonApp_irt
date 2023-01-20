# '''
# Tema: Entrada y Salida
# Fecha: 12 de septiembre del 2022
# Autor: Isaac Rocha Torres
#
# '''
#
# # Python soporta múltiples formas de formatear una cadena de caracteres. A continuación se describen:
# # 1. Formateo %. operador de interpolación
# # 2. format(). devuelve una versión formateada de una cadena de caracteres, usando substituciones desde argumentos
# # 3. formateo avanzado. Este método soporta muchas técnicas de formateo
# # 4. formateo por tipo
#
#
# # 1. Formateo %. operador de interpolación
#
#
#
#
# # formato con salida %.2
#
#
# #    Con esta sintaxis hay que determinar el tipo del objeto:
#
# #    %c = str, simple carácter.
# #    %s = str, cadena de carácter.
#
#
# #    %d = int, enteros.
# #    %f = float, coma flotante.
# #    %o = octal.
# #    %x = hexadecimal.
#
#
# # 2. format(). devuelve una versión formateada de una cadena de caracteres,
# #     usando substituciones desde argumentos
#
#
#
#
# # 3. fromateo avanzado. Este método soporta muchas técnicas de formateo
# #    A) Alinear una cadena de caracteres a la derecha en 30 caracteres
# estudiante = {
#     "Control": 100,
#     "Nombre": "Fernando Guerrero",
#     "Sexo": "M",
#     "Materia":[
#         {"Clave":100,"Nombre":"BASE DE DATOS","Promedio": 90}
#     ],
#     "altura":1.91
# }
# print("Nombre %s con el numero de control %d tiene una altura de %f"%(estudiante["Nombre"],estudiante["Control"],estudiante["altura"]))
# print("El promedio es %s"%((estudiante["Materia"][0])["Promedio"]))
# #    B) Alinear una cadena de caracteres a la izquierda en 30 caracteres
# #        (crea espacios a la derecha), con la siguiente sentencia
#
#
# #    C) Alinear una cadena de caracteres al centro en 30 caracteres.
#
#
# #    D) Truncamiento a 9 caracteres.
#
#
# # 4. Formateo por tipo
# #    s para cadenas de caracteres (tipo str).
# #    d para números enteros (tipo int).
# #    f para números de coma flotante (tipo float).
#
# # Formateo de numeros enteros rellenados con espacios
#
#
# # Formateo de numeros rellenados con ceros
#
#
# # Formateo de números flotantes, rellenados con espacios


'''
# Carrito de compra:
#    nombre_producto
#    precio
#    cantidad
#    descuento


#    NOMBRE PRODUCTO     PRECIO      CANTIDAD        SUBTOTAL



1. Mostrar el contenido del carrito alineado
2. Eliminar un producto del carrito
3. Regresar un JSON con una bandera si el carrito tiene productos
'''
carrito = {
            1:['Monitor Samsumng 27 pulgadas     ', 4589.98, 1, 3],
            2:['Tableta 10 pulgadas marca X      ', 2500.9, 1, 3],
            3:['Mouse gamer 3d                   ', 3400.5, 1, 3],
            4:['Computadora de escritorio lenovo ', 1589.98, 1, 3],
            5:['Renovación Antivirus X           ', 1057, 2, 3]
            }
def Eliminar(carrito2):
    art=int(input("¿Cual producto desea eliminar? (Especifique el numero): "))
    carrito2.pop(art)
    carrito = carrito2
    menu_productos()
    return carrito
def menu_productos():
    print("{:^30}".format("NOMBRE PRODUCTO"),"{:^15}".format("PRECIO"),"{:^10}".format("CANTIDAD"),"{:^10}".format("SUBTOTAL"))

    # carrito = {1:['Monitor Samsumng 27 pulgadas     ', 4589.98, 1, 3],
    #             2:['Tableta 10 pulgadas marca X      ', 2500.9, 1, 3],
    #             3:['Mouse gamer 3d                   ', 3400.5, 1, 3],
    #             4:['Computadora de escritorio lenovo ', 1589.98, 1, 3],
    #             5:['Renovación Antivirus X           ', 1057, 2, 3]
    #             }

    for i in carrito:
        print(carrito[i][0],"{:^10}".format( carrito[i][1]), "{:^16}".format( carrito[i][2]), "{:^4}".format( carrito[i][3]))
def Esta_Vacio():
    if not bool(carrito):
        banderilla = False
        msg = "No hay productos en el carrito"
    else:
        banderilla = True
        msg = "Si hay productos en el carrito"
    bandera = {"Bandera": banderilla, "Mensaje": msg}
    return bandera

opcion = 0
while opcion != 5:
    opcion = int(input("Que quieres hacer?\n1.-Limpiar Carrito 2.-Verificar si esta vacio en JSON\n3.-Eliminar un producto 4.-Mostrar el contenido del carrito\n5.-Salir\n"))
    match(opcion):
         case 1:
             carrito.clear()
         case 2:
             print(Esta_Vacio())
         case 3:
             Eliminar(carrito)
         case 4:
            menu_productos()

