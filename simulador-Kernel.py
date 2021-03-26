'''
Enrico Cecchini Rivera  - 531059  50%
Carmen Aurora Monjaras  - 531675  50%

Declaramos que hemos realizado esta actividad con integridad academica
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
contador=0

# Metodo para agregar procesos a Finished
def agregarFinished():                                
    global listaRunning
    #global listaProcesos
    global listaFinished
    global listaReady
    global Lbrun
    global Lbfin
    
    try:
      if listaRunning[0].cpuRestante == 0:
        listaRunning[0].estado = 4
        listaFinished.append(listaRunning[0])
        #listaRunning.pop()
        
        for process in listaRunning:
          Lbfin.insert(END, process.nombre)
          Lbrun.delete(0,END)
        listaRunning.pop()
      else:
        listaRunning[0].estado = 4
        listaFinished.append(listaRunning[0])
        for process in listaRunning:
          Lbfin.insert(END, process.nombre)
          Lbrun.delete(0)
        listaRunning.pop()
    except IndexError:
      pass
    Lbfin.delete(0,END)
    for process in listaFinished:
      Lbfin.insert(END, process.nombre)
    

# Metodo para agregar procesos de Running a Blocked
def agregarBlocked():
    global listaRunning
    #global listaProcesos
    global listaBlocked
    global Lbrun
    global lbB
    listaRunning[0].estado = 2
    listaBlocked.append(listaRunning[0])
    Lbrun.delete(0,END)
    listaRunning.pop(0)
    LbB.delete(0,END)
    i=1
    for process in listaBlocked:
      LbB.insert(i, process.nombre)
      i=i+1


# Metodo para agregar procesos de Running a Ready
def agregarRunningReady():
    global listaRunning
    global listaReady
    global Lbrun
    global Lbready
    
    listaRunning[0].estado = 3
    listaReady.append(listaRunning[0])
    Lbready.insert(END, listaRunning[0].nombre)
    Lbrun.delete(0, END)
    listaRunning.pop(0)

# Metodo para agregar procesos de Blocked a Ready
def agregarBlockedReady():
    global listaBlocked
    global listaReady
    global Lbready
    listaBlocked[0].estado = 3
    listaReady.append(listaBlocked[0])
    nom=listaBlocked[0].nombre
    Lbready.insert(END,nom)
    listaBlocked.pop(0)
    LbB.delete(0,END)
    i=1
    for process in listaBlocked:
      LbB.insert(i, process.nombre)
      i=i+1

# Metodo para agregar procesos de Ready a Running
def agregarReady():
    global listaReady
    global listaRunning
    global Lbready
    global Lbrun
    
    try:
      if not listaRunning:
          listaRunning.append(listaReady[0])
          nom=listaReady[0].nombre
          listaReady.pop(0)
          Lbready.delete(0)
          Lbrun.insert(END, nom)
    except IndexError:
      pass
    

def ShowChoice():
  global tiempoActual, contador
  global listaReady
  global listaRunning
  global listaBlocked
  global listaFinished
  global Lbready
  global Lbrun
  global Lbfin
  global lbB
  global label_nom, label_llegada, label_pag, label_tEjec, label_cpuA, label_cpuR, label_en, label_q  
  
  try:
    tiempoActual+=1

    if not checarFinProceso():
      agregarFinished()

    label_TActual.config(text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 12))
    opcion=int(v.get())
    
    if opcion==1:
      print("SVC de solicitud de i/o")
      agregarBlocked()
      agregarReady()
    elif opcion==2:
      print("terminacion normal")
      agregarFinished()
      agregarReady()
    elif opcion==3:
      print("SVC de solicitud de fecha")
      agregarRunningReady()
      agregarReady()
    elif opcion==4:
      print("Error de programa")
      agregarFinished()
      agregarReady()
    elif opcion==5:
      print("quantum expirado")
      agregarRunningReady()
      agregarReady()
    elif opcion==6:
      print("Dispositivo de i/o")
      agregarBlocked()
      agregarReady()
    
    for process in listaRunning: # agrega 1 a cpu asignado
      process.cpuAsignado=process.cpuAsignado+1
      process.cpuRestante-=1
    
    for process in listaReady:#Actualiza los datos de la lista de ready
      process.Envejecimiento=tiempoActual-process.llegada-process.cpuAsignado
      process.hrrn=(process.Envejecimiento-process.tEjec)/process.tEjec
    
    for process in listaBlocked:#Actualiza los datos de la lista de ready
      process.Envejecimiento=tiempoActual-process.llegada-process.cpuAsignado
      process.hrrn=(process.Envejecimiento-process.tEjec)/process.tEjec
    
    opcion=int(x.get())#se obtiene el tipo de scheduling
    if opcion==1: #fifo
      print("FIFO")
      algoritmoFIFO()
    elif opcion==2: #RR
      print("Round robin")
      listaRunning[0].quantum=4
      algoritmoRoundRobin()
    elif opcion==3: #SRT
      print("SRT")
      algoritmoSRT()
    elif opcion==4: #HRRn
      print("HRRN")
      algoritmoHRRN()
    
    contador+=1
    label_nom.config(text="Nombre: "+ str(listaRunning[0].nombre), font=('Times', 12))
    label_llegada.config(text="Tiempo de llegada: "+ str(listaRunning[0].llegada), font=('Times', 12))
    label_pag.config(text="Paginas: "+ str(listaRunning[0].paginas), font=('Times', 12))
    label_tEjec.config(text="Tiempo estimado de ejecución: "+ str(listaRunning[0].tEjec), font=('Times', 12))
    label_cpuA.config(text="CPU Asignado: "+ str(listaRunning[0].cpuAsignado), font=('Times', 12))
    label_cpuR.config(text="CPU Restante: "+ str(listaRunning[0].cpuRestante), font=('Times', 12))
    label_en.config(text="Envejecimiento: "+ str(listaRunning[0].Envejecimiento), font=('Times', 12))
    label_q.config(text="Quantum Restante: "+ str(listaRunning[0].quantum), font=('Times', 12))

    if contador%5 == 0 and listaBlocked:
      listaBlocked[0].estado=3
      listaReady.append(listaBlocked[0])
      listaBlocked.pop()
    Lbready.delete(0, END)
    Lbrun.delete(0, END)
    for process in listaReady:
      Lbready.insert(END, process.nombre)
    for process in listaRunning:
      Lbrun.insert(END, process.nombre)
  except IndexError:
    pass
  Lbfin.delete(0,END)
  for process in listaFinished:
    Lbfin.insert(END, process.nombre)
  Lbready.delete(0, END)
  Lbrun.delete(0, END)
  for process in listaReady:
    Lbready.insert(END, process.nombre)
  for process in listaRunning:
    Lbrun.insert(END, process.nombre)
  LbB.delete(0,END)
  for process in listaBlocked:
    LbB.insert(END, process.nombre)
  

def ShowCPU():
  opcion=int(x.get())

# Metodo para checar fin de proceso
def checarFinProceso():
    global listaRunning
    
    if listaRunning[0].cpuRestante > 0:
      return True       

# FIFO
def algoritmoFIFO():
    global listaReady
    global listaRunning
    global listaFinished
    global Lbready
    global Lbrun
    global Lbfin
    
    try:
      if not listaRunning:                        # Si la lista de Running esta vacia, agrega primer
          listaRunning.append(listaReady[0])      # proceso de Ready y lo quita de la lista y vuelve
          nom=listaReady[0].nombre
          Lbrun.insert(END, nom)
          Lbready.delete(0)
          listaReady.pop(0)                       #  a correr el metodo
          # Agregar metodo para continuar hasta que termine
          algoritmoFIFO()
      elif listaRunning[0].cpuRestante < 1: 
        agregarFinished()
        algoritmoFIFO()
    except IndexError:
      pass
      #algoritmoFIFO()
    #Checa las cosas en la interfaz gráfica
    Lbready.delete(0,END)
    Lbrun.delete(0,END)
    
    for process in listaReady:
      Lbready.insert(process.nombre)
    for process in listaRunning:
      Lbrun.insert(process.nombre)


# Round Robin
def algoritmoRoundRobin():
    global listaReady
    global listaRunning
    global listaFinished
    global Lbready
    global Lbrun
    global Lbfin
    
    if not listaReady:
        return
    
    if not listaRunning or listaRunning[0].quantum == 0:    # Si la lista de Running esta vacia, agrega primer
        if listaRunning:                                    # proceso de Ready y lo quita de la lista, si no esta vacia
            listaRunning[0].quantum = 0                     # y se acabo el quantum del proceso actual, se resetea a 4,
            agregarRunningReady() 
            #algoritmoRoundRobin()                           # se envia el proceso a Ready y se agrega el siguiente
        listaRunning.append(listaReady[0])   
        listaRunning[0].quantum = 5
        listaReady.pop(0)                      
        algoritmoRoundRobin()
    
    if listaRunning[0].quantum > 1 and checarFinProceso(): # Si el quantum es mayor a 0 o el proceso no ha terminado 
        listaRunning[0].quantum -= 1                          # se le resta 1
        #algoritmoRoundRobin()
    else:                                                     # Si se acaba el proceso se agreaga a Finished, si se acaba
        if not checarFinProceso():                                # el quantum se agrega a Ready
            agregarFinished()
            algoritmoRoundRobin()
        else:
            listaRunning[0].quantum = 0
            agregarRunningReady()

    #Checa las cosas en la interfaz gráfica
    Lbready.delete(0,END)
    Lbrun.delete(0,END)
    for process in listaReady:
      Lbready.insert(process.nombre)
    for process in listaRunning:
      Lbrun.insert(process.nombre)


# Metodo de SRT Apropiativo
def algoritmoSRT():
    global listaRunning
    global listaReady
    global Lbready
    global Lbrun
    global Lbfin
    
    try:
      if listaRunning:
        if not checarFinProceso():
          agregarFinished()
          algoritmoSRT()
        else:  
          agregarRunningReady()                                   # Quita proceso que se esta ejecutando y lo agrega a Ready
      else:
        procesoTemp = listaReady[0]
        
        for proceso in listaReady:                              # Encuentra proceso que termina mas rapido        
            if proceso.cpuRestante < procesoTemp.cpuRestante:
                procesoTemp = proceso
        
        listaReady.remove(procesoTemp)                          # Pone el proceso mas corto al inicio de Ready
        listaReady.insert(0, procesoTemp)
        listaRunning.append(listaReady[0])                      # Agrega proceso a Running
        nom = listaReady[0].nombre
        listaReady.pop(0)
        
        #Checa las cosas en la interfaz gráfica
        Lbready.delete(0,END)
        Lbrun.delete(0,END)
        for process in listaReady:
          Lbready.insert(process.nombre)
        for process in listaRunning:
          Lbrun.insert(process.nombre)
    
    except IndexError:
      pass

# Metodo de HRRN Apropiativo
def algoritmoHRRN():
    global listaRunning
    global listaReady
    global Lbready
    global Lbrun
    global Lbfin
    
    try:
      if listaRunning:
        if not checarFinProceso():
          agregarFinished()
          algoritmoHRRN()
      else:
        procesoTemp = listaReady[0]
        prioridadTemp = (procesoTemp.Envejecimiento-procesoTemp.tEjec)/procesoTemp.tEjec
        for proceso in listaReady:
            prioridadProceso = (proceso.Envejecimiento-proceso.tEjec)/proceso.tEjec  
            if prioridadProceso > prioridadTemp:
                prioridadTemp = prioridadProceso
                procesoTemp = proceso
        listaReady.remove(procesoTemp)                          # Pone el proceso con mas prioridad al inicio de Ready
        listaReady.insert(0, procesoTemp)
        listaRunning.append(listaReady[0])                      # Agrega proceso a Running
        listaReady.pop(0)
         #Checa las cosas en la interfaz gráfica
      Lbready.delete(0,END)
      Lbrun.delete(0,END)
      for process in listaReady:
          Lbready.insert(process.nombre)
      for process in listaRunning:
          Lbrun.insert(process.nombre)
    
    except IndexError:
      pass

def execTime():
  global tiempoActual
  global listaRunning
  global listaBlocked
  global contador
  global label_nom, label_llegada, label_pag, label_tEjec, label_cpuA, label_cpuR, label_en, label_q
  try:
    tiempoActual+=1
    label_TActual.config(text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 12))
    contador+=1
    
    for process in listaRunning: # agrega 1 a cpu asignado
      process.cpuAsignado+=1
      process.cpuRestante-=1
    
    for process in listaReady:#Actualiza los datos de la lista de ready
      process.Envejecimiento=tiempoActual-process.llegada-process.cpuAsignado
      process.hrrn=(process.Envejecimiento-process.tEjec)/process.tEjec
    
    for process in listaBlocked:#Actualiza los datos de la lista de ready
      process.Envejecimiento=tiempoActual-process.llegada-process.cpuAsignado
      process.hrrn=(process.Envejecimiento-process.tEjec)/process.tEjec
    
    opcion=int(x.get())#se obtiene el tipo de scheduling
    
    if opcion==1: #fifo
      print("FIFO")
      algoritmoFIFO()
    elif opcion==2: #RR
      print("Round robin")
      algoritmoRoundRobin()
    elif opcion==3: #SRT
      print("SRT")
      algoritmoSRT()
    elif opcion==4: #HRRn
      print("HRRN")
      algoritmoHRRN()
    label_nom.config(text="Nombre: "+ str(listaRunning[0].nombre), font=('Times', 12))
    label_llegada.config(text="Tiempo de llegada: "+ str(listaRunning[0].llegada), font=('Times', 12))
    label_pag.config(text="Paginas: "+ str(listaRunning[0].paginas), font=('Times', 12))
    label_tEjec.config(text="Tiempo estimado de ejecución: "+ str(listaRunning[0].tEjec), font=('Times', 12))
    label_cpuA.config(text="CPU Asignado: "+ str(listaRunning[0].cpuAsignado), font=('Times', 12))
    label_cpuR.config(text="CPU Restante: "+ str(listaRunning[0].cpuRestante), font=('Times', 12))
    label_en.config(text="Envejecimiento: "+ str(listaRunning[0].Envejecimiento), font=('Times', 12))
    label_q.config(text="Quantum Restante: "+ str(listaRunning[0].quantum), font=('Times', 12))

    if contador%5 == 0 and listaBlocked:
      listaBlocked[0].estado=3
      listaReady.append(listaBlocked[0])
      listaBlocked.pop()
    Lbready.delete(0,END)
    for process in listaReady:
      Lbready.insert(END, process.nombre)
    Lbrun.delete(0,END)
    for process in listaRunning:
      Lbrun.insert(END, process.nombre)
  
  except IndexError:
    pass
  Lbfin.delete(0,END)
  for process in listaFinished:
    Lbfin.insert(END, process.nombre)
  Lbready.delete(0, END)
  Lbrun.delete(0, END)
  for process in listaReady:
    Lbready.insert(END, process.nombre)
  for process in listaRunning:
    Lbrun.insert(END, process.nombre)
  LbB.delete(0,END)
  for process in listaBlocked:
    LbB.insert(END, process.nombre)
  
def refresh():
  #resetea las opciones de las interrupciones
  v.set(None)

def refreshCPU():
  #resetea las opciones de scheduling
  x.set(1)

# Clase proceso para crear cada proceso nuevo introducido al sistema
class Proceso:
    def __init__(self, nombre, llegada, paginas, tEjec, estado):
        self.nombre = nombre
        self.llegada = llegada
        self.paginas = paginas
        self.tEjec = tEjec
        self.estado = estado
        self.quantum = 0
        self.cpuAsignado=0 #lo que ya se
        self.cpuRestante=self.tEjec-self.cpuAsignado
        self.Envejecimiento=tiempoActual-self.llegada-self.cpuAsignado
        self.hrrn=(self.Envejecimiento-self.tEjec)/self.tEjec
    
    def printProceso(self):
        print("Nombre de Proceso:", self.nombre)
        print('Llegada:', self.llegada)
        print("Paginas:", self.paginas)
        print("Tiempo Total:", self.tEjec)
        print("Estado:", self.estado)
        print("CPU Asignado:", self.cpuAsignado)
        print("CPU restante:",self.cpuRestante)
        print("Envejecimiento:", self.Envejecimiento)


# Metodo para leer datos de archivo
def lecturaArchivo(nombreArchivo):
    global listaProcesos
    global listaNombres
    global listaReady
    global tiempoActual
    
    # Abre archivo para capturar datos
    f = open(nombreArchivo, 'r')
    data = f.readline().replace(' ','').split(',')
    pags = int(data[0])                                    # Cantidad maxima de paginas
    tiempoActual = int(data[1])                            # Tiempo actual
    numProcesos = int(f.readline())                          # Numero de procesos
    
    # Ciclo para crear los procesos leidos del archivo
    for i in range(numProcesos):
        # llegada, tiempo total estimado y estado (1-running, 2-blocked, 3-ready)
        datosProceso = f.readline().replace(' ','').split(',')   
        llegada = int(datosProceso[0])
        tiempoTotal = int(datosProceso[1])
        estado = int(datosProceso[2])
        numPags = int(f.readline())
        procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado)
        
        for pag in range(numPags):
            f.readline()
        listaProcesos.append(procesoNuevo) 
        
        if estado==1:
          listaRunning.append(procesoNuevo)
        elif estado==2:
          listaBlocked.append(procesoNuevo)
        elif estado==3:
          listaReady.append(procesoNuevo)
        elif estado==4:
          listaFinished.append(procesoNuevo)
        listaNombres.append(i+1)
    
    return pags, tiempoActual

#Método para crear un proceso, checar si ya existe o sí se excedio el limite de página, actualiza la lista ready
def crearProceso(listaReady, tiempoActual):
    global listaProcesos
    global listaNombres
    global e1
    global e2
    global e3
    
    # Checa que el nombre del proceso no exista ya
    while True:
        nombre = int(e1.get())
        paginas = int(e2.get()) 
        
        if nombre not in listaNombres and paginas <= 6:
            break
        else:
            print('El proceso ya existe o se excedió el num de paginas permitidos')
            return
    
    tiempoTotal = int(e3.get())
    llegada = tiempoActual
    procesoNuevo = Proceso(nombre, llegada, paginas, tiempoTotal, 3)
    listaProcesos.append(procesoNuevo)
    listaReady.append(procesoNuevo)
    listaNombres.append(nombre)
    Lbready.insert(END, nombre)
    
    return listaProcesos, listaReady
        
# Listas vacias para almacenar Procesos
listaProcesos = []
listaReady = []
listaRunning = []
listaBlocked = []
listaNombres = []
listaFinished = []

archivo = input('Nombre de Archivo a leer: ')
pags, tiempoActual = lecturaArchivo(archivo)

#1-running 2-blocked 3-ready
window = tk.Tk()
window.title("Kernel Project")
#parte de arriba
frameTop = tk.Frame( master=window, width=100, height=25, bg="grey")
frameTop.pack(fill=tk.BOTH, expand=True)
label_TActual = tk.Label(frameTop, text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 12))
label_TActual.pack()
button_next= tk.Button(frameTop, text="Ejecutar", width=3, height=2, font=('Times', 12), command = execTime)
button_next.pack()

labelI = tk.Label(frameTop, text="Escoja una interrupcion", font=('Times', 14))
labelI.pack()
v = tk.IntVar()
v.set(None)
interrupciones = [("SVC de solicitud de I/O", 1), 
                  ("SVC de terminacion normal", 2),
                  ("SVC de solicitud de fecha", 3),
                  ("Error de programa", 4), 
                  ("Externa de quantum expirado", 5), 
                  ("Dispositivo de I/O", 6)]

#Mostrar las interrupciones
for choice, val in interrupciones:
  tk.Radiobutton(frameTop, 
                   text=choice,
                   padx = 20, 
                   variable=v, 
                   font=('Times', 12), 
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

button_refresh= tk.Button(frameTop, text="Refresh", width=5, height=2, font=('Times', 12), command=refresh)
button_refresh.pack()
# segunda parte del gui
frameCPU = tk.Frame(master=window, width=100, height=100, bg="red")
frameCPU.pack(fill=tk.BOTH, expand=True)

#Mostrar los valores de NEW---------------------------------------------------
def show_entry_fields():#añadir proceso al oprimir botón
    #print("Nom: %s\npags: %s\nEjecTotal: %s\nLlegada: %s" % (e1.get(), e2.get(), e3.get(), str(tiempoActual)))
    crearProceso(listaReady, tiempoActual)

#fields= "Nombre", "Pags", "Ejec Total"
tk.Label(frameCPU, text="Nombre", font=('Times', 12)).grid(row=0)
tk.Label(frameCPU, text="Pags", font=('Times', 12)).grid(row=1)
tk.Label(frameCPU, text="Ejec total", font=('Times', 12)).grid(row=2)

e1 = tk.Entry(frameCPU) #Nombre de proceso
e2 = tk.Entry(frameCPU) #Num de pags
e3 = tk.Entry(frameCPU) #ejecucion total

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(frameCPU,text='Add', font=('Times', 12), command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
#Listas
label_ready=tk.Label(frameCPU, text="Ready", font=('Times', 12)).grid(row=4)
label_run=tk.Label(frameCPU, text="Running", font=('Times', 12)).grid(row=4, column=1)
label_fin=tk.Label(frameCPU, text="Finished", font=('Times', 12)).grid(row=4, column=2)
label_B=tk.Label(frameCPU, text="Blocked", font=('Times', 12)).grid(row=4, column=3)

Lbready = tk.Listbox(frameCPU,  bd=1, height=3, font=('Times', 12))
Lbrun = tk.Listbox(frameCPU,  bd=1, height=3, font=('Times', 12))
Lbfin = tk.Listbox(frameCPU,  bd=1, height=3, font=('Times', 12))
LbB = tk.Listbox(frameCPU,  bd=1, height=3, font=('Times', 12))

Lbready.grid(row=5)
Lbrun.grid(row=5, column=1)
Lbfin.grid(row=5, column=2)
LbB.grid(row=5, column=3)

def print_lists():# para agregar en las listbox
  global listaReady, listaRunning, listaFinished, listaBlocked, Lbready, Lbrun, Lbfin, LbB
  i=1
  for process in listaReady:
    Lbready.insert(i, process.nombre)
    i=i+1
  i=1
  for process in listaRunning:
    Lbrun.insert(i, process.nombre)
    i=i+1 
  i=1
  for process in listaFinished:
    Lbfin.insert(i, process.nombre)
    i=i+1
  i=1
  for process in listaBlocked:
    LbB.insert(i, process.nombre)
    i=i+1

print_lists()

#tercera parte del gui "Schedule"
frameSchedule = tk.Frame(master=window, width=100, height=50, bg="yellow")
frameSchedule.pack(fill=tk.BOTH, expand=True)
label_schedule=tk.Label(frameSchedule, text="Scheduling", font=('Times', 12))
label_schedule.pack()

labelC = tk.Label(frameSchedule, text="CPU", font=('Times', 14))
labelC.pack()
x = tk.IntVar()
x.set(1)
opcionesCPU = [("FIFO", 1), 
                  ("Round Robin", 2),
                  ("SRT", 3),
                  ("HRRN", 4)]

#Mostrar las opciones---------------------------------------------------
for opciones, val in opcionesCPU: #opciones de scheduling, comand = ShowCPU
  tk.Radiobutton(frameSchedule, 
                   text=opciones,
                   padx = 20, 
                   variable=x,
                   font=('Times', 12), 
                   command=ShowCPU,
                   value=val).pack(anchor=tk.W)


    #Mostrar proceso en estado de running
label_nom=tk.Label(frameSchedule, text="Nombre: "+str(listaRunning[0].nombre), font=('Times', 12))
label_nom.pack()
label_llegada=tk.Label(frameSchedule, text="Tiempo de llegada: "+str(listaRunning[0].llegada), font=('Times', 12))
label_llegada.pack()
label_pag=tk.Label(frameSchedule, text="Paginas: "+str(listaRunning[0].paginas), font=('Times', 12))
label_pag.pack()
label_tEjec=tk.Label(frameSchedule, text="Tiempo estimado de Ejecución: "+str(listaRunning[0].tEjec), font=('Times', 12))
label_tEjec.pack()
label_cpuA=tk.Label(frameSchedule, text="CPU asignado: "+str(listaRunning[0].cpuAsignado), font=('Times', 12))
label_cpuA.pack()
label_cpuR=tk.Label(frameSchedule, text="CPU Restante: "+str(listaRunning[0].cpuRestante), font=('Times', 12))
label_cpuR.pack()
label_en=tk.Label(frameSchedule, text="Envejecimiento: "+str(listaRunning[0].Envejecimiento), font=('Times', 12))
label_en.pack()
label_q=tk.Label(frameSchedule, text="Quantum Restante: "+str(listaRunning[0].quantum), font=('Times', 12))
label_q.pack()
quantumRequest=tk.Label(frameSchedule, text="Quantum", font=('Times', 12))
e4=tk.Entry()
e4.pack()
quantumRequest.pack()
def showQ():
  if e4.get():
    numQ=int(e4.get())
button_addQ= tk.Button(frameSchedule, text="Add", width=5, height=2, font=('Times', 12), command=showQ)
button_addQ.pack()

frameMemory = tk.Frame(master=window, width=100, height=50, bg="blue")
frameMemory.pack(side="bottom", fill=tk.BOTH, expand=True)

window.mainloop()  