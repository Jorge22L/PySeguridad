import copy


class Usuario:
    def __init__(self, idusuario=None, nombre=None, apellido=None,
                 nombreusuario=None, clave=None, fecha_creacion=None,
                 estado=None):
        self._idusuario=idusuario
        self._nombre=nombre
        self._apellido=apellido
        self._nombreusuario=nombreusuario
        self._clave=clave
        self._fecha_creacion=fecha_creacion
        self._estado=estado

    def __str__(self):
        return f'''
        idusuario: {self._idusuario},
        nombe: {self._nombre},
        apellido: {self._apellido},
        nombreusuario: {self._nombreusuario},
        clave: {self._clave}
        fecha_creacion: {self._fecha_creacion}
        estado: {self._estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idusuario = u._idusuario
        u.nombre = u._nombre
        u.apellido = u._apellido
        u.nombreusuario = u._nombreusuario
        u.fecha_creacion = u._fecha_creacion
        u.clave = u._clave
        u.estado = u._estado
        return u


    #GET
    @property
    def idusuario(self):
        return self._idusuario

    #SET
    @idusuario.setter
    def idusuario(self, idusuario):
        self._idusuario=idusuario

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
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self,clave):
        self._clave = clave

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self,fecha_creacion):
        self._fecha_creacion = fecha_creacion

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self,estado):
        self._estado = estado


if __name__ == '__main__':
    usuario1 = Usuario(nombre='Jorge', apellido='Morales', nombreusuario='jmorales', clave='1234')
    print(usuario1)