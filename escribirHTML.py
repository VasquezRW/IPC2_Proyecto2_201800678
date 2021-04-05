import subprocess
import xml.etree.ElementTree as ET
from graphviz import Digraph


def escribirArchivoHTML(reportes):
    try:
        f = open('tabla.html', 'w')
        inicio = """<html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
            <nav class="navbar navbar-dark bg-dark">
              <a class="navbar-brand">
                <img src="usacIcono.png" width="100" height="100">
              </a>
              <a class="navbar-brand">
              <h2><b> Wilmer Estuardo Vasquez Raxon - 2018000678 </b></h2>
              </a>
            </nav>
            </head>
            <body>"""
        f.write(inicio)
        datos = """
            <br>
            <br>
            \n"""
        f.write(datos)
        f.write("""
            <div class="container" style="text-align: center;"><h4 > <b>Reportes</b> <h4></div>
            <br>
            <div class="container" style="text-align: center;" > <ul class="list-group">""")
        for reporte in reportes:
            f.write("<br>")
            f.write("""<li class="list-group-item">""")
            txtMatrices = ""
            for matriz in reporte.matrices:
                txtMatrices += matriz + ", "
            f.write(reporte.fecha + " - " + reporte.hora + " - " + reporte.descripcion + " - Matriz(Matrices): " + txtMatrices)
            f.write("</li>")
        f.write('\n</ul> </div> \n')
        fin = """</body>
                </html>"""
        f.write(fin)
        f.close()
        subprocess.Popen(['tabla.html'], shell=True)
    except:
        print("algo ocurrio")


def generarGrafica(matriz, nombre, matOpe):
    try:
        matrizz = matriz
        dot = Digraph(comment='Table', format='png')
        dot.attr('node', shape='box')
        # dot.node('Nombre', str(nombre))
        # dot.node('Columna_', "1")
        # dot.edge('Nombre', 'Czolumn_0')
        inicio = """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">"""
        inicio += '<TR>'
        inicio += '<TD>' + str(nombre) + '</TD>'
        for i in range(1, len(matrizz)):
            # dot.node('Column_'+str(i), str(i+1))
            # dot.edge('Column_'+str(i-1), 'Column_'+str(i-1))
            inicio += '<TD>'
            inicio += str(i)
            inicio += '</TD>'
        inicio += '</TR>'

        line = 0

        for linea in matriz:
            inicio += '<TR>'
            inicio += '<TD>' + str(line+1) + '</TD>'
            # dot.node('fila_'+str(line), str(line+1))

            # dot.node('dato_'+str(line)+"_0", dato)
            # dot.edge('fila_'+str(line), 'dato_'+str(line)+"_0")
            for dato in linea:
                # if matriz[line][j] == "-":
                #     dato = " "
                # else:
                #     dato = "*"
                # dot.node('dato_'+str(line)+"_"+str(j), dato)
                # dot.edge('dato_'+str(line-1)+"_"+str(j-1), 'dato_'+str(line)+"_"+str(j))
                if dato == "*":
                    inicio += '<TD> * </TD>'
                else:
                    # dato = "*"
                    inicio += '<TD>   </TD>'
            inicio += '</TR>'
            line += 1
        inicio += '</TABLE>>'

        dot.node("tabla", inicio)
        dot.render('graficoMatriz_'+matOpe, view=True)
        return 'graficoMatriz_'+matOpe+'.png'
        # subprocess.Popen(['graficoMatriz_'+matOpe+'.png'], shell=True)

    except Exception as e:
        print("Algo ocurrio: " + str(e))
