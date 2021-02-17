# Clase proceso para crear cada proceso nuevo introducido al sistema
class Proceso:

    def __init__(self, nombre, llegada, paginas, tEjec, estado):
        self.nombre = nombre
        self.llegada = llegada
        self.paginas = paginas
        self.tEjec = tEjec
        self.estado = estado
    
    def printProceso(self):
        print("Nombre de Proceso:", self.nombre)
        print('Llegada:', self.llegada)
        print("Paginas:", self.paginas)
        print("Tiempo Total:", self.tEjec)
        print("Estado:", self.estado)

def agregarFinished():                                # Metodo para checar si ya termino un proceso
    global listaRunning
    global listaProcesos
    global listaFinished

    if listaRunning[0].tEjec < 1:               
        procesoAct.estado = 4
        listaFinished.append(listaRunning[0])
        listaRunning.pop()
        algoritmoFIFO()

def cehcarFinProceso():
    global listaRunning

    if listaRunning[0].tEjec < 1:
        return True

def algoritmoFIFO():
    global listaReady
    global listaRunning
    global listaFinished

    if not listaRunning:                        # Si la lista de Running esta vacia, agrega primer
        listaRunning.append(listaReady[0])      # proceso de Ready y lo quita de la lista y vuelve
        listaReady.pop(0)                       #  a correr el metodo
        algoritmoFIFO()

    elif cehcarFinProceso():                    # Si se termino el proceso, se cambia el estado, se agrega
        listaRunning[0].estado = 4              # a finished, y se carga el siguiente proceso
        listaFinished.append(listaRunning[0])
        listaRunning[0] = listaReady[0]
        listaReady.pop(0)

'''
    else:                                       # Se regresa el proceso a ready y se carga el siguiente
        listaRunning[0].estado = 3
        listaReady.append(listaRunning[0])
        listaRunning[0] = listaReady[0]
        listaReady.pop(0)
'''

# Metodo para leer datos de archivo
def lecturaArchivo():
    global listaProcesos
    global listaNombres
    global listaReady

    # Abre archivo para capturar datos
    while True:
        try:
            nombreArchivo = input('Nombre de Archivo a leer: ')
            f = open(nombreArchivo, 'r')
            break
        except FileNotFoundError:
            print('Ingrese el nombre completo del archivo')

    data = f.readline().replace(' ','').split(',')
    pags = int(data[0])                                      # Cantidad maxima de paginas
    tiempoActual = int(data[1])                              # Tiempo actual

    numProcesos = int(f.readline())                          # Numero de procesos

    # Ciclo para crear los procesos leidos del archivo
    for i in range(numProcesos):

        # llegada, tiempo total estimado y estado (1-running, 2-blocked, 3-ready, 4-Finished)
        datosProceso = f.readline().replace(' ','').split(',')   

        llegada = int(datosProceso[0])
        tiempoTotal = int(datosProceso[1])
        estado = int(datosProceso[2])

        numPags = int(f.readline())

        for pag in range(numPags):
            d = f.readline()

        procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado)

        listaProcesos.append(procesoNuevo) 
        listaReady.append(procesoNuevo)
        listaNombres.append(i+1)

    return pags, tiempoActual

def crearProceso(tiempoActual):
    global listaProcesos
    global listaNombres
    global listaReady

    # Checa que el nombre del proceso no exista ya
    while True:
        nombre = int(input("Nombre: "))
        if nombre not in listaNombres:
            break
        else:
            print('El proceso ya existe')

    paginas = int(input('Paginas: '))
    tiempoTotal = int(input('Tiempo de Ejecucion: '))
    llegada = tiempoActual

    procesoNuevo = Proceso(nombre, llegada, paginas, tiempoTotal, 3)

    listaProcesos.append(procesoNuevo)
    listaReady.append(procesoNuevo)

    #return listaReady
        
# Listas vacias para almacenar Procesos
listaProcesos = []
listaReady = []
listaRunning = []
listaBlocked = []
listaNombres = []
listaFinished = []

pags, tiempoActual = lecturaArchivo()

crearProceso(tiempoActual)

algoritmoFIFO()

# TESTING
print('\n******** READY ********')
for i, proceso in enumerate(listaReady):
    print(f'\n********* Proceso {i+1} **********')
    proceso.printProceso()

print('\n******** RUNNING ********')
print(listaRunning[0].printProceso())

print('\n******** Finished ********')
print(listaFinished[0].printProceso())
