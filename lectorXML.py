import re
from xml.dom import minidom
from ListaCircular import *
from listasSimples import *


def leer_Archivo(ruta):
    mydoc = minidom.parse(ruta)
    items = mydoc.getElementsByTagName('matriz')
    matrices = linked_list_circular()
    for elemento in items:
        matrizCorrecta = True
        nombre = elemento.getElementsByTagName('nombre')[0].firstChild.data
        # nombre = elemento.find('nombre')
        #print(nombre)
        filas = int(elemento.getElementsByTagName('filas')[0].firstChild.data)
        #print(filas)
        columnas = int(elemento.getElementsByTagName('columnas')[0].firstChild.data)
        #print(columnas)
        imagen = elemento.getElementsByTagName('imagen')[0].firstChild.data
        imagen = quitar_FilasVacias(imagen)
        #print(imagen)
        if matrices.comprobar_Nombre(nombre):
            matriz = Matriz(nombre=nombre, filas=filas, columnas=columnas)
            no_fila = 0
            lineas = imagen.strip("\n").split("\n")
            print(len(lineas))
            if len(lineas) <= int(filas):
                for linea in lineas:
                    fila = Fila(no_fila)
                    no_columna = 0
                    if len(linea) <= int(columnas):
                        for dato in linea:
                            if dato == "*":
                                fila.insertar(dato, no_columna)
                                no_columna += 1
                            elif dato == "-":
                                no_columna += 1
                        matriz.insertar(fila)
                        no_fila += 1

                    else:
                        print("Linea con columnas fuera de rango")
                        matrizCorrecta = False
                if matrizCorrecta:
                    matriz.calcularEspaciosLlenos()
                    matriz.calcularEspaciosVacios()
                    matrices.insertar(matriz=matriz, n=filas, m=columnas)
                else:
                    print(f"Matriz {nombre} no ingresada verifique los datos")
            else:
                print(f"Matriz {nombre} no ingresada verifique que la cantidad de filas sea correcta")
        else:
            print(f"Matriz {nombre} con nombre repetido")

    return matrices


def quitar_FilasVacias(imagen):
    img = ""
    for linea in imagen.strip("\n").split("\n"):
        linea = quitar_Tabs(linea)
        if linea != '':
            img += linea+"\n"
    return img


def quitar_Tabs(linea):
    line = ''
    for caracter in linea:
        if caracter != "\t":
            line += caracter
    return line