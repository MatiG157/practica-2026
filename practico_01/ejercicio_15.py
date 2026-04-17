"""Higher Order Functions, Decoradores, Memoized

Python permite funciones de orden superior, es decir, funciones que toman
otras funciones como parámetros. Esto posibilita una serie de patrones que
en otros lenguajes son difíciles de implementar y hace sencilla la
implementación de patrones como el decorador.


Caso de uso 1: Medir el tiempo de las funciones

En Python existe la función perf_counter del módulo time de la biblioteca
estandar que permite medir el tiempo con cierta precisión entre invocaciones.

Para poder utilizar un ejemplo real, se utilizará una función que calcula
y cuenta las permutaciones (una operación costosa computacionalmente).
"""

from itertools import permutations
from time import perf_counter
from typing import Callable, Sequence, Tuple


# NO MODIFICAR - INICIO
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


n = 11
limite = 10
lista = list(range(n))

start = perf_counter()
result = calcular_posibilidades(lista, limite)
elapsed = perf_counter() - start

print(f"Tiempo: {elapsed:2.2f} segundos - Enfoque procedural")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


from functools import partial, wraps


def medir_tiempo(func: Callable[[], int]) -> Tuple[int, float]:
    """Toma una función y devuelve una dupla conteniendo en su primer elemento
    el resultado de la función y en su segundo elemento el tiempo de ejecución.

    Restricción: La función no debe tomar parámetros y por lo tanto se
    recomienda usar partial.
    """
    start = perf_counter() # Iniciar el contador de tiempo
    result = func() # Ejecutar la función pasada como argumento
    elapsed = perf_counter() - start # Calcular el tiempo transcurrido
    return result, elapsed # Devolver el resultado y el tiempo de ejecución como una tupla


# NO MODIFICAR - INICIO
result, elapsed = medir_tiempo(partial(calcular_posibilidades, lista, limite))
print(f"Tiempo: {elapsed:2.2f} segundos - Usando Partial")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


def medir_tiempo(func: Callable[[Sequence[int], int], int]) -> Callable[[Sequence[int], int], Tuple[int, float]]:
    """Re-Escribir utilizando closures de forma tal que la función no requiera
    partial. En este caso se debe devolver una función que devuelva la tupla y
    tome una cantidad arbitraria de parámetros.
    """
    @wraps(func) #Wraps es un decorador que se utiliza para preservar 
    #la información de la función original (como su nombre, docstring, etc.) 
    #cuando se envuelve con otro decorador. Esto es útil para mantener la claridad y 
    # la trazabilidad del código, especialmente cuando se utilizan múltiples decoradores.
    def wrapper(*args, **kwargs):
        start = perf_counter() # Iniciar el contador de tiempo
        result = func(*args, **kwargs) # Ejecutar la función pasada como argumento
        elapsed = perf_counter() - start # Calcular el tiempo transcurrido
        return result, elapsed # Devolver el resultado y el tiempo de ejecución como una tupla

    return wrapper # Devolver la función wrapper que envuelve la función original


# NO MODIFICAR - INICIO
calcular_posibilidades_nueva = medir_tiempo(calcular_posibilidades)
result, elapsed = calcular_posibilidades_nueva(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""La función anterior cumple con las condiciones necesarias para ser utilizada
como decorador en Python. Utilizar la sintaxis especial de decoradores (el @)
y re-definir la función calcular_posibilidades con esta nueva sintaxis.

Referencia: https://docs.python.org/3/glossary.html#term-decorator

Este es un ejemplo y no hay que escribir código.
"""


# NO MODIFICAR - INICIO
@medir_tiempo
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Decorador con sintaxis especial")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""Un caso real de este patrón es guardar en una memoria cache auxiliar
resultados de funciones que son muy costosas computacionalmente. A este
patrón se lo suele denominar memoized
"""


def memoized(func):
    """Escribir una función memoized y utilizarla como decorador junto con medir_
    tiempo para la función calcular posibilidades. Prestar atención a los tiempo
    de ejecución
    """
    cache = {}

    def normalizar(valor):
        if isinstance(valor, list):
            return tuple(normalizar(v) for v in valor)
        if isinstance(valor, tuple):
            return tuple(normalizar(v) for v in valor)
        if isinstance(valor, dict):
            return tuple(sorted((k, normalizar(v)) for k, v in valor.items()))
        if isinstance(valor, set):
            return tuple(sorted(normalizar(v) for v in valor))
        return valor

    @wraps(func)
    def wrapper(*args, **kwargs):
        key_args = tuple(normalizar(arg) for arg in args)
        key_kwargs = tuple(sorted((k, normalizar(v)) for k, v in kwargs.items()))
        key = (key_args, key_kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoized
def _calcular_posibilidades_recursiva_impl(lista: Tuple[int, ...], limite: int) -> int:
    if limite <= 0:
        return 0
    return _calcular_posibilidades_recursiva_impl(lista, limite - 1) + sum(
        1 for _ in permutations(lista, limite - 1)
    )

# calcular_posibilidades = medir_tiempo(memoized(calcular_posibilidades))
#Aca al llamar:
#1ro medir_tiempo se ejecuta y devuelve una función wrapper que espera los argumentos de 
# calcular_posibilidades.
#2do memoized se ejecuta y devuelve otra función wrapper que envuelve la función original
#3ro calcular_posibilidades se redefine como la función wrapper devuelta por memoized, 
# que a su vez envuelve la función wrapper devuelta por medir_tiempo.
@medir_tiempo
@memoized
def calcular_posibilidades(lista: Sequence[int], limite: int) -> int:
    count = 0
    for i in range(limite):
        for _ in permutations(lista, i):
            count += 1
    return count


# NO MODIFICAR - INICIO
print()

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.2f} segundos - Con Memoized - 1ra ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 2da ejecución")
assert result == 28671512

result, elapsed = calcular_posibilidades(lista, limite)
print(f"Tiempo: {elapsed:2.8f} segundos - Con Memoized - 3ra ejecución")
assert result == 28671512
# NO MODIFICAR - FIN


###############################################################################


"""CHALLENGE OPCIONAL: Esta es otra ocasión donde las funciones recursivas
tienen ventajas adicionales  ya que al utilizar el patrón memoized, las
funciones recursivas permiten ejecuciones más rápidas para las llamadas
sucesivas.
"""


@medir_tiempo
@memoized
def calcular_posibilidades_recursiva(lista: Sequence[int], limite: int) -> int:
    """Re-Escribir de manera recursiva"""
    return _calcular_posibilidades_recursiva_impl(tuple(lista), limite)


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    print()

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(f"Tiempo: {elapsed:2.2f} segundos - Recursiva Memoized - 1ra Ejecución")
    assert result == 28671512

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - 2da Ejecución")
    assert result == 28671512

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 1")
    assert result == 68588312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 1)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 1")
    assert result == 68588312

    print()

    result, elapsed = calcular_posibilidades(lista, limite + 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro + 2")
    assert result == 108505112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 2)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro + 2")
    assert result == 108505112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 1)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 1")
    assert result == 8713112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 1)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 1")
    assert result == 8713112

    print()

    result, elapsed = calcular_posibilidades(lista, limite - 2)
    print(f"Tiempo: {elapsed:2.2f} segundos - Bucles Memoized - Parametro - 2")
    assert result == 2060312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 2)
    print(f"Tiempo: {elapsed:2.8f} segundos - Recursiva Memoized - Parametro - 2")
    assert result == 2060312
# NO MODIFICAR - FIN
