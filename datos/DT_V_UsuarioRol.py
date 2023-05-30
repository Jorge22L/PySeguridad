from datos.conexion import Conexion
from vistas_db.v_usuario_rol import V_Usuario_Rol


class DT_V_UsuarioRol:
    _SELECT = "SELECT * FROM seguridad.VW_Usuario_Rol"

    _cursor = None

    @classmethod
    def listarUsuarioRol(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        usuario_rol = []
        for ur in resultado:
            usuario_roles = V_Usuario_Rol(ur['idUsuarioRol'],ur['nombre'], ur['apellido'], ur['nombreusuario'], ur['descripcion'])
            usuario_rol.append(usuario_roles)
        print('Roles por usuario', usuario_rol)
        return usuario_rol



if __name__ == '__main__':
    pass
