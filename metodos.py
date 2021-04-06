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
    # for i in range(len(matrizAux)):
    #     for j in range(len(matrizAux[0])):
    #         if matrizNueva[j][i] == "*":
    #             matrizAux[i][j] = "*"
    #         else:
    #             matrizAux[i][j] = "-"
    columna = 0
    for linea in matrizNueva:
        for j in range(len(matrizAux)):
            matrizAux[j][columna] = linea[j]
        columna += 1

    matrizDatos = Matriz(nombre=matriz.nombre, filas=matriz.columnas, columnas=matriz.filas)
    matrizOperada = crearMatrizOrtogonal(matrizAux, matrizDatos)

    for fila in matrizAux:
        for elemento in fila:
            print(elemento, end=" ")
        print("\n")

    matrizOperada.imprimir()

    return matrizOperada


def limpiarZona(matriz, filaInicio, columnaInicio, filaFin, columnaFin):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for i in range(filaInicio - 1, filaFin):
        for j in range(columnaInicio - 1, columnaFin):
            matrizNueva[i][j] = "-"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)
    return matrizOperada


def agregarLineaHorizontal(matriz, filaInicio, columnaInicio, longitud):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for j in range((columnaInicio - 1), (columnaInicio + longitud - 1)):
        matrizNueva[filaInicio - 1][j] = "*"
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)

    return matrizOperada


def agregarLineaVertical(matriz, filaInicio, columnaInicio, longitud):
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    for i in range((filaInicio - 1), (filaInicio + longitud - 1)):
        matrizNueva[i][columnaInicio - 1] = "*"
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
    matrizNueva = crearMatriz(matriz, matriz.filas, matriz.columnas)
    k = 1
    for i in range(filaInicio - 1, (filaInicio + alto - 1)):

        for j in range(k):
            for n in range(columnaInicio - 1, columnaInicio + k - 1):
                matrizNueva[i][n] = "*"
        k += 1

    for fila in matrizNueva:
        for elemento in fila:
            print(elemento, end=" ")
        print("\n")

    matrizOperada = crearMatrizOrtogonal(matrizNueva, matriz)
    return matrizOperada


def unionMatrizAB(matrizA, matrizB):
    n = 0
    m = 0
    if matrizA.filas > matrizB.filas:
        n = matrizA.filas
    else:
        n = matrizB.filas

    if matrizA.columnas > matrizB.columnas:
        m = matrizA.columnas
    else:
        m = matrizB.columnas
    matrizNueva = crearMatrizVacia(n, m)

    for i in range(len(matrizNueva)):
        for j in range(len(matrizNueva[0])):
            if matrizA.comprobarPosicion(i, j) or matrizB.comprobarPosicion(i, j):
                matrizNueva[i][j] = "*"
            else:
                matrizNueva[i][j] = "-"
    matrizDatos = Matriz(nombre=matrizB.nombre + "-" + matrizB.nombre, filas=n, columnas=m)
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matrizDatos)
    return matrizOperada


def interseccionMatrizAB(matrizA, matrizB):
    n = 0
    m = 0
    if matrizA.filas > matrizB.filas:
        n = matrizA.filas
    else:
        n = matrizB.filas

    if matrizA.columnas > matrizB.columnas:
        m = matrizA.columnas
    else:
        m = matrizB.columnas
    matrizNueva = crearMatrizVacia(n, m)

    for i in range(len(matrizNueva)):
        for j in range(len(matrizNueva[0])):
            if matrizA.comprobarPosicion(i, j) and matrizB.comprobarPosicion(i, j):
                matrizNueva[i][j] = "*"
            else:
                matrizNueva[i][j] = "-"
    matrizDatos = Matriz(nombre=matrizB.nombre + "-" + matrizB.nombre, filas=n, columnas=m)
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matrizDatos)
    return matrizOperada


def diferenciaMatrizAB(matrizA, matrizB):
    n = 0
    m = 0
    if matrizA.filas > matrizB.filas:
        n = matrizA.filas
    else:
        n = matrizB.filas

    if matrizA.columnas > matrizB.columnas:
        m = matrizA.columnas
    else:
        m = matrizB.columnas
    matrizNueva = crearMatrizVacia(n, m)

    for i in range(len(matrizNueva)):
        for j in range(len(matrizNueva[0])):
            if matrizA.comprobarPosicion(i, j) and not matrizB.comprobarPosicion(i, j):
                matrizNueva[i][j] = "*"

            else:
                matrizNueva[i][j] = "-"
    matrizDatos = Matriz(nombre=matrizB.nombre + "-" + matrizB.nombre, filas=n, columnas=m)
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matrizDatos)
    return matrizOperada


def diferenciaSimetricaMatrizAB(matrizA, matrizB):
    n = 0
    m = 0
    if matrizA.filas > matrizB.filas:
        n = matrizA.filas
    else:
        n = matrizB.filas

    if matrizA.columnas > matrizB.columnas:
        m = matrizA.columnas
    else:
        m = matrizB.columnas
    matrizNueva = crearMatrizVacia(n, m)

    for i in range(len(matrizNueva)):
        for j in range(len(matrizNueva[0])):
            if matrizA.comprobarPosicion(i, j):
                if not matrizB.comprobarPosicion(i, j):
                    matrizNueva[i][j] = "*"
                else:
                    matrizNueva[i][j] = "-"
            elif matrizB.comprobarPosicion(i, j):
                if not matrizA.comprobarPosicion(i, j):
                    matrizNueva[i][j] = "*"
                else:
                    matrizNueva[i][j] = "-"
            else:
                matrizNueva[i][j] = "-"
    matrizDatos = Matriz(nombre=matrizB.nombre + "-" + matrizB.nombre, filas=n, columnas=m)
    matrizOperada = crearMatrizOrtogonal(matrizNueva, matrizDatos)
    return matrizOperada


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
