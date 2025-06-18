import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from vista.ui_interfaz import Ui_AreaCalculator
from logica import areas

class AreaApp(QMainWindow):
    """Ventana principal de la calculadora de áreas."""

    def __init__(self):
        super().__init__()
        self.ui = Ui_AreaCalculator()
        self.ui.setupUi(self)
        self.conectar_acciones()

    def conectar_acciones(self):
        """Conecta las acciones del menú con las funciones."""
        self.ui.actionCirculo.triggered.connect(self.calcular_circulo)
        self.ui.actionTriangulo.triggered.connect(self.calcular_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.calcular_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.calcular_cuadrado)

    def calcular_circulo(self):
        radio, ok = QInputDialog.getDouble(self, "Radio", "Ingrese el radio:")
        if ok:
            area = areas.area_circulo(radio)
            self.mostrar_resultado("Círculo", area)

    def calcular_triangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Base", "Ingrese la base:")
        if not ok1:
            return
        altura, ok2 = QInputDialog.getDouble(self, "Altura", "Ingrese la altura:")
        if ok2:
            area = areas.area_triangulo(base, altura)
            self.mostrar_resultado("Triángulo", area)

    def calcular_rectangulo(self):
        base, ok1 = QInputDialog.getDouble(self, "Base", "Ingrese la base:")
        if not ok1:
            return
        altura, ok2 = QInputDialog.getDouble(self, "Altura", "Ingrese la altura:")
        if ok2:
            area = areas.area_rectangulo(base, altura)
            self.mostrar_resultado("Rectángulo", area)

    def calcular_cuadrado(self):
        lado, ok = QInputDialog.getDouble(self, "Lado", "Ingrese el lado:")
        if ok:
            area = areas.area_cuadrado(lado)
            self.mostrar_resultado("Cuadrado", area)

    def mostrar_resultado(self, figura, area):
        """Muestra el resultado del cálculo en un cuadro de diálogo."""
        QMessageBox.information(self, "Resultado", f"El área del {figura} es: {area:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = AreaApp()
    ventana.show()
    sys.exit(app.exec_())
