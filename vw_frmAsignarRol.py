from PyQt6 import QtWidgets

from datos import DT_UsuarioRol
from datos.dt_rol import DT_Rol
from datos.DT_V_UsuarioRol import DT_V_UsuarioRol
from datos.dt_usuario import DT_Usuario
from datos.DT_UsuarioRol import DT_UsuarioRol
from entidades.usuario_rol import Usuario_Rol
from vistas import frmAsignarRol
class vw_frmAsignarRolW(QtWidgets.QMainWindow, frmAsignarRol.Ui_frmAsignarRol):
    def __init__(self, parent=None):
        super(vw_frmAsignarRolW,self).__init__(parent)
        self.dtr = DT_UsuarioRol
        self.setupUi(self)
        self.llenarComboRol()
        self.llenarComboUsuario()
        self.listarRolesUsuario()
        self.cbxRol.activated.connect(self.handleActivated)
        self.btnAsignarRol.clicked.connect(self.asignarRol)

    def llenarComboUsuario(self):
        users = DT_Usuario.listarUsuario()
        try:
            for u in users:
                self.cbxUsuario.addItem(u.nombre + ' ' + u.apellido, u.idusuario)
        except Exception as e:
            print(f'Ocurrió una excepcion al recuperar usuarios {e}')

    def llenarComboRol(self):
        roles = DT_Rol.listarRol()
        try:
            for row in roles:
                self.cbxRol.addItem(row.descripcion,row.idrol);
        except Exception as e:
            print(f'Ocurrió una excepción {e}')

    def asignarRol(self,index):
        Usuario_Rol.idUsuario = self.cbxRol.itemData(index)
        Usuario_Rol.idRol = self.cbxRol.itemData(index)

        try:
            self.dtr.DT_Rol.asignarRol(Usuario_Rol)
        except Exception as e:
            print(f'Ocurrió una excepcion al guardar: {e}')

    def listarRolesUsuario(self):
        usuario_roles = DT_V_UsuarioRol.listarUsuarioRol()
        indexes = len(usuario_roles)
        self.tableWidget.setRowCount(indexes)
        tablerow = 0
        for row in usuario_roles:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.idUsuarioRol)))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.nombre)))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.apellido)))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.nombreusuario)))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row.descripcion))


    def handleActivated(self, index):
        print(self.cbxRol.itemText(index))
        print(self.cbxRol.itemData(index))
