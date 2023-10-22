import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QComboBox,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
import test_functions as func


class EnteryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('files/ui/entery_window.ui', self)
        self.reg_pushButton_reg.clicked.connect(func.registration(self))
        self.ent_pushButton_ent.clicked.connect(func.entery(self))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        uic.loadUi('files/ui/main_window.ui', self)


def main():
    ex = MainWindow()
    ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EnteryWindow()
    ex.show()
    sys.exit(app.exec())
