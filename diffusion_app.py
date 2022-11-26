import sys
from PySide6 import QtCore, QtWidgets, QtGui
import torch
from diffusers import StableDiffusionPipeline

class DiffusionApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Generate Image")
        self.text = QtWidgets.QLabel("PyDiffusion",
                                     alignment=QtCore.Qt.AlignCenter)
        self.image_viewer = QtWidgets.QLabel()
        self.prompt = QtWidgets.QLineEdit()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.image_viewer)
        self.layout.addWidget(self.prompt)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.generate_image)

    @QtCore.Slot()
    def generate_image(self):
        pipe = StableDiffusionPipeline.from_pretrained(
          "CompVis/stable-diffusion-v1-4",
          torch_dtype=torch.float16,
          revision="fp16",
          use_auth_token=False
        ).to("cuda")
        pipe.enable_attention_slicing()

        image = pipe( self.prompt.text() ).images[0]

        image.save("test_image.png")
        image = QtGui.QPixmap("test_image.png")
        self.image_viewer.setPixmap( image )

if __name__=="__main__":
    app = QtWidgets.QApplication([])

    widget = DiffusionApp()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())