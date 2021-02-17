# Clase proceso para crear cada proceso nuevo introducido al sistema
class Proceso:

    def __init__(self, nombre, llegada, paginas, tEjec, estado):
        self.nombre = nombre
        self.llegada = llegada
        self.paginas = paginas
        self.tEjec = tEjec
        self.estado = estado
        self.quantum = 4
        self.cpuAsignado = 0
        self.cpuRestante = self.tEjec - self.cpuAsignado
    
    def printProceso(self):
        print("Nombre de Proceso:", self.nombre)
        print('Llegada:', self.llegada)
        print("Paginas:", self.paginas)
        print("Tiempo Total:", self.tEjec)
        print("Estado:", self.estado)

def agregarFinished():                                # Metodo para checar si ya termino un proceso
    global listaRunning
    #global listaProcesos
    global listaFinished
               
    listaRunning[0].estado = 4
    listaFinished.append(listaRunning[0])
    listaRunning.pop()
    algoritmoFIFO()

def agregarBlocked():
    global listaRunning
    #global listaProcesos
    global listaBlocked

    listaRunning[0].estado = 2
    listaBlocked.append(listaRunning[0])
    listaRunning.pop(0)

def agrergarRunningReady():
    global listaRunning
    global listaReady

    listaRunning.estado = 3
    listaReady.append(listaRunning[0])
    listaRunning.pop(0)

def agregarBlockedReady():
    global listaBlocked
    global listaReady

    listaBlocked[0].estado = 3
    listaReady.append(listaBlocked[0])
    listaBlocked.pop(0)

def manejoInterrupt(interrupcion):
    if interrupcion == 1:
        agregarBlocked()
    elif interrupcion == 2:
        agregarFinished()
    if interrupcion == 3:
        agrergarRunningReady()
    elif interrupcion == 4:
        agregarFinished()
    if interrupcion == 5:
        agrergarRunningReady()
    if interrupcion == 6:
        agregarBlocked()

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
        agregarFinished()

# Metodo de Round Robin
def algoritmoRoundRobin():
    global listaReady
    global listaRunning

    if not listaRunning or listaRunning[0].quantum == 0:    # Si la lista de Running esta vacia, agrega primer
        if listaRunning:                                    # proceso de Ready y lo quita de la lista, si no esta vacia
            listaRunning[0].quantum = 4                     # y se acabo el quantum del proceso actual, se resetea a 4,
            agrergarRunningReady()                          # se envia el proceso a Ready y se agrega el siguiente
        listaRunning.append(listaReady[0])   
        listaReady.pop(0)                      
        algoritmoRoundRobin()
    
    if listaRunning[0].quantum > 0 or not cehcarFinProceso(): # Si el quantum es mayor a 0 y el proceso no ha terminado 
        listaRunning[0].quantum -= 1                          # se le resta 1
    
    else:                                                     # Si se acaba el proceso se agreaga a Finished, si se acaba
        if cehcarFinProceso():                                # el quantum se agrega a Ready
            agregarFinished()
        else:
            listaRunning[0].quantum = 4
            agrergarRunningReady()


'''
    else:                                       # Se regresa el proceso a ready y se carga el siguiente
        listaRunning[0].estado = 3
        listaReady.append(listaRunning[0])
        listaRunning[0] = listaReady[0]
        listaReady.pop(0)
'''

# Metodo para leer datos de archivo
def lecturaArchivo():
    #global listaProcesos
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
            f.readline()

        procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado)

        #listaProcesos.append(procesoNuevo) 
        listaReady.append(procesoNuevo)
        listaNombres.append(i+1)

    return pags, tiempoActual

def crearProceso(tiempoActual):
    #global listaProcesos
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

    #listaProcesos.append(procesoNuevo)
    listaReady.append(procesoNuevo)

    #return listaReady
        
# Listas vacias para almacenar Procesos
#listaProcesos = []
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
