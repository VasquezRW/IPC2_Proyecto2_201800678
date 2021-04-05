import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from lectorXML import *
from metodos import *
from objetos import *
from escribirHTML import *
import metodos

ws = Tk()
ws.title("Proyecto 2 IPC2")
ws.iconbitmap('usacIcono.ico')
ws.geometry("1000x750")

matrices = linked_list_circular()
global opciones
opciones = []
matrizResultante = None
reportes = []


def escoger_archivo():
    global matrices
    ws.filename = filedialog.askopenfilename(title="Seleccione el archivo",
                                             filetypes=(("Archivos XML", "*.xml"),
                                                        ("all files", "*.*")))
    if ws.filename != '':
        matrices = leer_Archivo(ws.filename)
        matrices.imprimir()
        global opciones
        opciones = matrices.obtener_Nombres()
        print(opciones)
        global selecMA
        clickedA.set("Ninguna")
        selecMA.destroy()
        selecMA = OptionMenu(frameSelecMA, clickedA, *opciones)
        selecMA.grid(row=0, column=0)
        global selecMB
        clickedB.set("Ninguna")
        selecMB.destroy()
        selecMB = OptionMenu(frameSelecMB, clickedB, *opciones)
        selecMB.grid(row=0, column=0)

        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Archivos Cargados",
                          "Carga de Archivos",
                          opciones
                          )
        reportes.append(reporte)
    else:

        messagebox.showerror('Error', 'No se selecciono ningun archivo')


def datosEstudiante():
    messagebox.showinfo('Datos del Estudiante', 'Wilmer Estuardo Vasquez Raxon \n'
                                                '201800678\n'
                                                'Introduccion a la programacion y computacion 2 seccion \"E\" \n'
                                                'Ingenieria en Ciencias y Sistemas\n'
                                                '4to Semestre')


def documentacion():
    messagebox.showinfo('Datos del Estudiante', 'aun no hay :v ')


def rotarHorizontalA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    matrizOperada = rotarHorizontalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizA()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz rotada horizontalmente de manera correcta",
                      "Rotacion Horizontal",
                      nombres
                      )
    reportes.append(reporte)


def rotarHorizontalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    matrizOperada = rotarHorizontalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizB()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz rotada horizontalmente de manera correcta",
                      "Rotacion Horizontal",
                      nombres
                      )
    reportes.append(reporte)


def rotarVerticalA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    matrizOperada = rotarVerticalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizA()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz rotada verticalmente de manera correcta",
                      "Rotacion Vertical",
                      nombres
                      )
    reportes.append(reporte)


def rotarVerticalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    matrizOperada = rotarVerticalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizB()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz rotada verticalmente de manera correcta",
                      "Rotacion Vertical",
                      nombres
                      )
    reportes.append(reporte)


def transpuestaA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    matrizOperada = transpuestaMatriz(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizA()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz transpuesta de manera correcta",
                      "Transpuesta",
                      nombres
                      )
    reportes.append(reporte)


def transpuestaB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    matrizOperada = transpuestaMatriz(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizB()
    nombres = [matriz.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz transpuesta de manera correcta",
                      "Transpuesta",
                      nombres
                      )
    reportes.append(reporte)


def limpiarZonaA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    filaInicio = int(entry_filaInicioA.get())
    columnaInicio = int(entry_columnaInicioA.get())
    filaFin = int(entry_filaFinA.get())
    columnaFin = int(entry_columnaFinA.get())
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < filaFin <= matriz.filas and 0 < columnaFin <= matriz.filas:
        matrizOperada = limpiarZona(matriz, filaInicio, columnaInicio, filaFin, columnaFin)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizA()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Matriz Limpiada Correctamente",
                          "Limpiar Zona",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Limpiar Zona",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def limpiarZonaB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    filaInicio = int(entry_filaInicioB.get())
    columnaInicio = int(entry_columnaInicioB.get())
    filaFin = int(entry_filaFinB.get())
    columnaFin = int(entry_columnaFinB.get())
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < filaFin <= matriz.filas and 0 < columnaFin <= matriz.filas:
        matrizOperada = limpiarZona(matriz, filaInicio, columnaInicio, filaFin, columnaFin)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizB()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Matriz Limpiada Correctamente",
                          "Limpiar Zona",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Limpiar Zona",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addLineaHorizontalA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    filaInicio = int(entry_filaInicioA.get())
    columnaInicio = int(entry_columnaInicioA.get())
    longitud = int(entry_altoLongA.get())
    posFin = columnaInicio + longitud
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas:
        matrizOperada = agregarLineaHorizontal(matriz, filaInicio, columnaInicio, longitud)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizA()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Linea horizonal agregada correctamente",
                          "Agregar linea horizontal",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar linea horizontal",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addLineaVerticalA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    filaInicio = int(entry_filaInicioA.get())
    columnaInicio = int(entry_columnaInicioA.get())
    longitud = int(entry_altoLongA.get())
    posFin = filaInicio + longitud
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas:
        matrizOperada = agregarLineaVertical(matriz, filaInicio, columnaInicio, longitud)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizA()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Linea vertical agregada correctamente",
                          "Agregar linea vertical",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar linea vertical",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addLineaHorizontalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    filaInicio = int(entry_filaInicioB.get())
    columnaInicio = int(entry_columnaInicioB.get())
    longitud = int(entry_altoLongB.get())
    posFin = columnaInicio + longitud
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas:
        matrizOperada = agregarLineaHorizontal(matriz, filaInicio, columnaInicio, longitud)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizB()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Linea horizontal agregada correctamente",
                          "Agregar linea horizontal",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar linea horizontal",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addLineaVerticalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    filaInicio = int(entry_filaInicioB.get())
    columnaInicio = int(entry_columnaInicioB.get())
    longitud = int(entry_altoLongB.get())
    posFin = filaInicio + longitud
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas:
        matrizOperada = agregarLineaVertical(matriz, filaInicio, columnaInicio, longitud)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizB()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Linea vertical agregada correctamente",
                          "Agregar linea vertical",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar linea vertical",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addRectanguloA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    filaInicio = int(entry_filaInicioA.get())
    columnaInicio = int(entry_columnaInicioA.get())
    alto = int(entry_altoLongA.get())
    ancho = int(entry_anchoA.get())
    posFin = filaInicio + alto
    posFin2 = columnaInicio + ancho
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas and 0 < posFin2 <= matriz.filas:
        matrizOperada = agregarRectangulo(matriz, filaInicio, columnaInicio, alto, ancho)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizA()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Rectangulo agregada correctamente",
                          "Agregar rectangulo",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar rectangulo",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addTrianguloA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    filaInicio = int(entry_filaInicioA.get())
    columnaInicio = int(entry_columnaInicioA.get())
    alto = int(entry_altoLongA.get())
    ancho = int(entry_anchoA.get())
    posFin = filaInicio + alto
    posFin2 = columnaInicio + ancho
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas and 0 < posFin2 <= matriz.filas:
        matrizOperada = agregarTrianguloRectangulo(matriz, filaInicio, columnaInicio, alto, ancho)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizA()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Triangulo rectangulo agregada correctamente",
                          "Agregar triangulo rectangulo",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar triangulo rectangulo",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addRectanguloB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    filaInicio = int(entry_filaInicioB.get())
    columnaInicio = int(entry_columnaInicioB.get())
    alto = int(entry_altoLongB.get())
    ancho = int(entry_anchoB.get())
    posFin = filaInicio + alto
    posFin2 = columnaInicio + ancho
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas and 0 < posFin2 <= matriz.filas:
        matrizOperada = agregarRectangulo(matriz, filaInicio, columnaInicio, alto, ancho)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizB()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Rectangulo agregada correctamente",
                          "Agregar rectangulo",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar rectangulo",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def addTrianguloB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    filaInicio = int(entry_filaInicioB.get())
    columnaInicio = int(entry_columnaInicioB.get())
    alto = int(entry_altoLongB.get())
    ancho = int(entry_anchoB.get())
    posFin = filaInicio + alto
    posFin2 = columnaInicio + ancho
    if 0 < filaInicio <= matriz.filas and 0 < columnaInicio <= matriz.filas and 0 < posFin <= matriz.filas and 0 < posFin2 <= matriz.filas:
        matrizOperada = agregarTrianguloRectangulo(matriz, filaInicio, columnaInicio, alto, ancho)
        matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
        cargarMatrizB()
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Triangulo rectangulo agregada correctamente",
                          "Agregar triangulo rectangulo",
                          nombres
                          )
        reportes.append(reporte)
    else:
        nombres = [matriz.nombre]
        reporte = Reporte(time.strftime("%d/%m/%y"),
                          time.strftime("%H:%M:%S"),
                          "Limites incorrectos",
                          "Agregar triangulo rectangulo",
                          nombres
                          )
        reportes.append(reporte)
        messagebox.showerror('Error', 'Limites incorrectos')


def unionAB():
    matrizA = matrices.obtener_Matriz(clickedA.get())
    matrizB = matrices.obtener_Matriz(clickedB.get())
    matrizResultante = unionMatrizAB(matrizA, matrizB)
    # matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizR(matrizResultante)
    nombres = [matrizA.nombre, matrizB.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Union A y B correcta",
                      "Union A,B",
                      nombres
                      )
    reportes.append(reporte)


def interseccionAB():
    matrizA = matrices.obtener_Matriz(clickedA.get())
    matrizB = matrices.obtener_Matriz(clickedB.get())
    matrizResultante = interseccionMatrizAB(matrizA, matrizB)
    # matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizR(matrizResultante)
    nombres = [matrizA.nombre, matrizB.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Interseccion A y B correcta",
                      "Interseccion A,B",
                      nombres
                      )
    reportes.append(reporte)


def diferenciaAB():
    matrizA = matrices.obtener_Matriz(clickedA.get())
    matrizB = matrices.obtener_Matriz(clickedB.get())
    matrizResultante = diferenciaMatrizAB(matrizA, matrizB)
    # matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizR(matrizResultante)
    nombres = [matrizA.nombre, matrizB.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Diferencia A y B correcta",
                      "Diferencia A,B",
                      nombres
                      )
    reportes.append(reporte)


def diferenciaSimetricaAB():
    matrizA = matrices.obtener_Matriz(clickedA.get())
    matrizB = matrices.obtener_Matriz(clickedB.get())
    matrizResultante = diferenciaSimetricaMatrizAB(matrizA, matrizB)
    # matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizR(matrizResultante)
    nombres = [matrizA.nombre, matrizB.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Diferencia simetrica A y B correcta",
                      "Diferencia Simetrica A,B",
                      nombres
                      )
    reportes.append(reporte)


def sustituirA():
    matrizA = matrices.obtener_Matriz(clickedA.get())
    matrices.reemplazar_Matriz(matrizA.nombre, matrizResultante)
    nombres = [matrizA.nombre, matrizResultante.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz resultante sustituida en matriz A",
                      "Sustituir en A",
                      nombres
                      )
    reportes.append(reporte)


def sustituirB():
    matrizB = matrices.obtener_Matriz(clickedB.get())
    matrices.reemplazar_Matriz(matrizB.nombre, matrizResultante)
    nombres = [matrizB.nombre, matrizResultante.nombre]
    reporte = Reporte(time.strftime("%d/%m/%y"),
                      time.strftime("%H:%M:%S"),
                      "Matriz resultante sustituida en matriz B",
                      "Sustituir en B",
                      nombres
                      )
    reportes.append(reporte)


'''
def crearMatriz(frame, matriz, ruta):
    for i in range(matriz.filas):
        for j in range(matriz.columnas):
            if matriz.comprobarPosicion(i, j):
                label = Label(frame, text="*")
                label.config(font=('Arial', 14))
                label.grid(row=i, column=j, padx=1, pady=1)
                frame.grid_columnconfigure(i, weight=1)
            else:
                label = Label(frame, text="-")
                label.grid(row=i, column=j, padx=1, pady=1)
                frame.grid_columnconfigure(j, weight=1)
'''


def crearMatriz(frame, ruta):
    img = Image.open(ruta)
    image = ImageTk.PhotoImage(img)
    imgFrame = Label(frame, image=image)
    imgFrame.pack()


def cargarMatrizA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    labelMA_Auxiliar.destroy()
    global frameMatrizA
    frameMatrizA.destroy()
    frameMatrizA = LabelFrame(frameAreaMA, text='Matriz A')
    frameMatrizA.grid(row=0, column=0)
    matrizNueva = metodos.crearMatriz(matriz, matriz.filas, matriz.columnas)
    ruta = generarGrafica(matrizNueva, matriz.nombre, "matrizA")
    crearMatriz(frameMatrizA, ruta)


def cargarMatrizB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    labelMB_Auxiliar.destroy()
    global frameMatrizB
    frameMatrizB.destroy()
    frameMatrizB = LabelFrame(frameAreaMB, text='Matriz B')
    frameMatrizB.grid(row=0, column=0)
    crearMatriz(frameMatrizB, matriz)
    matrizNueva = metodos.crearMatriz(matriz, matriz.filas, matriz.columnas)
    generarGrafica(matrizNueva, matriz.nombre)


def cargarMatrizR(matriz):
    labelMB_Auxiliar.destroy()
    global frameMatrizR
    frameMatrizR.destroy()
    frameMatrizR = LabelFrame(frameMatrizResultante, text='Matriz Resultante')
    frameMatrizR.grid(row=0, column=0)
    crearMatriz(frameMatrizR, matriz)
    matrizNueva = metodos.crearMatriz(matriz, matriz.filas, matriz.columnas)
    generarGrafica(matrizNueva, matriz.nombre)


def generarHTML():
    for reporte in reportes:
        reporte.imprimir()
    escribirArchivoHTML(reportes)


menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
cargarArchivo = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
# file.add_command(label="New")
cargarArchivo.add_command(label="Seleccionar Archivo", command=escoger_archivo)
# file.add_separator()
menubar.add_cascade(label="Cargar Archivo", menu=cargarArchivo)

edit = Menu(menubar, tearoff=0)
edit.add_command(label="Generar HTML", command=generarHTML)
menubar.add_cascade(label="Reportes", menu=edit)

help = Menu(menubar, tearoff=0)
help.add_command(label="Datos del estudiante", command=datosEstudiante)
help.add_command(label="Documentacion", command=documentacion)
menubar.add_cascade(label="Ayuda", menu=help)

salir = Menu(menubar, tearoff=0)
salir.add_command(label="Salir", command=ws.quit)
menubar.add_cascade(label="Salir", menu=salir)

ws.config(menu=menubar)

frameTitulo = Frame(ws)
frameTitulo.grid(row=0, column=0)

Label(frameTitulo, text="Operadora de imagenes", font=("arial italic", 18)).pack()

# frame de seleccion de matrices A y B
frameMAB = Frame(ws)
frameMAB.grid(row=1, column=0)

# frame de principal
framePrincipal = Frame(ws)
framePrincipal.grid(row=2, column=0)

# frame de operaciones y matriz A
frameAreaMA = Frame(framePrincipal)
frameAreaMA.grid(row=0, column=0)

# frame de operaciones entre matrices
frameAreaOp = Frame(framePrincipal)
frameAreaOp.grid(row=0, column=1)

# frame de operaciones y matriz B
frameAreaMB = Frame(framePrincipal)
frameAreaMB.grid(row=0, column=2)

# frame de operador igual =
frameOpIgual = Frame(framePrincipal)
frameOpIgual.grid(row=0, column=3)

# frame de matriz resultante
frameMatrizResultante = Frame(framePrincipal)
frameMatrizResultante.grid(row=0, column=4)

# frame de matriz A
frameMatrizA = LabelFrame(frameAreaMA, text='Matriz A')
frameMatrizA.grid(row=0, column=0)

# frame de operaciones matriz A
frameOperacionesMatrizA = LabelFrame(frameAreaMA, text='Operaciones de Matriz A')
frameOperacionesMatrizA.grid(row=1, column=0)

# frame de matriz B
frameMatrizB = LabelFrame(frameAreaMB, text='Matriz B')
frameMatrizB.grid(row=0, column=0)

# frame de operaciones matriz B
frameOperacionesMatrizB = LabelFrame(frameAreaMB, text='Operaciones de Matriz B')
frameOperacionesMatrizB.grid(row=1, column=0)

# frame de matriz resultante
frameMatrizR = LabelFrame(frameMatrizResultante, text='Matriz Resultante')
frameMatrizR.grid(row=0, column=0)

# frame de operaciones de matriz resultante
frameOpMR = LabelFrame(frameMatrizResultante, text='Operaciones de Matriz Resultante')
frameOpMR.grid(row=1, column=0)

# frame de signo de operaciones entre matrices
frameSignoOperaciones = LabelFrame(frameAreaOp, text='')
frameSignoOperaciones.grid(row=0, column=0)

# frame de operaciones entre matrices
frameOperaciones = LabelFrame(frameAreaOp, text='Operaciones entre matrices A,B')
frameOperaciones.grid(row=1, column=0)

# frame de seleccion matriz A
frameSelecMA = LabelFrame(frameMAB, text='Seleccione la matriz A')
frameSelecMA.grid(row=0, column=0)

# frame de seleccion matriz B
frameSelecMB = LabelFrame(frameMAB, text='Seleccione la matriz B')
frameSelecMB.grid(row=0, column=1)

# combo box y botones de carga de matrices y seleccion de matrices A y B
clickedA = StringVar()
clickedA.set("Ninguna")
selecMA = OptionMenu(frameSelecMA, clickedA, opciones)
selecMA.grid(row=0, column=0)
Button(frameSelecMA, text="Cargar Matriz A", command=cargarMatrizA).grid(row=1, column=0)

clickedB = StringVar()
clickedB.set("Ninguna")
selecMB = OptionMenu(frameSelecMB, clickedB, opciones)
selecMB.grid(row=0, column=0)
Button(frameSelecMB, text="Cargar Matriz B", command=cargarMatrizB).grid(row=1, column=0)

# matriz A
labelMA_Auxiliar = Label(frameMatrizA, text="Matriz A, en construccion", font=("arial italic", 10))
labelMA_Auxiliar.grid(row=0, column=0)
# matriz B
labelMB_Auxiliar = Label(frameMatrizB, text="Matriz B, en construccion", font=("arial italic", 10))
labelMB_Auxiliar.grid(row=0, column=0)
# matriz Resultante
Label(frameMatrizR, text="Matriz Resultante, en construccion", font=("arial italic", 10)).grid(row=0, column=0)

# botones matriz A---------------------------------------------------------------------
Button(frameOperacionesMatrizA, text="Rotacion Horizontal", command=rotarHorizontalA).grid(row=0, column=0)
Button(frameOperacionesMatrizA, text="Rotacion Vertical", command=rotarVerticalA).grid(row=0, column=1)
Button(frameOperacionesMatrizA, text="Transpuesta", command=transpuestaA).grid(row=1, column=0)
Button(frameOperacionesMatrizA, text="Limpiar Zona", command=limpiarZonaA).grid(row=1, column=1)
Button(frameOperacionesMatrizA, text="Agregar Linea Horizontal", command=addLineaHorizontalA).grid(row=2, column=0)
Button(frameOperacionesMatrizA, text="Agregar Linea Vertical", command=addLineaVerticalA).grid(row=2, column=1)
Button(frameOperacionesMatrizA, text="Agregar Rectangulo", command=addRectanguloA).grid(row=3, column=0)
Button(frameOperacionesMatrizA, text="Agregar Triangulo Rectangulo", command=addTrianguloA).grid(row=3, column=1)
# datos para las operaciones
Label(frameOperacionesMatrizA, text="Fila Inicio").grid(row=4, column=0)
entry_filaInicioA = Entry(frameOperacionesMatrizA)
entry_filaInicioA.grid(row=4, column=1)

Label(frameOperacionesMatrizA, text="Columna Inicio").grid(row=5, column=0)
entry_columnaInicioA = Entry(frameOperacionesMatrizA)
entry_columnaInicioA.grid(row=5, column=1)

Label(frameOperacionesMatrizA, text="Fila Fin").grid(row=6, column=0)
entry_filaFinA = Entry(frameOperacionesMatrizA)
entry_filaFinA.grid(row=6, column=1)

Label(frameOperacionesMatrizA, text="Columna Fin").grid(row=7, column=0)
entry_columnaFinA = Entry(frameOperacionesMatrizA)
entry_columnaFinA.grid(row=7, column=1)

Label(frameOperacionesMatrizA, text="Alto/Longitud de fila").grid(row=8, column=0)
entry_altoLongA = Entry(frameOperacionesMatrizA)
entry_altoLongA.grid(row=8, column=1)

Label(frameOperacionesMatrizA, text="Ancho").grid(row=9, column=0)
entry_anchoA = Entry(frameOperacionesMatrizA)
entry_anchoA.grid(row=9, column=1)

# botones matriz B---------------------------------------------------------------------
Button(frameOperacionesMatrizB, text="Rotacion Horizontal", command=rotarHorizontalB).grid(row=0, column=0)
Button(frameOperacionesMatrizB, text="Rotacion Vertical", command=rotarVerticalB).grid(row=0, column=1)
Button(frameOperacionesMatrizB, text="Transpuesta", command=transpuestaB).grid(row=1, column=0)
Button(frameOperacionesMatrizB, text="Limpiar Zona", command=limpiarZonaB).grid(row=1, column=1)
Button(frameOperacionesMatrizB, text="Agregar Linea Horizontal", command=addLineaHorizontalB).grid(row=2, column=0)
Button(frameOperacionesMatrizB, text="Agregar Linea Vertical", command=addLineaVerticalB).grid(row=2, column=1)
Button(frameOperacionesMatrizB, text="Agregar Rectangulo", command=addRectanguloB).grid(row=3, column=0)
Button(frameOperacionesMatrizB, text="Agregar Triangulo Rectangulo", command=addTrianguloB).grid(row=3, column=1)

# datos para las operaciones
Label(frameOperacionesMatrizB, text="Fila Inicio").grid(row=4, column=0)
entry_filaInicioB = Entry(frameOperacionesMatrizB)
entry_filaInicioB.grid(row=4, column=1)

Label(frameOperacionesMatrizB, text="Columna Inicio").grid(row=5, column=0)
entry_columnaInicioB = Entry(frameOperacionesMatrizB)
entry_columnaInicioB.grid(row=5, column=1)

Label(frameOperacionesMatrizB, text="Fila Fin").grid(row=6, column=0)
entry_filaFinB = Entry(frameOperacionesMatrizB)
entry_filaFinB.grid(row=6, column=1)

Label(frameOperacionesMatrizB, text="Columna Fin").grid(row=7, column=0)
entry_columnaFinB = Entry(frameOperacionesMatrizB)
entry_columnaFinB.grid(row=7, column=1)

Label(frameOperacionesMatrizB, text="Alto/Longitud de fila").grid(row=8, column=0)
entry_altoLongB = Entry(frameOperacionesMatrizB)
entry_altoLongB.grid(row=8, column=1)

Label(frameOperacionesMatrizB, text="Ancho").grid(row=9, column=0)
entry_anchoB = Entry(frameOperacionesMatrizB)
entry_anchoB.grid(row=9, column=1)

# botones operaciones entre matrices -------------------------------------------------------------
Button(frameOperaciones, text="Union A,B", command=unionAB).pack()
Button(frameOperaciones, text="Interseccion A,B", command=interseccionAB).pack()
Button(frameOperaciones, text="Diferencia A,B", command=diferenciaAB).pack()
Button(frameOperaciones, text="Diferencia Simetrica A,B", command=diferenciaSimetricaAB).pack()

# botones operaciones matriz resultante
Button(frameOpMR, text="Sustituir en A", command=sustituirA).pack()
Button(frameOpMR, text="Sustituir en B", command=sustituirB).pack()

# Label signo igual y signo de operacion
Label(frameOpIgual, text="=", font=("arial italic", 18)).grid(row=0, column=0)
label_Signo = Label(frameSignoOperaciones, text="+", font=("arial italic", 18)).grid(row=0, column=0)

ws.mainloop()
