import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton)
from test_functions import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        init(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())