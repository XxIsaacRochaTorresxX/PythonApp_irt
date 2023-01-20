
# Insertar pasajeros
def agregar_pasajeros(pasajeros):
    clave = int(input("Dame la Clave del pasajero: "))
    nombre = input ("Dame el Nombre del Pasajero: ")
    ciudad = input("Dame la Ciudad")
    pasajeros.append((nombre,clave,ciudad))

# Insertar ciudades
def agregar_ciudades(ciudades):
    ciudad = input("Dame la Ciudad: ")
    estado = input("Dame el Estado: ")
    ciudades.append((ciudad,estado))

# Funcion que regresa la ciudad dada la clave del pasajero
def buscar_ciudad(clave,pasajeros):
    for pasajero in pasajeros:
        if pasajero[1] == clave:
            return pasajero[2]
    return " No existe viaje "

# Regresar el número de pasajeros que viajan a una ciudad
def contar_pasajeros(ciudad,pasajeros):
    contador = 0
    for pasajero in pasajeros:
        if pasajero[2] == ciudad:
            contador += 1
    return contador

# Regresa el estado al que viaja un pasajero
def regresa_estado(clave, pasajeros, ciudades):
    for p in pasajeros:
        if p[1] == clave:
            for c in ciudades:
                if c[0] == p[2]:
                    return c[1]
    return " Pasajero no existe "