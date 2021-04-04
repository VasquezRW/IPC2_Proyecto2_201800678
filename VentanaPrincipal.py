from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from lectorXML import *
from metodos import *

ws = Tk()
ws.title("Proyecto 2 IPC2")
ws.iconbitmap('usacIcono.ico')
ws.geometry("1000x750")

matrices = linked_list_circular()
global opciones
opciones = []


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


def rotarHorizontalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    matrizOperada = rotarHorizontalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizB()


def rotarVerticalA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    matrizOperada = rotarVerticalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizA()


def rotarVerticalB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    matrizOperada = rotarVerticalmente(matriz)
    matrices.reemplazar_Matriz(matriz.nombre, matrizOperada)
    cargarMatrizB()


def crearMatriz(frame, matriz):
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


def cargarMatrizA():
    matriz = matrices.obtener_Matriz(clickedA.get())
    labelMA_Auxiliar.destroy()
    global frameMatrizA
    frameMatrizA.destroy()
    frameMatrizA = LabelFrame(frameAreaMA, text='Matriz A')
    frameMatrizA.grid(row=0, column=0)
    crearMatriz(frameMatrizA, matriz)


def cargarMatrizB():
    matriz = matrices.obtener_Matriz(clickedB.get())
    labelMB_Auxiliar.destroy()
    global frameMatrizB
    frameMatrizB.destroy()
    frameMatrizB = LabelFrame(frameAreaMB, text='Matriz B')
    frameMatrizB.grid(row=0, column=0)
    crearMatriz(frameMatrizB, matriz)


menubar = Menu(ws, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
cargarArchivo = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
# file.add_command(label="New")
cargarArchivo.add_command(label="Seleccionar Archivo", command=escoger_archivo)
# file.add_separator()
menubar.add_cascade(label="Cargar Archivo", menu=cargarArchivo)

edit = Menu(menubar, tearoff=0)
# edit.add_command(label="Cut")
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

# botones matriz A
Button(frameOperacionesMatrizA, text="Rotacion Horizontal", command=rotarHorizontalA).grid(row=0, column=0)
Button(frameOperacionesMatrizA, text="Rotacion Vertical", command=rotarVerticalA).grid(row=0, column=1)
Button(frameOperacionesMatrizA, text="Transpuesta").grid(row=1, column=0)
Button(frameOperacionesMatrizA, text="Limpiar Zona").grid(row=1, column=1)
Button(frameOperacionesMatrizA, text="Linea Horizontal").grid(row=2, column=0)
Button(frameOperacionesMatrizA, text="Linea Vertical").grid(row=2, column=1)
Button(frameOperacionesMatrizA, text="Agregar Rectangulo").grid(row=3, column=0)
Button(frameOperacionesMatrizA, text="Agregar Triangulo Rectangulo").grid(row=3, column=1)

# botones matriz B
Button(frameOperacionesMatrizB, text="Rotacion Horizontal", command=rotarHorizontalB).grid(row=0, column=0)
Button(frameOperacionesMatrizB, text="Rotacion Vertical", command=rotarVerticalB).grid(row=0, column=1)
Button(frameOperacionesMatrizB, text="Transpuesta").grid(row=1, column=0)
Button(frameOperacionesMatrizB, text="Limpiar Zona").grid(row=1, column=1)
Button(frameOperacionesMatrizB, text="Linea Horizontal").grid(row=2, column=0)
Button(frameOperacionesMatrizB, text="Linea Vertical").grid(row=2, column=1)
Button(frameOperacionesMatrizB, text="Agregar Rectangulo").grid(row=3, column=0)
Button(frameOperacionesMatrizB, text="Agregar Triangulo Rectangulo").grid(row=3, column=1)

# botones operaciones entre matrices
Button(frameOperaciones, text="Union A,B").pack()
Button(frameOperaciones, text="Interseccion A,B").pack()
Button(frameOperaciones, text="Diferencia A,B").pack()
Button(frameOperaciones, text="Diferencia Simetrica A,B").pack()

# botones operaciones matriz resultante
Button(frameOpMR, text="Sustituir").pack()

# Label signo igual y signo de operacion
Label(frameOpIgual, text="=", font=("arial italic", 18)).grid(row=0, column=0)
label_Signo = Label(frameSignoOperaciones, text="+", font=("arial italic", 18)).grid(row=0, column=0)

ws.mainloop()
