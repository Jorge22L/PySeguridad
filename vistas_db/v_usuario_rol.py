import copy


class V_Usuario_Rol:
    def __init__(self, idUsuarioRol=None, nombre=None, apellido=None,
                 nombreusuario=None, descripcion=None):
        self._idUsuarioRol=idUsuarioRol
        self._nombre=nombre
        self._apellido=apellido
        self._nombreusuario=nombreusuario
        self._descripcion=descripcion

    def __str__(self):
        return f'''
        idUsuarioRol: {self._idUsuarioRol},
        nombre: {self._nombre},
        apellido: {self._apellido},
        nombreusuario: {self._nombreusuario},
        rol: {self._descripcion}
        '''

    def __getitem__(self, item):
        ur = copy.copy(self)
        ur.idUsuarioRol = ur._idUsuarioRolidUsuarioRol
        ur.nombre = ur._nombre
        ur.apellido = ur._apellido
        ur.nombreusuario = ur._nombreusuario
        ur.descripcion = ur._descripcion
        return ur


    #GET
    @property
    def idUsuarioRol(self):
        return self._idUsuarioRol

    #SET
    @idUsuarioRol.setter
    def idUsuarioRol(self, idUsuarioRol):
        self._idUsuarioRol=idUsuarioRol

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def nombreusuario(self):
        return self._nombreusuario

    @nombreusuario.setter
    def nombreusuario(self, nombreusuario):
        self._nombreusuario = nombreusuario

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self,descripcion):
        self._descripcion = descripcion


if __name__ == '__main__':
    pass