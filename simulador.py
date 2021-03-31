# Clase proceso para crear cada proceso nuevo introducido al sistema
class Proceso:
    global tiempoActual

    def __init__(self, nombre, llegada, paginas, tEjec, estado, listaPags):
        self.nombre = nombre
        self.llegada = llegada
        self.paginas = paginas
        self.tEjec = tEjec
        self.estado = estado
        self.listaPags = listaPags
        self.quantum = 0
        self.cpuAsignado = 0
        self.cpuRestante = self.tEjec - self.cpuAsignado
        self.envejecimiento = tiempoActual - self.llegada - self.cpuAsignado
    
    def printProceso(self):
        print("Nombre de Proceso:", self.nombre)
        print('Llegada:', self.llegada)
        print("Paginas:", self.paginas)
        print("Tiempo Total:", self.tEjec)
        print("Estado:", self.estado)
        print('CPU Restante:', self.cpuRestante)
        print('Edad:', self.envejecimiento)
        print('Quantum Restante:', self.quantum)

        print('Paginas:')
        nPag = 0
        for pag in self.listaPags:
          print(f'Pagina {nPag}:', pag)
          nPag+=1
        '''
        if self.estado == 1:
            print('Paginas:')
            nPag = 0
            for pag in self.listaPags:
                print(f'Pagina {nPag}:', pag)
                nPag+=1
        '''

# ****************** Algoritmos de Paginacion ******************

# Metodo para resetear valores de NUR
def resetNur():
    global listaRunning

    for i in range(len(listaRunning[0].listaPags)):
        listaRunning[0].listaPags[i][5] = 0
        listaRunning[0].listaPags[i][6] = 0

# Algoritmo de Paginacion FIFO
def pagFIFO():
    global limitePags
    global listaRunning

    tiempoTempNuevo = listaRunning[0].listaPags[0][2]
    tiempoTempViejo = listaRunning[0].listaPags[0][2]
    indexNuevo = 0
    indexViejo = 0
    pagsAct = 0

    # Se iteran las paginas para encontrar la primera en llegar no activada y la mas vieja activada
    for i in range(len(listaRunning[0].listaPags)):
        if tiempoTempNuevo > listaRunning[0].listaPags[i][2] and listaRunning[0].listaPags[i][1] == 0:
            indexNuevo = i
            tiempoTempNuevo = listaRunning[0].listaPags[i][2]
        
        if tiempoTempViejo < listaRunning[0].listaPags[i][2] and listaRunning[0].listaPags[i][1] == 1:
            indexViejo = i
            tiempoTempViejo = listaRunning[0].listaPags[i][2]

        if listaRunning[0].listaPags[i][1] == 1:
            pagsAct += 1
    
    # Si aun hay espacio para paginas nuevas, se carga la pagina nueva
    if pagsAct < limitePags:
        listaRunning[0].listaPags[indexNuevo][1] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexNuevo][1] = 1
        

# Algoritmo de Paginacion LRU
def pagLRU():
    global limitePags
    global listaRunning

    accesoTempNuevo = listaRunning[0].listaPags[0][3]
    accesoTempViejo = listaRunning[0].listaPags[0][3]
    indexNuevo = 0
    indexViejo = 0
    pagsAct = 0

    # Se iteran las paginas para encontrar la pagina con mas tiempo sin accesar y la mas recientemente accesada
    for i in range(len(listaRunning[0].listaPags)):
        if accesoTempNuevo > listaRunning[0].listaPags[i][3] and listaRunning[0].listaPags[i][1] == 0:
            indexNuevo = i
            accesoTempNuevo = listaRunning[0].listaPags[i][3]
        
        if accesoTempViejo < listaRunning[0].listaPags[i][3] and listaRunning[0].listaPags[i][1] == 1:
            indexViejo = i
            accesoTempViejo = listaRunning[0].listaPags[i][3]

        if listaRunning[0].listaPags[i][1] == 1:
            pagsAct += 1
    
    # Si aun hay espacio para paginas nuevas, se carga la pagina nueva
    if pagsAct < limitePags:
        listaRunning[0].listaPags[indexNuevo][1] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexNuevo][1] = 1

# Algoritmo de Paginacion LFU
def pagLFU():
    global limitePags
    global listaRunning

    nAccesosTempNuevo = listaRunning[0].listaPags[0][3]
    nAccesosTempViejo = listaRunning[0].listaPags[0][3]
    indexNuevo = 0
    indexViejo = 0
    pagsAct = 0

    # Se iteran las paginas para encontrar la pagina con mas tiempo sin accesar y la mas recientemente accesada
    for i in range(len(listaRunning[0].listaPags)):
        if nAccesosTempNuevo > listaRunning[0].listaPags[i][4] and listaRunning[0].listaPags[i][1] == 0:
            indexNuevo = i
            nAccesosTempNuevo = listaRunning[0].listaPags[i][4]
        
        if nAccesosTempViejo < listaRunning[0].listaPags[i][4] and listaRunning[0].listaPags[i][1] == 1:
            indexViejo = i
            nAccesosTempViejo = listaRunning[0].listaPags[i][4]

        if listaRunning[0].listaPags[i][1] == 1:
            pagsAct += 1
    
    # Si aun hay espacio para paginas nuevas, se carga la pagina nueva
    if pagsAct < limitePags:
        listaRunning[0].listaPags[indexNuevo][1] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexNuevo][1] = 1

def pagNUR():
    global limitePags
    global listaRunning
    
    prioridad0 = []
    prioridad1 = []
    prioridad2 = []
    prioridad3 = []

    pagAct = 0
    for i in range(len(listaRunning[0].listaPags)):
        if listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 0:
            prioridad0.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 0:
            prioridad1.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 1:
            prioridad2.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 1:
            prioridad3.append(i)
        
        if listaRunning[0].listaPags[i][1] == 1:
            pagAct+=1

    prioridad0.append(prioridad1).append(prioridad2).append.prioridad3()

    if pagAct < limitePags:
        listaRunning[0].listaPags[prioridad0[0]][1] = 1
    
    else:
        listaRunning[0].listaPags[prioridad0[-1]][1] = 0
        listaRunning[0].listaPags[prioridad0[0]][1] = 0



# ****************** Algoritmos de Scheduling ******************
def findRunning():
    global listaReady

    procesoTemp = listaReady[0]

    for proceso in listaReady:
        if proceso.estado == 1:
            procesoTemp = proceso
            break
    
    listaReady.remove(procesoTemp)                    # Pone el proceso ejecutandose al inicio de Ready
    listaReady.insert(0, procesoTemp)

def agregarFinished():                                # Metodo para checar si ya termino un proceso
    global listaRunning
    #global listaProcesos
    global listaFinished
               
    try:
      if listaRunning[0].cpuRestante == 0:
        listaRunning[0].estado = 4
        listaFinished.append(listaRunning[0])
        listaRunning.pop()
        
      else:
        listaRunning[0].estado = 4
        listaFinished.append(listaRunning[0])
    
    except IndexError:
      pass
    
def agregarBlocked():
    global listaRunning
    #global listaProcesos
    global listaBlocked

    listaRunning[0].estado = 2
    listaBlocked.append(listaRunning[0])
    listaRunning.pop(0)

def agregarRunningReady():
    global listaRunning
    global listaReady

    listaRunning[0].estado = 3
    listaReady.append(listaRunning[0])
    listaRunning.pop(0)

def agregarBlockedReady():
    global listaBlocked
    global listaReady

    listaBlocked[0].estado = 3
    listaReady.append(listaBlocked[0])
    listaBlocked.pop(0)

def agregarReady():
    global listaReady
    global listaRunning

    if not listaRunning:
        listaRunning.append(listaReady[0])
        listaReady.pop(0)

def manejoInterrupt(interrupcion):
    if interrupcion == 1:
        agregarBlocked()
        agregarReady()
    elif interrupcion == 2:
        agregarFinished()
        agregarReady()
    if interrupcion == 3:
        agregarRunningReady()
        agregarReady()
    elif interrupcion == 4:
        agregarFinished()
        agregarReady()
    if interrupcion == 5:
        agregarRunningReady()
    if interrupcion == 6:
        agregarBlocked()

def checarFinProceso():
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
        # Agregar metodo para continuar hasta que termine
        algoritmoFIFO()

    elif checarFinProceso():                    # Si se termino el proceso, se cambia el estado, se agrega
        agregarFinished()

# Metodo de Round Robin
def algoritmoRoundRobin():
    global listaReady
    global listaRunning

    if not listaReady:
        return

    if not listaRunning or listaRunning[0].quantum == 0:    # Si la lista de Running esta vacia, agrega primer
        if listaRunning:                                    # proceso de Ready y lo quita de la lista, si no esta vacia
            listaRunning[0].quantum = 0                     # y se acabo el quantum del proceso actual, se resetea a 4,
            agregarRunningReady() 
            #algoritmoRoundRobin()                           # se envia el proceso a Ready y se agrega el siguiente
        listaRunning.append(listaReady[0])   
        listaRunning[0].quantum = 4
        listaReady.pop(0)                      
        algoritmoRoundRobin()
    
    if listaRunning[0].quantum > 0 or not checarFinProceso(): # Si el quantum es mayor a 0 y el proceso no ha terminado 
        listaRunning[0].quantum -= 1                          # se le resta 1
        #algoritmoRoundRobin()

    else:                                                     # Si se acaba el proceso se agreaga a Finished, si se acaba
        if checarFinProceso():                                # el quantum se agrega a Ready
            agregarFinished()
        else:
            listaRunning[0].quantum = 4
            #agregarRunningReady()

# Metodo de SRT Apropiativo
def algoritmoSRT():
    global listaRunning
    global listaReady

    if listaRunning:
        agregarRunningReady()                                   # Quita proceso que se esta ejecutando y lo agrega a Ready
    
    procesoTemp = listaReady[0]

    for proceso in listaReady:                              # Encuentra proceso que termina mas rapido                         
        if proceso.cpuRestante < procesoTemp.cpuRestante:
            procesoTemp = proceso
    
    listaReady.remove(procesoTemp)                          # Pone el proceso mas corto al inicio de Ready
    listaReady.insert(0, procesoTemp)

    listaRunning.append(listaReady[0])                      # Agrega proceso a Running
    listaReady.pop(0)

# Metodo de HRRN Apropiado
def algoritmoHRRN():
    global listaRunning
    global listaReady

    if listaRunning:
        if checarFinProceso():
            agregarFinished()
            algoritmoHRRN()
        else:
            # Agregar metodo para siguiente vuelta hasta que el proceso actual termine
            algoritmoHRRN()

    else:
        procesoTemp = listaReady[0]
        prioridadTemp = (procesoTemp.envejecimiento-procesoTemp.tEjec)/procesoTemp.tEjec

        for proceso in listaReady:
            prioridadProceso = (proceso.envejecimiento-proceso.tEjec)/proceso.tEjec
            
            if prioridadProceso > prioridadTemp:
                prioridadTemp = prioridadProceso
                procesoTemp = proceso
        
        listaReady.remove(procesoTemp)                          # Pone el proceso con mas prioridad al inicio de Ready
        listaReady.insert(0, procesoTemp)

        listaRunning.append(listaReady[0])                      # Agrega proceso a Running
        listaReady.pop(0)

# Metodo para leer datos de archivo
def lecturaArchivo():
    #global listaProcesos
    global listaNombres
    global listaReady
    global tiempoActual
    global limitePags

    # Abre archivo para capturar datos
    while True:
        try:
            nombreArchivo = input('Nombre de Archivo a leer: ')
            f = open(nombreArchivo, 'r')
            break
        except FileNotFoundError:
            print('Ingrese el nombre completo del archivo')

    data = f.readline().replace(' ','').split(',')
    limitePags = int(data[0])                                      # Cantidad maxima de paginas
    tiempoActual = int(data[1])                              # Tiempo actual

    numProcesos = int(f.readline())                          # Numero de procesos

    # Ciclo para crear los procesos leidos del archivo
    for i in range(numProcesos):
        # llegada, tiempo total estimado y estado (1-running, 2-blocked, 3-ready)
        datosProceso = f.readline().replace(' ','').split(',')   
        llegada = int(datosProceso[0])
        tiempoTotal = int(datosProceso[1])
        estado = int(datosProceso[2])
        numPags = int(f.readline())
        listaPags = []
        
        n = 0
        for pag in range(numPags):
            pags = f.readline().replace(' ','').replace('\n','').split(',')
            res = int(pags[0])
            tLlegada = int(pags[1])
            ultAccess = int(pags[2])
            numAccess = int(pags[3])
            bitLectura = int(pags[4])
            bitEscritura = int(pags[5])
            
            page = [n, res, tLlegada, ultAccess, numAccess, bitLectura, bitEscritura]
            
            listaPags.append(page)
            n+=1
        
        procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado, listaPags)

        #listaProcesos.append(procesoNuevo) 
        listaReady.append(procesoNuevo)
        listaNombres.append(i+1)

# Metodo para crear procesos
def crearProceso():
    #global listaProcesos
    global listaNombres
    global listaReady
    global tiempoActual
    global limitePags

    # Checa que el nombre del proceso no exista ya
    while True:
        nombre = int(input("Nombre: "))
        if nombre not in listaNombres:
            break
        else:
            print('El proceso ya existe')

    while True:
        paginas = int(input('Paginas: '))
        if paginas <= limitePags:
            break
        else:
            print('Excediste limite de paginas')
    
    tiempoTotal = int(input('Tiempo de Ejecucion: '))
    llegada = tiempoActual

    listaPags = []
    
    for i in range(paginas):
        pag = [i, 0, 0, 0, 0, 0, 0]
        listaPags.append(pag)

    procesoNuevo = Proceso(nombre, llegada, paginas, tiempoTotal, 3, listaPags)

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

tiempoActual = 0
limitePags = 0

lecturaArchivo()

# TESTING
#crearProceso()

print('\n****************** READY ******************')
for i, proceso in enumerate(listaReady):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')

findRunning()

algoritmoFIFO()
manejoInterrupt(1)
algoritmoFIFO()

print('\n\n')
print('-'*30)
print('\n****************** READY ******************')
for i, proceso in enumerate(listaReady):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')

print('\n****************** RUNNING ******************')
for i, proceso in enumerate(listaRunning):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')

print('\n****************** Blocked ******************')
for i, proceso in enumerate(listaBlocked):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')

print('\n****************** Finished ******************')
for i, proceso in enumerate(listaFinished):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')

#algoritmoFIFO()
pagLRU()

print('\n\n')
print('-'*30)
print('\n****************** RUNNING ******************')
for i, proceso in enumerate(listaRunning):
    print(f'********* Proceso {i+1} *********')
    proceso.printProceso()
    print('\n')