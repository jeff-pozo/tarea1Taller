from datetime import datetime

#Búsquedas
"""
Nombre: busquedaUsuario,
Entrada:parte del nombre de usuario (busqueda),
Salida:registros con esa parte de nombre de usuario,
Restricciones: el parametro de entrada no debe de estar vacia
"""

def busquedaUsuario(busqueda):
    text = leerArchivo("tPrueba.txt")
    fila = []
    usuario = ""
    for linea in text:
        fila = linea.split(", ")
        usuario = fila[1]
        if compararString(usuario, busqueda) == True:
            print(linea)


"""
Nombre: busquedaAplicación,
Entrada: parte nombre de aplicación(aplicacion),
Salida: registros con esa parte de nombre de aplicación,
Restricciones:parametro de entrada no debe estar vacia
"""

def busquedaAplicacion(busqueda):
    text = leerArchivo("tPrueba.txt")
    fila = []
    app = ""
    for linea in text:
        fila = linea.split(", ")
        app = fila[2]
        if compararString(app, busqueda) == True:
            print(linea)

"""
Nombre: busquedaFecha
Entrada: rango de fechas (fechaInicial/fechaFinal)
Salida: registros dentro de ese rango de fechas
Restricciones: ningun parametro puede estar vacío
"""

def busquedaFecha(fechaInicial, fechaFinal):
    text = leerArchivo("tPrueba.txt")
    fila = []
    celda = []
    fecha = []
    fecha1 = datetime.strptime(fechaInicial, "%d-%m-%Y")
    fecha2 = datetime.strptime(fechaFinal, "%d-%m-%Y")
    for linea in text :
        fila = linea.split(", ")
        celda = fila[0]
        fecha =  celda.split(" ")[0]
        fecha = datetime.strptime(fecha, "%d-%m-%Y")
        if fecha >= fecha1 and fecha <= fecha2:
            print(linea)


"""
Nombre: leerArchivo
Entrada: nombreArchivo
Salida: contenidoArchivo
Restricciones: parametro no puede estar vacio
"""

def leerArchivo(archivo):
    texto = open(archivo, encoding="utf-8", mode="r")
    return texto



#comparar string

def compararString(cadena, aBuscar):
    contadorB = 0
    for i in aBuscar:
        contadorB += 1
    while cadena != "":
        if cadena[:contadorB] == aBuscar:
            return True
        cadena = cadena[1:]
    return False

"""
Nombre:cantidadMensajes,
Entrada: 
Salida:
Restricciones:   
"""

def cantidadMensajes():
    text = leerArchivo("tPrueba.txt")
    contador = 0
    for elemento in text:
        contador +=1
    return contador

"""
Nombre:guardarMensajes,
Entradas: fechaInicial, fechaFinal, nombreArchivo
Salida: archivo con las activdades dentro de los rangos
"""

def guardarMensajes(fInicial, fFinal, nArchivo):
    text = leerArchivo("tPrueba.txt")
    fila = []
    celda = []
    fecha = []
    fecha1 = datetime.strptime(fInicial, "%d-%m-%Y")
    fecha2 = datetime.strptime(fFinal, "%d-%m-%Y")
    for linea in text :
        fila = linea.split(", ")
        celda = fila[0]
        fecha =  celda.split(" ")[0]
        fecha = datetime.strptime(fecha, "%d-%m-%Y")
        if fecha >= fecha1 and fecha <= fecha2:
            crearArchivo(nArchivo, linea)



def crearArchivo(archivo, actividad):
    nuevoArchivo = open(archivo, encoding= "utf-8", mode="a")
    nuevoArchivo.writelines(actividad)
    nuevoArchivo.close()




