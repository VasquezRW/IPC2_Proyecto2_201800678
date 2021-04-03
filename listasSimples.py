class nodoDato:
    def __init__(self, dato=None, y=None, next=None):
        self.dato = dato
        self.next = next
        self.y = y

class Fila:

    def __init__(self, no_fila=None):
        self.head = None  
        self.no_fila = no_fila
        self.size = 0

    def insertar(self, dato, y):
        if not self.head:
            self.head = nodoDato(dato=dato, y=y)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nodoDato(dato=dato, y=y)
        self.size += 1

    def comprobarPosicion(self, y):
        current = self.head
        while current.next is not self.head:
            if current.y == y:
                if current.dato is not None:
                    return True
                else:
                    return False
            else:
                current = current.next

    def imprimir(self):
        nod = self.head
        while nod is not None:

            print(nod.dato, end="|")
            nod = nod.next


# --------------------------------------------------------------------------

class nodoFila:
    def __init__(self, fila=None, next=None):
        self.fila = fila
        self.next = next


class Matriz:

    def __init__(self, filas=0, columnas=0):
        self.head = None
        self.size = 0
        self.espaciosLlenos = 0
        self.espaciosVacios = 0
        self.filas = filas
        self.columnas = columnas

    def insertar(self, fila):
        if not self.head:
            self.head = nodoFila(fila=fila)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nodoFila(fila=fila)
        self.size += 1

    def comprobarPosicion(self, x, y):
        nodo = self.head
        while nodo.next is not self.head:
            if nodo.fila.x == x:
                return nodo.fila.comprobarPosicion(y)
            else:
                nodo = nodo.next

    def eliminarfila(self, x):
        previous = self.head
        current = previous.next
        if self.head.fila.x == x:
            self.head = self.head.next
        else:
            while current.fila.x != x:
                previous = current
                current = current.next
            previous.next = current.next
        self.size -= 1

    def imprimir(self):
        nodo = self.head
        while nodo is not None:
            print(f" Fila: {nodo.fila.no_fila} | {nodo.fila.imprimir()}")
            nodo = nodo.next

    def calcularEspaciosLlenos(self):
        nodo = self.head
        no_espacios = 0
        while nodo.next is not self.head:
            if nodo.fila.head is not None:
                no_espacios += nodo.fila.size
        self.espaciosLlenos = no_espacios

    def calcularEspaciosVacios(self):
        espaciosTotales = self.filas * self.columnas
        self.espaciosVacios = espaciosTotales-self.espaciosLlenos
