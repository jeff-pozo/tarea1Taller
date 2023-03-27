import datetime

ahora = datetime.datetime.now()

print(ahora)

def registrarActividad(Usuario, Aplicacion, Mensaje):
    code = generarCodigo2()
    print(code)
    fecha = datetime.datetime.now()
    bitacora = open("tPrueba.txt", "a")
    registro = str(fecha.strftime("%d-%m-%Y %H:%M:%S")) + ", " + str(Usuario) + ", " + str(Aplicacion) + ", " + str(Mensaje) + ", " "Codigo:"+ str(code)
    bitacora.write(str(registro) + "\n")
    bitacora.close

def generarCodigo():
    archivo = open("tPrueba.txt", "r")
    #archivo = archivo.readlines()
    codigo = 0
    ultimaFila = []

    filas = archivo.readlines()
    print(filas)

    for elemento in filas:
        ultimaFila = [elemento]
    print(ultimaFila)

def generarCodigo2():
    codigo = 0
    fila = []
    texto = open("tPrueba.txt", encoding = 'utf- 8', mode ='r')
    if texto.readline() != "":
        for elemento in texto:
            fila = elemento.split(", ")
            print(fila)
        fila = fila[4].split(":")
        codigo = (int(fila[1]) + 1)
    else:
        codigo = 1
    return codigo

def borrarRegistro(codigo):
    texto = open("tPrueba.txt", encoding = 'utf- 8', mode ='r')
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
    texto = open("tPrueba.txt", mode="w")
    for elemento in newTex:
        texto.writelines(str(elemento))
    texto.close()
def resetearTexto():
    texto = texto = open("tPrueba.txt", encoding = 'utf- 8', mode ='w')


def encontrarActividad(codigo,user,app, msj,):
    texto = open("tPrueba.txt", mode="r")
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
            print(usuario, user)
            fila[2] = fila[2].replace(aplicacion, app)
            fila[3] = fila[3].replace(mensaje, msj)
            filaNueva = fila[0] + ", " + fila[1] +", "+ fila[2]+ ", " +fila[3] +", "+ fila[4]
            nuevaLista += [filaNueva]
        elif valor != codigo:
            nuevaLista += [elemento]
        print(filaNueva)
        print(elemento)
    sobreEscribir(nuevaLista)
    print(nuevaLista)

def listaString(list):
    string = ""
    for ele in list:
        string += ele + ", "
    print(string)

def imprimirActividades():
    texto = open("tPrueba.txt", mode="r")
    for elemento in texto:
        print(elemento)