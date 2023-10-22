import sys
import sqlite3
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic
import test

def registration(ex):
    values = (ex.reg_ComboBox_role.currentText(), ex.reg_lineEdit_email.text(), ex.reg_lineEdit_phone.text(),
              ex.reg_lineEdit_password.text(), ex.reg_lineEdit_address.text(), ex.reg_lineEdit_bankcard.text(),
              ex.reg_lineEdit_cvc.text(), ex.reg_lineEdit_date.text())
    value = {'role': ex.reg_ComboBox_role.currentText(), 'email': ex.reg_lineEdit_email.text(), 'phone': ex.reg_lineEdit_phone.text(),
              'password': ex.reg_lineEdit_password.text(), 'address': ex.reg_lineEdit_address.text(), 'bankcard': ex.reg_lineEdit_bankcard.text(),
              'cvc': ex.reg_lineEdit_cvc.text(), 'date': ex.reg_lineEdit_date.text()}
    con = sqlite3.connect("files/csv/PyQT_db.sqlite")
    cur = con.cursor()
    cur.execute("""INSERT INTO account(role, email, phone, password, address, bankcard, cvc, date)
    VALUES (:role, :email, :phone, :password, :address, :bankcard, :cvc, :date)""", value)
    con.commit()
    con.close()

    #test.ex.reg_lineEdit_post

def entery(ex):
    pass












def initUI():
    pass
    #db = QSqlDatabase.addDatabase('QSQLITE')
    #db.setDatabaseName('files/csv/PyQT_db.sqlite')
    #db.open()

    #model = QSqlTableModel(test.ex, db)
    #model.setTable('account')
    #model.select()
