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
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    matrizRotada = []
    for fila in matrizNueva:
        filaRotada = np.flip(fila, 0)
        matrizRotada.append(filaRotada)
    matrizOperada = crearMatrizOrtogonal(matrizRotada, matriz)

    return matrizOperada


def transpuestaMatriz(matriz):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    matrizAux = crearMatrizVacia(matriz.columnas, matriz.filas)

    for i in range(len(matrizNueva)):
        for j in range(len(matrizNueva[0])):
            matrizAux[j][i] = matrizNueva[i][j]

    matrizOperada = crearMatrizOrtogonal(matrizAux, matriz)

    return matrizOperada


def limpiarZona(matriz, filaInicio, columnaInicio, filaFin, columnaFin):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for i in range(filaInicio-1, filaFin):
        for j in range(columnaInicio-1, columnaFin):
            matrizNueva[i][j] = "-"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)
    return matrizOperada


def agregarLineaHorizontal(matriz, filaInicio, columnaInicio, longitud):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for j in range((columnaInicio-1), (columnaInicio+longitud-1)):
        matrizNueva[filaInicio-1][j] = "*"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)

    return matrizOperada


def agregarLineaVertical(matriz, filaInicio, columnaInicio, longitud):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for i in range((filaInicio - 1), (filaInicio + longitud - 1)):
        matrizNueva[i][columnaInicio-1] = "*"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)

    return matrizOperada


def agregarRectangulo(matriz, filaInicio, columnaInicio, alto, ancho):
    print("en construccion")
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for i in range(filaInicio - 1, (filaInicio + alto - 1)):
        for j in range(columnaInicio - 1, (columnaInicio + ancho - 1)):
            matrizNueva[i][j] = "*"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)
    return matrizOperada


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


def crearMatrizVacia(n, m):
    matriz = []
    for i in range(0, n):
        fila = []
        for j in range(0, m):
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
