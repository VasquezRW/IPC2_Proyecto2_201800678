from listasSimples import *
import lectorXML


class nodoMatriz:
    def __init__(self, nombre=None, matriz=None, n=0, m=0, next=None):
        self.nombre = nombre
        self.matriz = matriz
        self.n = n
        self.next = next
        self.m = m


class linked_list_circular:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, matriz, nombre, n, m):
        if self.size == 0:
            self.head = nodoMatriz(nombre=nombre, matriz=matriz, n=n, m=m)
            self.head.next = self.head
        else:
            nodo = self.head
            while nodo.next is not self.head:
                nodo = nodo.next
            new_node = nodoMatriz(nombre=nombre, matriz=matriz, n=n, m=m, next=self.head)
            nodo.next = new_node
        self.size += 1

    def comprobar_Nombre(self, nombre):
        nodo = self.head
        # existe = False
        if self.size == 0:
            return True
        else:
            while nodo.next is not self.head:
                if nodo.nombre is nombre:
                    return False
                else:
                    nodo = nodo.next
            return True

    def obtener_Nombre(self, indice):
        nodo = self.head
        # existe = False
        if self.size == 0:
            print("matriz vacia")
            return "vacio"
        else:
            for i in range(1, indice):
                nodo = nodo.next
            return nodo.nombre

    def imprimir(self):
        if self.head is None:
            return
        nodo = self.head
        print(f"nombre: {nodo.nombre} | matriz: {nodo.matriz} | n: {nodo.n} | m: {nodo.m}")
        print(nodo.matriz.imprimir())
        while nodo.next is not self.head:
            nodo = nodo.next
            print(f"nombre: {nodo.nombre} | matriz: {nodo.matriz} | n: {nodo.n} | m: {nodo.m}")
            print(nodo.matriz.imprimir())

    def imprimirNombres(self):
        if self.head is None:
            return
        nodo = self.head
        i = 1
        print(f"{i}: matriz: {nodo.nombre} | n: {nodo.n} | m: {nodo.m}")
        while nodo.next is not self.head:
            nodo = nodo.next
            i += 1
            print(f"{i}: matriz: {nodo.nombre} | n: {nodo.n} | m: {nodo.m}")
