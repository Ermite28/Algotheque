import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,600)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWindow()
    widget.show()

    sys.exit(app.exec_())