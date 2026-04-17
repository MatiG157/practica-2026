"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_01 import DB_PATH
from practico_04.ejercicio_06 import reset_tabla
from practico_04.ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    if buscar_persona(id_persona) is False:
        return False

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT MAX(Fecha)
        FROM PersonaPeso
        WHERE IdPersona = ?
        """,
        (id_persona,),
    )
    ultima_fecha = cursor.fetchone()[0] # fetchone() devuelve una tupla con el resultado de la 
    #consulta, y [0] accede al primer elemento de esa tupla,
    # que en este caso es la fecha máxima encontrada para esa persona.
    fecha_nueva = fecha.date().isoformat()

    if ultima_fecha is not None and ultima_fecha > fecha_nueva:
        conexion.close()
        return False

    cursor.execute(
        """
        INSERT INTO PersonaPeso (IdPersona, Fecha, Peso)
        VALUES (?, ?, ?)
        """,
        (id_persona, fecha_nueva, peso),
    )
    nuevo_id = cursor.lastrowid

    conexion.commit()
    conexion.close()

    return nuevo_id


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
