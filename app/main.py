from app.view import MyWindow
from PySide6.QtWidgets import QApplication
import sys

def main() -> None:
    app = QApplication()
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())