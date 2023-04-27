import sys

import pymysql.cursors


class Conexion:
    _DATABASE = 'seguridad'
    _USERNAME = 'pa'
    _PASSWORD = '1234'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None

    @classmethod
    def getConnection(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pymysql.connect(user = cls._USERNAME,
                                                password= cls._PASSWORD,
                                                host=cls._HOST,
                                                database=cls._DATABASE,
                                                cursorclass=pymysql.cursors.DictCursor)
                print(f'Conexión exitosa {cls._conexion}')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió una excepcion {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.getConnection().cursor()
                print(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió un error {e}')
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    Conexion.getConnection()
    Conexion.getCursor()