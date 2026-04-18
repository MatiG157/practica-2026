"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

DB_PATH = "practico_04.db"

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conexion = sqlite3.connect(DB_PATH) # Conectamos a la base de datos, si no existe se crea
    cursor = conexion.cursor() # Creamos un cursor para ejecutar comandos SQL

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre CHAR(30),
            FechaNacimiento DATE,
            DNI INTEGER,
            Altura INTEGER
        )
        """
    )

    conexion.commit()
    conexion.close()
    

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    cursor.execute("DROP TABLE IF EXISTS Persona")

    conexion.commit()
    conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
