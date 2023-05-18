from PyQt6 import QtWidgets
from vistas import frmAsignarRol
class vw_frmAsignarRolW(QtWidgets.QMainWindow, frmAsignarRol.Ui_frmAsignarRol):
    def __init__(self, parent=None):
        super(vw_frmAsignarRolW,self).__init__(parent)
        self.setupUi(self)
