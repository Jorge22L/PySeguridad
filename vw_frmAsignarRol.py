from PyQt6 import QtWidgets
<<<<<<< HEAD

from datos import DT_UsuarioRol
from datos.dt_rol import DT_Rol
from datos.dt_usuario import DT_Usuario
from entidades.usuario_rol import Usuario_Rol
=======
>>>>>>> 25afe3541f679131a853a949f7c215f61ddd2da1
from vistas import frmAsignarRol
class vw_frmAsignarRolW(QtWidgets.QMainWindow, frmAsignarRol.Ui_frmAsignarRol):
    def __init__(self, parent=None):
        super(vw_frmAsignarRolW,self).__init__(parent)
<<<<<<< HEAD
        self.dtr = DT_UsuarioRol
        self.setupUi(self)
        self.llenarComboRol()
        self.llenarComboUsuario()
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

    def handleActivated(self, index):
        print(self.cbxRol.itemText(index))
        print(self.cbxRol.itemData(index))
=======
        self.setupUi(self)
>>>>>>> 25afe3541f679131a853a949f7c215f61ddd2da1
