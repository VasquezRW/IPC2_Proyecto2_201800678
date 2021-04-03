import subprocess
import xml.etree.ElementTree as ET
from graphviz import Digraph


def escribirArchivoXML(datos, ruta):
    try:
        elementoMatrices = ET.Element("matrices")
        matrizz = datos.head
        for i in range(0, datos.size):
            filaa = matrizz.matriz.head
            elementoMatriz = ET.SubElement(elementoMatrices, "matriz", nombre=matrizz.nombre,
                                           n=str(matrizz.matriz.size+1), m=str(matrizz.m), g=str(matrizz.matriz.size+1))
            i = 1
            while filaa is not None:
                dato = filaa.fila.head
                while dato is not None:
                    ET.SubElement(elementoMatriz, "dato", x=str(i), y=str(dato.y)).text = str(dato.numero)
                    dato = dato.next
                filaa = filaa.next
                i += 1
            filaa = matrizz.matriz.head
            while filaa is not None:
                ET.SubElement(elementoMatriz, "frecuencia", g=str(filaa.fila.x)).text = str(filaa.fila.frecuencia)
                filaa = filaa.next
            matrizz = matrizz.next

        arbol = ET.ElementTree(elementoMatrices)
        ET.indent(arbol, space=" ", level=0)

        arbol.write(ruta, encoding='UTF-8', xml_declaration=True)

        subprocess.Popen([ruta], shell=True)
    except:
        print("algo ocurrio")


def generarGrafica(datos, nombreMatriz):
    try:
        matrizz = datos.head
        for i in range(0, datos.size):
            if matrizz.nombre is nombreMatriz:
                dot = Digraph(comment='The Round Table')
                dot.node('Matrices', 'matrices')
                dot.node('Nombre', str(matrizz.nombre))
                dot.node('n', 'n= '+str(matrizz.n))
                dot.node('m', 'm= '+str(matrizz.m))
                dot.edge('Matrices', 'Nombre')
                dot.edge('Nombre', 'n')
                dot.edge('Nombre', 'm')
                filaa = matrizz.matriz.head
                while filaa is not None:
                    dato = filaa.fila.head
                    dot.node('fila'+str(filaa.fila.x), 'fila: '+str(filaa.fila.x))
                    dot.edge('Nombre', 'fila' + str(filaa.fila.x))

                    dot.node('numero_' + str(filaa.fila.x) + "_" + str(dato.y), str(dato.numero))
                    dot.edge('fila' + str(filaa.fila.x), 'numero_' + str(filaa.fila.x) + "_" + str(dato.y))
                    while dato.next is not None:
                        dot.node('numero_' + str(filaa.fila.x) + "_" + str(dato.next.y), str(dato.next.numero))
                        dot.edge('numero_' + str(filaa.fila.x) + "_" + str(dato.y),
                                 'numero_' + str(filaa.fila.x) + "_" + str(dato.next.y))
                        dato = dato.next
                    filaa = filaa.next
            else:
                matrizz = matrizz.next

        dot.render('graficoMatriz.gv', view=True)
        subprocess.Popen(['graficoMatriz.gv'], shell=True)

    except Exception as e:
        print("Algo ocurrio: " + str(e))

