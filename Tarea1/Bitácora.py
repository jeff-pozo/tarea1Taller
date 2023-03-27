#dependencias
import datetime

#Funcion Principal
def main():

    #Menu principal
    print("--------------------------------------------------")
    print("Bienvenido")
    print("Elija una Opción")
    print("Opción 1: Registro de Actividades")
    print("Opción 2: Búsquedas ")
    print("Opción 3: Cantidad de Mensajes")
    print("Opción 4: Guardar mensajes")
    print("Opción 9: Salir")
    opcion = int(input("Elige una Opción: "))
    
    #Sub Menu 1
    if opcion == 1:
        return menu1()
    #Sub Menu 2
    elif opcion ==2:
        print("Opción 21: Buscar por usuario")
        print("Opción 22: Buscar por aplicación")
        print("Opción 23: Buscar por fecha")
        print("Opción 24: Retornar")
        opcionSub2 = int(input("Elija una opción: "))
        if opcionSub2 == 21:
            pass
        elif opcionSub2 == 22:
            pass
        elif opcionSub2 == 23:
            pass
        elif opcionSub2 == 24:
            return main()

    #Funcionalidad 3
    elif opcion == 3:
        pass

    #Funcionalidad4
    elif opcion == 4:
        pass

    #Salir
    elif opcion == 9:
        return "Adios"
    return main()

#Menu 1
"""
Nombre:menu1
Funcion: Ejecutar el menu1, registro de actividades
"""
def menu1():
    print("--------------------------------------------------")
    print("Opción 11: Registrar actividad")
    print("Opción 12: Borrar Actividad")
    print("Opción 13: Modificar actividad")
    print("Opción 14: Ver todas las actividades")
    print("Opción 15: Retornar")
    opcionSub1 = int(input("Elija una opción: "))
    if opcionSub1 == 11:
        return opcion11()
            
    elif opcionSub1 == 12:
        print("Eliminar Actividad")
        codex= input("Ingrese el código de la actividad que desea elminar: ")
        borrarRegistro(codex)
    elif opcionSub1 == 13:
        pass
    elif opcionSub1 == 14:
        pass
    elif opcionSub1 == 15:
        return main()

#Registrar actividad
"""
Nombre: opcion11
Entradas: 0
Funcion: ejcutar la opcion de registrar y hacer validaciones
Restricciones: El tamaño maximo de usuario, aplicación, mensaje deben ser 8,16,50 caracterese respectivamente
"""
def opcion11():
    print("Registrar Actividad")
    user= input("Ingrese el Usuario: ")
    if len(user) > 8:
        print("Error, tamaño maximo para Usuario: 8 caracteres")
        return opcion11()
    app = input("Ingrese el nombre de Aplicación: ")
    if len(app) > 16:
        print("Error, tamaño maximo para Aplicación: 16 caracteres")
        return(opcion11)
    msj = input("Ingrese el Mensaje: ")
    if len(msj) > 50:
        print("Error, tamaño maximo para mensaje: 50 caracteres")
        return opcion11()
    registrarActividad(user, app, msj)
    return menu1()

"""
Nombre:registrarActividad
Entradas:usuario, aplicacion, mensaje
Salida:Escritura de registro en bitacora
"""
def registrarActividad(Usuario, Aplicacion, Mensaje):
    code = generarCodigo()
    fecha = datetime.datetime.now()
    bitacora = open("Bitácora.txt", "a")
    registro = str(fecha.strftime("%d-%m-%Y %H:%M:%S")) + ", " + str(Usuario) + ", " + str(Aplicacion) + ", " + str(Mensaje) + ", " "Codigo:"+ str(code)
    bitacora.write(str(registro) + "\n")
    bitacora.close

"""
Nombre: generarCodigo
Funcion: generar codigo automatico
"""
def generarCodigo():
    codigo = 0
    fila = []
    texto = open("Bitácora.txt", encoding = 'utf- 8', mode ='r')
    if texto.readline() != "":
        for elemento in texto:
            fila = elemento.split(", ")
        fila = fila[4].split(":")
        codigo = (int(fila[1]) + 1)
    else:
        codigo = 1
    return codigo

#Borrar Actividad
def borrarRegistro(codigo):
    texto = open("Bitácora.txt", encoding = 'utf- 8', mode ='r')
    fila = []
    celda = []
    valor = 0
    nuevoTex = []
    for elemento in texto:
        #print(elemento)
        fila = elemento.split(", ")
        #print(fila)
        celda = fila[4].split(":")
        valor = int(celda[1])
        #print(valor)
        if valor == codigo:
            pass
        else:
            nuevoTex += [elemento]
    texto.close()
    sobreEscribir(nuevoTex)

def sobreEscribir(newTex):
    texto = open("Bitácora.txt", mode="w")
    for elemento in newTex:
        texto.writelines(str(elemento))
    texto.close()

#ModificarActividad
def encontrarActividad(codigo,user,app, msj,):
    texto = open("Bitácora.txt", mode="r")
    nuevaLista = []
    filaNueva = []
    fila = []
    celda = []
    valor = 0
    tiempo = []
    fecha = ""
    hora = ""
    usuario = ""
    aplicacion = ""
    mensaje = ""
    for elemento in texto:
        fila = elemento.split(", ")
        celda = fila[4].split(":")
        tiempo = fila[0].split(" ")
        fecha = tiempo[0]
        hora = tiempo[1]
        usuario = fila[1]
        aplicacion = fila[2]
        mensaje = fila[3]
        valor = int(celda[1])
        if valor == codigo:
            fila[1] = fila[1].replace(usuario,user)
            fila[2] = fila[2].replace(aplicacion, app)
            fila[3] = fila[3].replace(mensaje, msj)
            filaNueva = fila[0] + ", " + fila[1] +", "+ fila[2]+ ", " +fila[3] +", "+ fila[4]
            nuevaLista += [filaNueva]
        elif valor != codigo:
            nuevaLista += [elemento]
    sobreEscribir(nuevaLista)

#Ver todas la actividades
def imprimirActividades():
    texto = open("Bitácora.txt", mode="r")
    for elemento in texto:
        print(elemento)

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