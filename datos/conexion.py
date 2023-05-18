import sys
from pymysqlpool.pool import Pool
import pymysql.cursors


class Conexion:
    _DATABASE = 'seguridad'
    _USERNAME = 'pa'
    _PASSWORD = '1234'
    _HOST = 'localhost'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    _conexion = None
    _cursor = None

    @classmethod
    def getConnectionPool(cls):
        if cls._pool is None:
            try:
                cls._pool = Pool(host=cls._HOST,
                                                       user=cls._USERNAME,
                                                       database=cls._DATABASE,
                                                       password=cls._PASSWORD)
                cls._pool.init()
                print(f'Conexión exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                print(f'Error al obtener pool')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def getConnectionFromPool(cls):
        conexion = cls.getConnectionPool().get_conn()
        print(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.getConnectionPool().release(conexion)
        print(f'Regresamos la conexion al pool : {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.getConnectionPool().destroy()

    @classmethod
    def getConnection(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pymysql.connect(user=cls._USERNAME,
                                                password=cls._PASSWORD,
                                                host=cls._HOST,
                                                database=cls._DATABASE,
                                                cursorclass=pymysql.cursors.SSDictCursor)
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
            print('Abriendo cursor')
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
    conexion1 = Conexion.getConnectionFromPool()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.getConnectionFromPool()
