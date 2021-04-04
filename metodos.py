import numpy as np
from listasSimples import *


def rotarHorizontalmente(matriz):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    matrizRotada = np.flip(matrizNueva, 0)
    matrizOperada = crearMatrizOrtogonal(matrizRotada, matriz)

    # for fila in matrizRotada:
    #     for elemento in fila:
    #         print(elemento, end=" ")
    #     print("\n")

    return matrizOperada


def rotarVerticalmente(matriz):
    print("en construccion")
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    matrizRotada = []
    for fila in matrizNueva:
        filaRotada = np.flip(fila, 0)
        matrizRotada.append(filaRotada)
    matrizOperada = crearMatrizOrtogonal(matrizRotada, matriz)

    return matrizOperada


def transpuestaMatriz(matriz):
    print("en construccion")


def limpiarZona(matriz, filaInicio, columnaInicio, filaFin, columnaFin):
    print("en construccion")


def agregarLineaHorizontal(matriz, filaInicio, columnaInicio, longitud):
    print("en construccion")


def agregarLineaVertical(matriz, filaInicio, columnaInicio, filaFin, columnaFin):
    print("en construccion")


def agregarRectangulo(matriz, filaInicio, columnaInicio, alto, ancho):
    print("en construccion")


def agregarTrianguloRectangulo(matriz, filaInicio, columnaInicio, alto, ancho):
    print("en construccion")


def crearMatriz(mat, n, m):
    matriz = []
    for i in range(0, n):
        fila = []
        for j in range(0, m):
            if mat.comprobarPosicion(i, j):
                fila.append("*")
            else:
                fila.append("-")
        matriz.append(fila)
    return matriz


def crearMatrizOrtogonal(matrizOperada, matriz):
    matrizOrtogonal = Matriz(nombre=matriz.nombre, filas=matriz.filas, columnas=matriz.columnas)
    no_fila = 0
    for linea in matrizOperada:
        fila = Fila(no_fila)
        no_columna = 0
        for dato in linea:
            if dato == "*":
                fila.insertar(dato, no_columna)
                no_columna += 1
            elif dato == "-":
                no_columna += 1
        matrizOrtogonal.insertar(fila)
        no_fila += 1
    print("Matriz operada ortogonal")
    matrizOrtogonal.imprimir()
    return matrizOrtogonal
