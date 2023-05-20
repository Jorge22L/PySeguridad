import sys

from entidades.rol import Rol
from .conexion import Conexion


class DT_Rol:
    _SELECT = "SELECT * FROM seguridad.rol"
    _INSERT = "INSERT INTO seguridad.usuario_rol (idUsuario, idRol) values (%s,%s)"

    _cursor = None

    @classmethod
    def listarRol(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        roles = []
        for r in resultado:
            rol = Rol(r['idrol'], r['descripcion'])
            roles.append(rol)
        print('roles', roles)
        return roles

    @classmethod
    def asignarRol(cls, usuario_rol):
        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:

                try:

                    print(f'Rol asinado: {usuario_rol.idUsuario, usuario_rol.idRol}')
                    valores = (usuario_rol.idUsuario, usuario_rol.idRol)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Rol insertado: {usuario_rol.idUsuario, usuario_rol.idRol}')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')


    @classmethod
    def actualizarRol(cls, rol):

        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:
                try:
                    valores = (rol.descripcion)
                    cursor.execute(cls._UPDATE, valores)
                    print('Actualizando rol')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Excepción al editar: {e.__traceback__}')

    @classmethod
    def eliminarRol(cls, rol):
        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:
                try:
                    valores = (rol.idrol)
                    print("Eliminando Rol")
                    cursor.execute(cls._DELETE,valores)
                    print("Rol eliminado")
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Ocurrió un error al eliminar el rol: {e}')
                    sys.exit()



if __name__ == '__main__':
    roles = DT_Rol.listarRol()
    for r in roles:
        print(r)
    #INSERTAR REGISTRO
    # usuario1 = Usuario(nombre='miguel', apellido='cervantes', nombreusuario='elQuijote', clave='123', fecha_creacion='2023-03-10')
    # insertar = DT_Usuario.guardarUsuario(usuario1)
    # print(f'Usuario insertado : {insertar}')
