import subprocess
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
            <div class="container" style="text-align: center;"> <ul class="list-group">""")
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
    except Exception as e:
        print("Algo ocurrio: " + str(e))


def generarGrafica(matriz, nombre, matOpe):
    try:
        matrizz = matriz
        dot = Digraph(comment='Table', format='png')
        dot.attr('node', shape='box')
        inicio = """<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n"""
        inicio += '<TR>\n'
        inicio += '<TD>' + str(nombre) + '</TD>\n'
        for i in range(0, len(matrizz[0])):
            inicio += '<TD>'
            inicio += str(i+1)
            inicio += '</TD>\n'
        inicio += '</TR>'

        line = 0

        for linea in matriz:
            inicio += '<TR>\n'
            inicio += '<TD>' + str(line+1) + '</TD>\n'
            for dato in linea:
                if dato == "*":
                    inicio += '<TD> * </TD>\n'
                else:
                    inicio += '<TD>   </TD>\n'
            inicio += '</TR>\n'
            line += 1
        inicio += '</TABLE>>\n'

        dot.node("tabla", inicio)
        dot.render('graficoMatriz_'+matOpe, view=False)
        return 'graficoMatriz_'+matOpe+'.png'
        # subprocess.Popen(['graficoMatriz_'+matOpe+'.png'], shell=True)

    except Exception as e:
        print("Algo ocurrio: " + str(e))
