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

def crearProceso(listaReady, tiempoActual):
    global listaProcesos
    global listaNombres

    # Checa que el nombre del proceso no exista ya
    nombre = -1
    while nombre == -1 or nombre in listaNombres:
        nombre = int(input("Nombre: "))

    paginas = int(input('Paginas: '))
    tiempoTotal = int(input('Tiempo de Ejecucion: '))
    llegada = tiempoActual

    procesoNuevo = Proceso(nombre, llegada, paginas, tiempoTotal, 3)

    listaProcesos.append(procesoNuevo)
    listaReady.append(procesoNuevo)

    return listaReady
        

l = input().replace(' ','').split(',')
pags = int(l[0])                                    # Cantidad maxima de paginas
tiempoActual = int(l[1])                                  # Tiempo actual

listaProcesos = []
listaReady = []
listaRunning = []
listaBlocked = []
listaNombres = []

numProcesos = int(input())                          # Numero de procesos

# Ciclo para crear los procesos leidos del archivo
for i in range(numProcesos):

    # llegada, tiempo total estimado y estado (1-running, 2-blocked, 3-ready)
    datosProceso = input().replace(' ','').split(',')   

    llegada = int(datosProceso[0])
    tiempoTotal = int(datosProceso[1])
    estado = int(datosProceso[2])


    numPags = int(input())

    procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado)

    listaProcesos.append(procesoNuevo) 
    listaReady.append(procesoNuevo)
    listaNombres.append(i+1)

listaReady = crearProceso(listaReady, tiempoActual)
for i, proceso in enumerate(listaProcesos):
    print(f'\n********* Proceso {i+1} **********')
    proceso.printProceso()