# Form implementation generated from reading ui file 'frmAsignarRol.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frmAsignarRol(object):
    def setupUi(self, frmAsignarRol):
        frmAsignarRol.setObjectName("frmAsignarRol")
        frmAsignarRol.resize(686, 480)
        self.centralwidget = QtWidgets.QWidget(parent=frmAsignarRol)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 471, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.cbxUsuario = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.cbxUsuario.setObjectName("cbxUsuario")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbxUsuario)
        self.cbxRol = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.cbxRol.setObjectName("cbxRol")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cbxRol)
        self.btnAsignarRol = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.btnAsignarRol.setObjectName("btnAsignarRol")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btnAsignarRol)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 169, 471, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(489, 169, 101, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.btnEliminarRolAsignado = QtWidgets.QPushButton(parent=self.formLayoutWidget_2)
        self.btnEliminarRolAsignado.setObjectName("btnEliminarRolAsignado")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btnEliminarRolAsignado)
        frmAsignarRol.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmAsignarRol)
        QtCore.QMetaObject.connectSlotsByName(frmAsignarRol)

    def retranslateUi(self, frmAsignarRol):
        _translate = QtCore.QCoreApplication.translate
        frmAsignarRol.setWindowTitle(_translate("frmAsignarRol", "Asignar rol a usuario"))
        self.label.setText(_translate("frmAsignarRol", "Usuario:"))
        self.label_2.setText(_translate("frmAsignarRol", "Rol:"))
        self.btnAsignarRol.setText(_translate("frmAsignarRol", "Asignar Rol"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmAsignarRol", "Id Usuario Rol"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmAsignarRol", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("frmAsignarRol", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("frmAsignarRol", "Nombre Usuario"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("frmAsignarRol", "Rol"))
        self.btnEliminarRolAsignado.setText(_translate("frmAsignarRol", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmAsignarRol = QtWidgets.QMainWindow()
    ui = Ui_frmAsignarRol()
    ui.setupUi(frmAsignarRol)
    frmAsignarRol.show()
    sys.exit(app.exec())
