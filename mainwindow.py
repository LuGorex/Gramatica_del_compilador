from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow
from analyzer import analyze
import numpy as np
from colorama import init, Fore, Back, Style
import networkx as nx  
import matplotlib.pyplot as plt  
import rules


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        header = self.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.ui.pushButton.clicked.connect(self.Automata)

    @Slot()
    def Automata(self):
        cadena = self.ui.textEdit.toPlainText().strip() + '$'
        elementos, resultado = analyze(cadena)
        
        if resultado == 'Cadena aceptada!':
            QMessageBox.information(self, 'Mensaje', resultado)
        else:
            QMessageBox.information(self, 'Mensaje', 'Cadena rechazada!')

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(elementos))

        for row, elemento in enumerate(elementos):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(elemento['token']))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(elemento['num'])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(elemento['lexema']))