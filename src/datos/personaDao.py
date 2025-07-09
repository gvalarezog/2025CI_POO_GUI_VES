from src.datos.conexion import Conexion
from src.dominio.persona import Persona


class PersonaDao:
    _ERROR = -1
    _INSERT = ("INSERT INTO Persona (nombre, apellido, cedula,sexo, email) "
               "values (?, ?, ?, ?, ?)")
    _SELECT = ("select nombre, apellido, cedula, sexo, email from Persona "
               "where cedula = ?")
    _UPDATE = ("update persona set nombre=?, apellido=?, cedula=?, "
               "sexo=?, email=? where cedula=?")
    _DELETE = "DELETE FROM Persona WHERE cedula=?"

    @classmethod
    def insertar_persona(cls, persona):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula,
                         persona.sexo, persona.email,)
                retorno = cursor.execute(cls._INSERT, datos)
                return retorno.rowcount
        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_persona(cls, cedula):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                retorno = cursor.execute(cls._SELECT, datos).fetchone()
                if retorno[3] == 'H':
                    sexo = 'Hombre'
                else:
                    sexo = 'Mujer'
                persona = Persona(nombre=retorno[0],
                                  apellido=retorno[1],
                                  cedula=retorno[2],
                                  sexo=sexo,
                                  email=retorno[4])
                return persona
        except Exception as e:
            print(e)
            cursor.rollback()
            return None


    @classmethod
    def actualizar_persona(cls, persona):
        try:
            # cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula,
                         persona.sexo, persona.email, persona.cedula,)
                retorno = cursor.execute(cls._UPDATE, datos)
                return retorno.rowcount
        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR

if __name__ == '__main__':
    p1 = Persona('Luis15', 'Paz', '0123456789', 'M', 'lpaz@mail.com')
    persona = PersonaDao.actualizar_persona(p1)
    print(persona)
