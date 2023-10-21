from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton)


def init(other):
    other.setGeometry(0, 0, 1280, 720)
    other.setWindowTitle('Energy House Shop')
    other.entery_GridLayout = QGridLayout()
    #other.entery_GridLayout.se
    other.registration_Laybel = QLabel('Регистрация', other)
    other.post_Laybel1 = QLabel('Почта', other)

    other.entery_Laybel = QLabel('Вход', other)
    other.post_Laybel2 = QLabel('Почта', other)


    other.entery_GridLayout.addWidget(other.registration_Laybel, 0, 0)
    other.entery_GridLayout.addWidget(other.post_Laybel1, 1, 0)


    other.entery_GridLayout.addWidget(other.entery_Laybel, 0, 1)
    other.entery_GridLayout.addWidget(other.post_Laybel2, 1, 1)


