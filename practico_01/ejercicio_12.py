"""Tuple, Enumerate, Zip, Args.


Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""


from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción: Resolver utilizando un bucle for.
    """
    resultado = []
    for i in range(len(nombres)):
        resultado.append((nombres[i], precios[i]))
    return tuple(resultado)
    # La función tuple() convierte la lista resultado en una tupla, que es un tipo de dato inmutable.
    # Cada elemento de la lista resultado es una dupla (nombre, precio) que se agrega a la tupla final.


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    """Re-Escribir utilizando enumerate y agregando un nuevo componente.
    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """
    resultado = []
    for i, nombre in enumerate(nombres):
        resultado.append((nombre, precios[i], ids[i]))
    return tuple(resultado)
    # La función enumerate() devuelve un objeto enumerado que contiene pares de índice y valor 
    # para cada elemento de la lista nombres.
    # En cada iteración del bucle, i representa el índice y nombre representa el valor correspondiente 
    # en la lista nombres.
    # Luego, se accede a los elementos correspondientes en las listas precios e ids 
    # utilizando el índice i para crear una tupla con el nombre, precio e id de cada artículo.
    # Finalmente, se convierte la lista resultado en una tupla antes de devolverla.


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    """Re-Escribir utilizando zip.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """
    return tuple(zip(nombres, precios, ids))
    # La función zip() toma las listas nombres, precios e ids y las combina en una sola 
    # secuencia de tuplas, donde cada tupla contiene un elemento de cada lista en la misma posición.
    # Luego, se convierte el resultado de zip() en una tupla antes de devolverla.
    

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:
    """Re-Escribir utilizando zip y una cantidad arbitraria de componentes.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    """
    return tuple(zip(*args))
    # El operador * se utiliza para desempaquetar la lista de argumentos args, 
    # lo que permite que cada lista dentro de args se pase como un argumento separado a la función zip().
    # Esto permite combinar una cantidad arbitraria de listas en una sola secuencia de tuplas, 
    # donde cada tupla contiene un elemento de cada lista en la misma posición.
    # Finalmente, se convierte el resultado de zip() en una tupla antes de devolverla.


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
# NO MODIFICAR - FIN
