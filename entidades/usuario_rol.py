import copy


class Usuario_Rol:
    def __init__(self, idUsuarioRol=None, idUsuario=None,idRol=None):
        self._idUsuarioRol = idUsuarioRol
        self._idUsuario = idUsuario
        self._idRol = idRol

    def __str__(self):
        return f'''
        idUsuarioRol: {self._idUsuarioRol},
        idUsuario: {self._idUsuario},
        idRol: {self._idRol}

        '''

    def __getitem__(self, item):
        ur = copy.copy(self)
        ur.idUsuarioRol = ur._idUsuarioRol
        ur.idUsuario = ur._idUsuario
        ur.idRol = ur._idRol

        return ur

    # GET
    @property
    def idUsuarioRol(self):
        return self._idUsuarioRol

    # SET
    @idUsuarioRol.setter
    def idUsuarioRol(self, idUsuarioRol):
        self._idUsuarioRol = idUsuarioRol

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self._idUsuario = idUsuario

    @property
    def idRol(self):
        return self._idRol

    @idRol.setter
    def idRol(self, idRol):
        self._idRol = idRol

if __name__ == '__main__':
    rol1 = Usuario_Rol(idUsuario=1, idRol=1)
    print(rol1)