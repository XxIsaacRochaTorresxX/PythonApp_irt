'''
Tema: Gestión de excepciones
Fecha: 19 de septiembre del 2022
Autor: Isaac Rocha Torres
'''
#    En algunas ocasiones nuestros programas pueden fallar ocasionando su detención.
#    Ya sea por errores de sintaxis o de lógica, tenemos que que ser capaces de detectar esos
#    momentos y tratarlos debidamente para prevenirlos.

#    Los errores detienen la ejecución del programa y tienen varias causas. Para poder estudiarlos
#    vamos a provocar algunos intencionadamente.
#    Tipos: Errores de sintaxis, de nombre y semánticos.

# 1. Excepciones: Las excepciones son bloques de código que nos permiten continuar
#    con la ejecución de un programa pese a que ocurra un error.

#    Se trata de una forma de controlar el comportamiento de un programa
#    cuando se produce un error.

# 2. Sintaxis:
'''
try:
        # Intenta ejecutar la instrucion(es)
    except:
        # Si ocurre un error aqui se trata
    else:
        # Si entra al bloque try se ejecuta este bloque de código
    finally: 
        # Siempre se ejecutara este código
'''
'''
# Los ejemplos más comunes que podemos nombrar de excepciones:
#
# 1. Tratar de convertir a entero un string que no contiene valores numéricos. (ValueError)
while True:
    try:
        num = int(input("Dame un número: "))
    except ValueError:
        print("Por favor, teclea un número..")
    else:
        print(f"El número ingresado es: {num}")
        if num%2 == 0:
            print("El número es par")
        else:
            print(f"El número es impar")
        break



# 2. Tratar de dividir por cero.

while True:
    try:
        num = int(input("Dame el primer valor: "))
        num1 = int(input("Dame el segundo valor: "))
        res = num / num1
        
    except ZeroDivisionError:
        print("División entre 0 imposible")
    else:
        print(f"El resultado es: {res}")
        break
'''
'''
while True:
    try:
        num = int(input("Dame el primer valor: "))
        num1 = int(input("Dame el segundo valor: "))
        res = num / num1

    except ZeroDivisionError:
        print("División entre 0 imposible")
    except ValueError:
        print("Por favor, teclea un número..")
    else:
        print(f"El resultado es: {res}")
        if res%2 == 0:
            print("El número es par")
        else:
            print(f"El número es impar")
        break
        break


# 3. Abrir un archivo de texto inexistente o que se encuentra bloqueado por otra aplicación.
PATH="C:/Users/Isaac RT/PycharmProjects/UnidadII/"


arch = "CPdescarga.txt"
#arch = None
try:
    arch = open(PATH + arch, "r")
except Exception:
    print(f"No existe el archivo: {arch}")
else:
    print("\n")
    print(arch, f"Tiene {len(arch.readlines())} líneas")
finally:
    if arch:
        arch.close()

'''

# 4. Conectar con un servidor de bases de datos que no se encuentra activo.
'''
# 4. Conectar con un servidor de bases de datos de MySQL que no se encuentra activo.
#      Importar mysql-connector
#      pip install mysql-connector
'''

import  mysql.connector

try:
    conexion = mysql.connector.connect(host="localhost",user="root", passwd="1234", database="nombre_base")
except  mysql.connector.errors.InterfaceError:
    print("No se puede establecer la conexion a la base de datos...")
else:
    cursor1 = conexion.cursor()
    try:
        cursor1.execute("SELECT productoNombre FROM products WHERE idCategoria = 3")
    except mysql.connector.errors.ProgrammingError:
        print("No existe el campo o el nombre de la tabla...")
    else:
        for p in cursor1:
            print(p)
    finally:
        if cursor1:
            cursor1.close()
finally:
    if conexion:
        conexion.close()

