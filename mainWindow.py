import sys
from PyQt6 import (QtWidgets)
from PyQt6.QtWidgets import QApplication

import vw_frmGuardarUsuario
import vw_lista_usuariosW
from vistas import (vw_home, vw_lista_usuarios)


class MainWindow(QtWidgets.QMainWindow, vw_home.Ui_mw_Seguridad):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #LLAMANDO A LISTAR USUARIOS
        self.actionListar_Usuarios.triggered.connect(self.loadWindow)
        #LLAMANDO A GUARDAR USUARIOS
        self.actionAgregar.triggered.connect(self.guardarUsuariosClick)

    def loadWindow(self):
        self.lista_usuarios = vw_lista_usuariosW.vw_lista_usuarios_Widget()
        self.verticalLayout.addWidget(self.lista_usuarios)

    def guardarUsuariosClick(self):
        self.guardar_usuarios = vw_frmGuardarUsuario.VW_frmGuardarUsuario()
        self.verticalLayout.addWidget(self.guardar_usuarios)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()