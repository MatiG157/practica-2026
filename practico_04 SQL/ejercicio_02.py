"""Base de Datos SQL - Alta"""

import datetime
import sqlite3
from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_01 import DB_PATH


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO Persona (Nombre, FechaNacimiento, DNI, Altura)
        VALUES (?, ?, ?, ?)
        """,
        (nombre, nacimiento.date().isoformat(), dni, altura), # Aca van los valores a insertar
    )

    nuevo_id = cursor.lastrowid # lastrowid es un atributo del cursor que devuelve el ID del último
    #registro insertado en la base de datos.
    conexion.commit()
    conexion.close()

    return nuevo_id


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
