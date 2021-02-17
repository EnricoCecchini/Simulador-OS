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

        # llegada, tiempo total estimado y estado (1-running, 2-blocked, 3-ready)
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

pags, tiempoActual = lecturaArchivo()

crearProceso(tiempoActual)

#print(listaProcesos[0].printProceso())

for i, proceso in enumerate(listaProcesos):
    print(f'\n********* Proceso {i+1} **********')
    proceso.printProceso()
