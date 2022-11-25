import sys
from PySide6 import QtCore, QtWidgets, QtGui

class DiffusionApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Generate Image")
        self.text = QtWidgets.QLabel("PyDiffusion",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.generate_image)

    @QtCore.Slot()
    def generate_image(self):
        print("Test button")


if __name__=="__main__":
    app = DiffusionApp()
    app.resize(800, 600)
    app.show()
    sys.exit(app.exec())