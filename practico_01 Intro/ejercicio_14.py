"""Apply, Partial

En múltiples librerías se estila tener una función llamada apply que aplica
una función a todos los elementos de un conjunto de datos, puede ser una
tabla en una base de datos, una columna en un DataFrame o una fila en un
arreglo multidimensional. El problema suele estar en que esta función apply
sólo admite funciones de ún parámetro. Para poder superar esta dificultad,
debe hacerse uso de la función partial.
"""

from functools import partial
from typing import Callable, Iterable


def apply(lista: Iterable[int], func: Callable[[int], bool]) -> Iterable[bool]:
    """Toma una lista y una función que toma un parámetro y devuelve una lista
    con la función aplicada a todos los elementos."""
    return [func(x) for x in lista]

#Ej: Si func fuera es_par(x)
#apply([3, 4, 5], es_par) → [False, True, False]

# NO MODIFICAR - INICIO
def esta_entre_valores(x: int, min_: float, max_: float) -> bool:
    return min_ < x < max_
# NO MODIFICAR - FIN


###############################################################################

#El problema es que la funcion esta_entre_valores toma 3 parámetros, 
# pero apply sólo admite funciones de un parámetro. func(x)

#Entonces debemos usar partial para crear una nueva función 
# que fije los valores de min_ y max_ y deje sólo el parámetro x libre.

lista = [3, 4, 5, 6, 7, 8]
min_ = 4
max_ = 7
nueva_funcion = partial(esta_entre_valores, min_=min_, max_=max_)

#Es como si hubiéramos definido:
#def nueva_funcion(x):
#    return esta_entre_valores(x, min_=4, max_=7)

# NO MODIFICAR - INICIO
lista = [3, 4, 5, 6, 7, 8]
assert [False, False, True, True, False, False] == apply(lista, nueva_funcion)
# NO MODIFICAR - FIN
