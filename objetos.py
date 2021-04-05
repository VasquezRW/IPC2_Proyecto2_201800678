
class Reporte:
    def __init__(self, fecha, hora, descripcion, operacion, matrices):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.operacion = operacion
        self.matrices = matrices

    def imprimir(self):
        txtMatrices = ""
        for matriz in self.matrices:
            txtMatrices += matriz + ", "
        print(f"{self.fecha} - {self.hora} - {self.descripcion} - Matriz(Matrices): {txtMatrices}")
