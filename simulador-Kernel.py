'''
Enrico Cecchini Rivera  - 531059  50%
Carmen Aurora Monjaras  - 531675  50%

Declaramos que hemos realizado esta actividad con integridad academica
'''

'''
Notas:
No se pasa primer proceso de blocked a Ready, y se duplican nombres cuando se pasan. Checar otra vez, ya se realizaron cambios
'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
contador=0

# ************* Algoritmos Para Enviar Procesos a Lista Correcta *************
# Metodo para agregar procesos a Finished
def agregarFinished():                         
    global listaRunning
    #global listaProcesos
    global listaFinished
    global listaReady
    global Lbrun
    global Lbfin
    global Lbready
    global label_page

    try:
      if listaRunning[0].cpuRestante == 0:
        listaRunning[0].estado = 4
        listaFinished.append(listaRunning[0])
        #listaRunning.pop()
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
    Lbrun.delete(0,END)
    for process in listaRunning:
      Lbrun.insert(END, process.nombre)
    Lbready.delete(0,END)
    for process in listaReady:
      Lbready.insert(END, process.nombre)
    Lbfin.delete(0,END)
    for process in listaFinished:
      Lbfin.insert(END, process.nombre)
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    for i in range(len(listaRunning[0].listaPags)):
      pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)
    


# Metodo para agregar procesos de Running a Blocked
def agregarBlocked():
    global listaRunning
    #global listaProcesos
    global listaBlocked
    global Lbrun
    global lbB
    global label_page
    listaRunning[0].estado = 2
    listaBlocked.append(listaRunning[0])
    Lbrun.delete(0,END)
    listaRunning.pop(0)
    LbB.delete(0,END)
    for process in listaBlocked:
      LbB.insert(END, process.nombre)
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    for i in range(len(listaRunning[0].listaPags)):
      pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)



# Metodo para agregar procesos de Running a Ready
def agregarRunningReady():
    global listaRunning
    global listaReady
    global Lbrun
    global Lbready
    global label_page
  
    listaRunning[0].estado = 3
    listaReady.append(listaRunning[0])
    Lbready.insert(END, listaRunning[0].nombre)
    Lbrun.delete(0, END)
    for process in listaRunning:
      Lbrun.insert(END, process.nombre)
    listaRunning.pop(0)
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    for i in range(len(listaRunning[0].listaPags)):
      pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)


# Metodo para agregar procesos de Blocked a Ready
def agregarBlockedReady():
    global listaBlocked
    global listaReady
    global Lbready
    global LbB
    global label_page

    listaBlocked[0].estado = 3
    listaReady.append(listaBlocked[0])

    print('****************** Testing BlockedReady *********************')
    for i in listaReady:
      print(i)

    nom=listaBlocked[0].nombre
    Lbready.insert(END,nom)
    listaBlocked.pop(0)
    LbB.delete(0,END)
    for process in listaBlocked:
      LbB.insert(END, process.nombre)
    Lbready.delete(0,END)
    for process in listaReady:
      Lbready.insert(END, process.nombre)
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    for i in range(len(listaRunning[0].listaPags)):
      pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)


# Metodo para agregar procesos de Ready a Running
def agregarReady():
    global listaReady
    global listaRunning
    global Lbready
    global Lbrun
    global label_page
    
    try:
      if not listaRunning:
          listaRunning.append(listaReady[0])
          nom=listaReady[0].nombre
          listaReady.pop(0)
          Lbready.delete(0,END)
          for process in listaReady:
            Lbready.insert(END, process.nombre)
          Lbrun.delete(0,END)
          for process in listaRunning:
            Lbrun.insert(END, process.nombre)
    except IndexError:
      pass
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    for i in range(len(listaRunning[0].listaPags)):
      pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)

    

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
    label_TActual.config(text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 10))
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
    label_nom.config(text="Nombre: "+ str(listaRunning[0].nombre), font=('Times', 10))
    label_llegada.config(text="Tiempo de llegada: "+ str(listaRunning[0].llegada), font=('Times', 10))
    label_pag.config(text="Paginas: "+ str(listaRunning[0].paginas), font=('Times', 10))
    label_tEjec.config(text="Tiempo estimado de ejecución: "+ str(listaRunning[0].tEjec), font=('Times', 10))
    label_cpuA.config(text="CPU Asignado: "+ str(listaRunning[0].cpuAsignado), font=('Times', 10))
    label_cpuR.config(text="CPU Restante: "+ str(listaRunning[0].cpuRestante), font=('Times', 10))
    label_en.config(text="Envejecimiento: "+ str(listaRunning[0].Envejecimiento), font=('Times', 10))
    label_q.config(text="Quantum Restante: "+ str(listaRunning[0].quantum), font=('Times', 10))
    
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


# ****** Algoritmos de Scheduling ******
# FIFO
def algoritmoFIFO():
    global listaReady
    global listaRunning
    global listaFinished
    global Lbready
    global Lbrun
    global Lbfin
    global label_page
    
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
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    if listaRunning:
      for i in range(len(listaRunning[0].listaPags)):
            pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
      label_page.config(text=pagesText)


# Round Robin
def algoritmoRoundRobin():
    global listaReady
    global listaRunning
    global listaFinished
    global Lbready
    global Lbrun
    global Lbfin
    global label_page
    global e4
    if not listaReady:
        return
    if not listaRunning or listaRunning[0].quantum == 0:    # Si la lista de Running esta vacia, agrega primer
        if listaRunning:                                    # proceso de Ready y lo quita de la lista, si no esta vacia
            listaRunning[0].quantum = 0                     # y se acabo el quantum del proceso actual, se resetea a 4,
            agregarRunningReady() 
            #algoritmoRoundRobin()                           # se envia el proceso a Ready y se agrega el siguiente
        listaRunning.append(listaReady[0])
        if e4.get():
          listaRunning[0].quantum= int(e4.get())+1
        else:
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
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    if listaRunning:
      for i in range(len(listaRunning[0].listaPags)):
            pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
      label_page.config(text=pagesText)


# Metodo de SRT Apropiativo
def algoritmoSRT():
    global listaRunning
    global listaReady
    global Lbready
    global Lbrun
    global Lbfin
    global label_page
    
    try:
      if listaRunning:
        if not checarFinProceso():
          agregarFinished()
          algoritmoSRT()
        #else:  
          #agregarRunningReady()                                   # Quita proceso que se esta ejecutando y lo agrega a Ready
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
    #Checa las cosas en la interfaz gráfica
    Lbready.delete(0,END)
    Lbrun.delete(0,END)
    for process in listaReady:
      Lbready.insert(process.nombre)
    for process in listaRunning:
      Lbrun.insert(process.nombre)
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    if listaRunning:
      for i in range(len(listaRunning[0].listaPags)):
            pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
      label_page.config(text=pagesText)

# Metodo de HRRN Apropiativo
def algoritmoHRRN():
    global listaRunning
    global listaReady
    global Lbready
    global Lbrun
    global Lbfin
    global label_page
    
    try:
      if listaRunning:
        if not checarFinProceso():
          agregarFinished()
          algoritmoHRRN()
      else:
        procesoTemp = listaReady[0]
        prioridadTemp = (procesoTemp.Envejecimiento+procesoTemp.tEjec)/procesoTemp.tEjec
        for proceso in listaReady:
            prioridadProceso = (proceso.Envejecimiento+proceso.tEjec)/proceso.tEjec  
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
    pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
    if listaRunning:
      for i in range(len(listaRunning[0].listaPags)):
            pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
      label_page.config(text=pagesText)

def execTime():
  global tiempoActual
  global listaRunning
  global listaBlocked
  global contador
  global label_page
  global label_nom, label_llegada, label_pag, label_tEjec, label_cpuA, label_cpuR, label_en, label_q
  # Testing
  print('\n****Testing****\n')
  for proceso in listaBlocked:
    print(proceso.printProceso())
    print('')
  
  print('Contador:',contador)
  print('\n****************\n')

  print('Test Contador:',contador)
  try:
    if  contador > 0 and contador%5 == 0:
      agregarBlockedReady()
  except IndexError:
    pass
      
  try:
    tiempoActual+=1
    label_TActual.config(text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 10))
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
    
    label_nom.config(text="Nombre: "+ str(listaRunning[0].nombre), font=('Times', 10))
    label_llegada.config(text="Tiempo de llegada: "+ str(listaRunning[0].llegada), font=('Times', 10))
    label_pag.config(text="Paginas: "+ str(listaRunning[0].paginas), font=('Times', 10))
    label_tEjec.config(text="Tiempo estimado de ejecución: "+ str(listaRunning[0].tEjec), font=('Times', 10))
    label_cpuA.config(text="CPU Asignado: "+ str(listaRunning[0].cpuAsignado), font=('Times', 10))
    label_cpuR.config(text="CPU Restante: "+ str(listaRunning[0].cpuRestante), font=('Times', 10))
    label_en.config(text="Envejecimiento: "+ str(listaRunning[0].Envejecimiento), font=('Times', 10))
    label_q.config(text="Quantum Restante: "+ str(listaRunning[0].quantum), font=('Times', 10))
    
    
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

  # Aumenta numero de accesos, y cambia bit de escritura si se accesa 5 veces
    if listaRunning:
      for i in range(len(listaRunning[0].listaPags)):
        if listaRunning[0].listaPags[i][1] == 1:
          if listaRunning[0].listaPags[i][4] == 5:
            listaRunning[0].listaPags[i][6] = 1
          listaRunning[0].listaPags[i][5] = 1 

  pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"
  
  if listaRunning:
    for i in range(len(listaRunning[0].listaPags)):
          pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
    label_page.config(text=pagesText)


  
def refresh():
  #resetea las opciones de las interrupciones
  v.set(None)

def refreshCPU():
  #resetea las opciones de scheduling
  x.set(1)

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
    global tiempoActual

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
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexViejo][3] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][1] = 1
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1
    
    agregarBlocked()
        

# Algoritmo de Paginacion LRU
def pagLRU():
    global limitePags
    global listaRunning
    global tiempoActual

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
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexViejo][3] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][1] = 1
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1
    
    agregarBlocked()

# Algoritmo de Paginacion LFU
def pagLFU():
    global limitePags
    global listaRunning
    global tiempoActual

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
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1

    # Si no, se apaga la pagina vieja y activa la nueva
    else:
        listaRunning[0].listaPags[indexViejo][1] = 0
        listaRunning[0].listaPags[indexViejo][3] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][1] = 1
        listaRunning[0].listaPags[indexNuevo][2] = tiempoActual
        listaRunning[0].listaPags[indexNuevo][5] = 1
    
    agregarBlocked()

def pagNUR():
    global limitePags
    global listaRunning
    global tiempoActual
    
    prioridadOff0 = []
    prioridadOff1 = []
    prioridadOff2 = []
    prioridadOff3 = []

    prioridadAct0 = []
    prioridadAct1 = []
    prioridadAct2 = []
    prioridadAct3 = []

    pagAct = 0
    for i in range(len(listaRunning[0].listaPags)):
        if listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 0:
            prioridadOff0.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 0:
            prioridadOff1.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 1:
            prioridadOff2.append(i)
        elif listaRunning[0].listaPags[i][1] == 0 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 1:
            prioridadOff3.append(i)
        if listaRunning[0].listaPags[i][1] == 1 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 0:
            prioridadAct0.append(i)
        elif listaRunning[0].listaPags[i][1] == 1 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 0:
            prioridadAct0.append(i)
        elif listaRunning[0].listaPags[i][1] == 1 and listaRunning[0].listaPags[i][5] == 0 and listaRunning[0].listaPags[i][6] == 1:
            prioridadAct2.append(i)
        elif listaRunning[0].listaPags[i][1] == 1 and listaRunning[0].listaPags[i][5] == 1 and listaRunning[0].listaPags[i][6] == 1:
            prioridadAct3.append(i)
        
        if listaRunning[0].listaPags[i][1] == 1:
            pagAct+=1

    prioridadesOff = prioridadOff0 + prioridadOff1 + prioridadOff2 + prioridadOff3
    prioridadesAct = prioridadAct0 + prioridadAct1 + prioridadAct2 + prioridadAct3

    # Si no se ha llegado al limite de procesos, se enciende el de mayor prioridad
    if pagAct < limitePags:
        listaRunning[0].listaPags[prioridadesOff[0]][1] = 1
        listaRunning[0].listaPags[prioridadesOff[0]][2] = tiempoActual
        listaRunning[0].listaPags[prioridadesOff[0]][5] = 1
    
    # Se apaga el proceso de menor prioridad y se activa el de mayor prioridad
    else:
        listaRunning[0].listaPags[prioridadesAct[-1]][1] = 0
        listaRunning[0].listaPags[prioridadesAct[-1]][3] = tiempoActual
        listaRunning[0].listaPags[prioridadesOff[0]][1] = 1
        listaRunning[0].listaPags[prioridadesOff[0]][2] = tiempoActual
        listaRunning[0].listaPags[prioridadesOff[0]][5] = 1
    
    agregarBlocked()



# Clase proceso para crear cada proceso nuevo introducido al sistema
class Proceso:
    def __init__(self, nombre, llegada, paginas, tEjec, estado, listaPags):
        self.nombre = nombre
        self.llegada = llegada
        self.paginas = paginas
        self.tEjec = tEjec
        self.estado = estado
        self.listaPags = listaPags
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
        listaPags = []
        
        n = 0
        for pag in range(numPags):
            pagina = f.readline().replace(' ','').replace('\n','').split(',')
            res = int(pagina[0])
            tLlegada = int(pagina[1])
            ultAccess = int(pagina[2])
            numAccess = int(pagina[3])
            bitLectura = int(pagina[4])
            bitEscritura = int(pagina[5])
            page = [n, res, tLlegada, ultAccess, numAccess, bitLectura, bitEscritura]
            listaPags.append(page)
            n+=1
        procesoNuevo = Proceso(i+1, llegada, numPags, tiempoTotal, estado, listaPags)
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
    listaPags = []
    
    for i in range(paginas):
        pag = [i, 0, 0, 0, 0, 0, 0]
        listaPags.append(pag)
    procesoNuevo = Proceso(nombre, llegada, paginas, tiempoTotal, 3, listaPags)
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
limitePags, tiempoActual = lecturaArchivo(archivo)

#1-running 2-blocked 3-ready
window = tk.Tk()
window.title("Kernel Project")
#parte de arriba
frameTop = tk.Frame( master=window, width=100, height=25, bg="grey")
frameTop.pack(fill=tk.BOTH, expand=True)
label_TActual = tk.Label(frameTop, text="Tiempo Actual: "+ str(tiempoActual), font=('Times', 10))
label_TActual.pack()
button_Exec= tk.Button(frameTop, text="Ejecutar", width=5, height=2, font=('Times', 10), command=execTime)
button_Exec.pack() 

def ShowChoiceP(): #obtener la página a ejecutar
  global tiempoActual, contado
  global listaReady
  global listaRunning 
  global listaBlocked
  global listaFinished
  global tkvar
  opcion=int(valor.get())
  métodoPaginacion=tkvar.get()
  print(len(listaRunning[0].listaPags))
  if opcion<len(listaRunning[0].listaPags):
    if (opcion==1 and listaRunning[0].listaPags[0][1]==1):
        print("pag 0")
        execTime()
    elif(opcion==1 and listaRunning[0].listaPags[0][1]==0):
      print("pag 0 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==2 and listaRunning[0].listaPags[1][1]==1):
      print("pag 1")
      execTime()
    elif (opcion==2 and listaRunning[0].listaPags[1][1]==0):
      print("pag 1 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==3 and listaRunning[0].listaPags[2][1]==1):
      print("pag 2")
      execTime()
    elif (opcion==3 and listaRunning[0].listaPags[2][1]==0):
      print("pag 2 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==4 and listaRunning[0].listaPags[3][1]==1):
      print("pag 3")
      execTime()
    elif (opcion==4 and listaRunning[0].listaPags[3][1]==0):
      print("pag 3 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==5 and listaRunning[0].listaPags[4][1]==1):
      print("pag 4")
      execTime()
    elif (opcion==5 and listaRunning[0].listaPags[4][1]==0):
      print("pag 4 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==6 and listaRunning[0].listaPags[5][1]==1):
      print("pag 5")
      execTime()
    elif (opcion==6 and listaRunning[0].listaPags[5][1]==0):
      print("pag 5 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==7 and listaRunning[0].listaPags[6][1]==1):
      print("pag 6")
      execTime()
    elif (opcion==7 and listaRunning[0].listaPags[6][1]==0):
      print("pag 6 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()
    elif (opcion==8 and listaRunning[0].listaPags[7][1]==1):
      print("pag 7")
      execTime()
    elif (opcion==8 and listaRunning[0].listaPags[7][1]==0):
      print("pag 7 no cargada")
      if tkvar.get()=='FIFO':
          print("FIFOM")
          pagFIFO()
      if tkvar.get()=='LRU':
          print("LRUM")
          pagLRU()
      if tkvar.get()=='LFU':
          print("LFUM")
          pagLFU()
      if tkvar.get()=='NUR':
          print("NURM")
          pagNUR()

valor=tk.IntVar()
valor.set(None)
myPages = [("0", 1), ("1", 2), ("2", 3), ("3", 4), ("4", 5), ("5", 6), ("6", 7), ("7", 8)]
for choice, val in myPages:
  tk.Radiobutton(frameTop, 
                   text=choice,
                   padx = 20, 
                   variable=valor, 
                   font=('Times', 10), 
                   command=ShowChoiceP,
                   value=val).pack(anchor=tk.W)



labelI = tk.Label(frameTop, text="Escoja una interrupcion", font=('Times', 10))
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
                   font=('Times', 10), 
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

button_refresh= tk.Button(frameTop, text="Refresh", width=5, height=2, font=('Times', 10), command=refresh)
button_refresh.pack()
# segunda parte del gui
frameCPU = tk.Frame(master=window, width=100, height=100, bg="red")
frameCPU.pack(fill=tk.BOTH, expand=True)

#Mostrar los valores de NEW---------------------------------------------------
def show_entry_fields():#añadir proceso al oprimir botón
    #print("Nom: %s\npags: %s\nEjecTotal: %s\nLlegada: %s" % (e1.get(), e2.get(), e3.get(), str(tiempoActual)))
    crearProceso(listaReady, tiempoActual)

#fields= "Nombre", "Pags", "Ejec Total"
tk.Label(frameCPU, text="Nombre", font=('Times', 10)).grid(row=0)
tk.Label(frameCPU, text="Pags", font=('Times', 10)).grid(row=1)
tk.Label(frameCPU, text="Ejec total", font=('Times', 10)).grid(row=2)

e1 = tk.Entry(frameCPU) #Nombre de proceso
e2 = tk.Entry(frameCPU) #Num de pags
e3 = tk.Entry(frameCPU) #ejecucion total

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(frameCPU,text='Add', font=('Times', 10), command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
#Listas
label_ready=tk.Label(frameCPU, text="Ready", font=('Times', 10)).grid(row=4)
label_run=tk.Label(frameCPU, text="Running", font=('Times', 10)).grid(row=4, column=1)
label_fin=tk.Label(frameCPU, text="Finished", font=('Times', 10)).grid(row=4, column=2)
label_B=tk.Label(frameCPU, text="Blocked", font=('Times', 10)).grid(row=4, column=3)

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
label_schedule=tk.Label(frameSchedule, text="Scheduling", font=('Times', 10))
label_schedule.pack()

labelC = tk.Label(frameSchedule, text="CPU", font=('Times', 10))
labelC.pack()
x = tk.IntVar()
x.set(1)
opcionesCPU = [("FIFO", 1), 
                  ("Round Robin", 2),
                  ("SRT", 3),
                  ("HRRN", 4)]

#Mostrar las opciones---------------------------------------------------
for opciones, val in opcionesCPU: #opciones de scheduling, comand = ShowCPU
  tk.Radiobutton(frameSchedule, text=opciones, padx = 20, variable=x, font=('Times', 10), command=ShowCPU, value=val).pack(anchor=tk.W, side=tk.LEFT)


    #Mostrar proceso en estado de running
label_nom=tk.Label(frameSchedule, text="Nombre: "+str(listaRunning[0].nombre), font=('Times', 10))
label_nom.pack()
label_llegada=tk.Label(frameSchedule, text="Tiempo de llegada: "+str(listaRunning[0].llegada), font=('Times', 10))
label_llegada.pack()
label_pag=tk.Label(frameSchedule, text="Paginas: "+str(listaRunning[0].paginas), font=('Times', 10))
label_pag.pack()
label_tEjec=tk.Label(frameSchedule, text="Tiempo estimado de Ejecución: "+str(listaRunning[0].tEjec), font=('Times', 10))
label_tEjec.pack()
label_cpuA=tk.Label(frameSchedule, text="CPU asignado: "+str(listaRunning[0].cpuAsignado), font=('Times', 10))
label_cpuA.pack()
label_cpuR=tk.Label(frameSchedule, text="CPU Restante: "+str(listaRunning[0].cpuRestante), font=('Times', 10))
label_cpuR.pack()
label_en=tk.Label(frameSchedule, text="Envejecimiento: "+str(listaRunning[0].Envejecimiento), font=('Times', 10))
label_en.pack()
label_q=tk.Label(frameSchedule, text="Quantum Restante: "+str(listaRunning[0].quantum), font=('Times', 10))
label_q.pack()
quantumRequest=tk.Label(frameSchedule, text="Quantum", font=('Times', 10))
e4=tk.Entry()

quantumRequest.pack()
e4.pack()
def showQ():
  if e4.get():
    numQ=int(e4.get())
button_addQ= tk.Button(frameSchedule, text="Add", width=5, height=2, font=('Times', 10), command=showQ)
button_addQ.pack()

frameMemory = tk.Frame(master=window, width=100, height=50, bg="blue")
frameMemory.pack(side="bottom", fill=tk.BOTH, expand=True)

'dropdown button'
tkvar = StringVar(frameMemory)
choices = { 'FIFO', 'LRU', 'LFU', 'NUR'}
tkvar.set('FIFO')

popupMenu = OptionMenu(frameMemory, tkvar, *choices)
Label(frameMemory, text="Memoria").pack()
popupMenu.pack()

def change_dropdown(*args):
    if tkvar.get()=='FIFO':
      print("FIFOM")
    if tkvar.get()=='LRU':
      print("LRUM")
    if tkvar.get()=='LFU':
      print("LFUM")
    if tkvar.get()=='NUR':
      print("NURM")
    
      
tkvar.trace('w', change_dropdown)

buttonReset= tk.Button(frameMemory, text="Reset bit NUR", width=10, height=3, font=('Times', 10), command = resetNur)
buttonReset.pack()

label_page=tk.Label(frameMemory,text="", font=('Times', 10))
label_page.pack()

pagesText="Page Residencia Llegada ultAccess Accessos NUR\n"

for i in range(len(listaRunning[0].listaPags)):
  pagesText+= str(listaRunning[0].listaPags[i][0])+(" "*10)+ str(listaRunning[0].listaPags[i][1])+(" "*10)+str(listaRunning[0].listaPags[i][2])+(" "*10)+str(listaRunning[0].listaPags[i][3])+(" "*10)+str(listaRunning[0].listaPags[i][4])+(" "*11)+str(listaRunning[0].listaPags[i][5])+str(listaRunning[0].listaPags[i][6])+"\n"
label_page.config(text=pagesText)

window.mainloop()   