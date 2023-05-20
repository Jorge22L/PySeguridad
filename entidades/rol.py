import copy


class Rol:
    def __init__(self, idrol=None, descripcion=None):
        self._idrol=idrol
        self._descripcion=descripcion

    def __str__(self):
        return f'''
        idrol: {self._idrol},
        descripcion: {self._descripcion},
        
        '''

    def __getitem__(self, item):
        r = copy.copy(self)
        r.idrol = r._idrol
        r.descripcion = r._descripcion

        return r


    #GET
    @property
    def idrol(self):
        return self._idrol

    #SET
    @idrol.setter
    def idrol(self, idrol):
        self._idrol=idrol

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion=descripcion


if __name__ == '__main__':
    rol1 = Rol(descripcion='administrador')
    print(rol1)