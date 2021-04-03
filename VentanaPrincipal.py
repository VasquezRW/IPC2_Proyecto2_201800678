from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from lectorXML import *

ws = Tk()
ws.title("Proyecto 2 IPC2")
ws.iconbitmap('usacIcono.ico')
ws.geometry("1000x750")

global matrices


def escoger_archivo():
    ws.filename = filedialog.askopenfilename(title="Seleccione el archivo",
                                             filetypes=(("Archivos XML", "*.xml"),
                                                        ("all files", "*.*")))
    if ws.filename != '':
        matrices = leer_Archivo(ws.filename)
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


def crearMatriz(frame, n, m, matriz):
    for row in range(5):
        for column in range(6):
            if row == 0:
                label = Entry(frame, text="Heading : " + str(column))
                label.config(font=('Arial', 14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                frame.grid_columnconfigure(column, weight=1)
            else:
                label = Entry(frame, text="Row : " + str(row) + " , Column : " + str(column))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                frame.grid_columnconfigure(column, weight=1)


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

# frame de principal
framePrincipal = Frame(ws)
framePrincipal.grid(row=1, column=0)

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

# matriz A
Label(frameMatrizA, text="Matriz A, en construccion", font=("arial italic", 10)).grid(row=0, column=0)
# matriz B
Label(frameMatrizB, text="Matriz B, en construccion", font=("arial italic", 10)).grid(row=0, column=0)
# matriz Resultante
Label(frameMatrizR, text="Matriz Resultante, en construccion", font=("arial italic", 10)).grid(row=0, column=0)

# botones matriz A
Button(frameOperacionesMatrizA, text="Rotacion Horizontal").grid(row=0, column=0)
Button(frameOperacionesMatrizA, text="Rotacion Vertical").grid(row=0, column=1)
Button(frameOperacionesMatrizA, text="Transpuesta").grid(row=1, column=0)
Button(frameOperacionesMatrizA, text="Limpiar Zona").grid(row=1, column=1)
Button(frameOperacionesMatrizA, text="Linea Horizontal").grid(row=2, column=0)
Button(frameOperacionesMatrizA, text="Linea Vertical").grid(row=2, column=1)
Button(frameOperacionesMatrizA, text="Agregar Rectangulo").grid(row=3, column=0)
Button(frameOperacionesMatrizA, text="Agregar Triangulo Rectangulo").grid(row=3, column=1)

# botones matriz B
Button(frameOperacionesMatrizB, text="Rotacion Horizontal").grid(row=0, column=0)
Button(frameOperacionesMatrizB, text="Rotacion Vertical").grid(row=0, column=1)
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