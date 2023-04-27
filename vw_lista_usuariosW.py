import PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from datos.dt_usuario import DT_Usuario
from vistas import vw_lista_usuarios


class vw_lista_usuarios_Widget(QtWidgets.QMainWindow, vw_lista_usuarios.Ui_frmListaUsuarios):
    def __init__(self, parent=None):
        super(vw_lista_usuarios_Widget,self).__init__(parent)
        self.setupUi(self)
        self.listarUsuarios()

    def listarUsuarios(self):
        usuarios = DT_Usuario.listarUsuario()
        indexes = len(usuarios)
        self.tw_usuarios.setRowCount(indexes)
        tablerow = 0
        for row in usuarios:
            self.tw_usuarios.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.idusuario)))
            self.tw_usuarios.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row.nombre))
            self.tw_usuarios.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row.apellido))
            self.tw_usuarios.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row.nombreusuario))
            self.tw_usuarios.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.fecha_creacion)))
            tablerow += 1