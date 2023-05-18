import sys
from PyQt6 import (QtWidgets)
from PyQt6.QtWidgets import QApplication

import vw_frmAsignarRol
import vw_frmGuardarUsuario
import vw_lista_usuariosW
from vistas import (vw_home, frmAsignarRol)


class MainWindow(QtWidgets.QMainWindow, vw_home.Ui_mw_Seguridad):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showWindows = None
        self.lista_usuarios = None
        self.asignar_rol = None
        #LLAMANDO A LISTAR USUARIOS
        self.actionListar_Usuarios.triggered.connect(self.loadWindow)
        #LLAMANDO A GUARDAR USUARIOS
        self.actionAgregar.triggered.connect(self.guardarUsuariosClick)
        self.actionAsignar_Rol.triggered.connect(self.loadRolWindow)

    def loadWindow(self):
        if self.showWindows is None:
            self.lista_usuarios = vw_lista_usuariosW.vw_lista_usuarios_Widget()
            self.verticalLayout.addWidget(self.lista_usuarios)
            self.showWindows = self.lista_usuarios
        else:
            if self.showWindows == self.lista_usuarios:
                return self.lista_usuarios
            else:
                self.showWindows.close()
                self.lista_usuarios = vw_lista_usuariosW.vw_lista_usuarios_Widget()
                self.verticalLayout.addWidget(self.lista_usuarios)
                self.showWindows = self.lista_usuarios


    def loadRolWindow(self):
        if self.showWindows is None:
            self.asignar_rol = vw_frmAsignarRol.vw_frmAsignarRolW()
            self.verticalLayout.addWidget(self.asignar_rol)
            self.showWindows = self.asignar_rol
        else:
            if self.showWindows == self.asignar_rol:
                return self.asignar_rol
            else:
                self.showWindows.close()
                self.asignar_rol = vw_frmAsignarRol.vw_frmAsignarRolW()
                self.verticalLayout.addWidget(self.asignar_rol)
                self.showWindows = self.asignar_rol


    def loadAsignarRol(self):
        self.asignarRol = vw_frmAsignarRol.vw_frmAsignarRolW()
        self.verticalLayout.addWidget(self.asignarRol)

    def guardarUsuariosClick(self):
        self.guardar_usuarios = vw_frmGuardarUsuario.VW_frmGuardarUsuario()
        self.verticalLayout.addWidget(self.guardar_usuarios)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()