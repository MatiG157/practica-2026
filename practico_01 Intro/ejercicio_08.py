"""Any y Sets."""

from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricción: Utilizar bucles anidados.
    """
    for elemento_1 in lista_1:
            for elemento_2 in lista_2:
                if elemento_1 == elemento_2:
                    return True  
    return False




# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN."""

    for elemento_1 in lista_1:
        if elemento_1 in lista_2:
            return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando sin bucles, el operador in y la funcion any.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return any(elemento_1 in lista_2 for elemento_1 in lista_1)
 # La función any devuelve True si al menos uno de los elementos del iterable es verdadero.
 # En este caso, el iterable es una expresión generadora que verifica si cada elemento de 
 # lista 1 está presente en lista 2. 
 # Si al menos uno de los elementos de lista 1 se encuentra en lista 2,
 # any devolverá True; de lo contrario, devolverá False.


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).
    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
    """
    return bool(set(lista_1) & set(lista_2))
    # La función set() convierte las listas en conjuntos,
    # que son colecciones no ordenadas de elementos únicos.
    
    # El operador & entre conjuntos devuelve un nuevo conjunto que contiene
    # solo los elementos que están presentes en ambos conjuntos (la intersección).
    # Si la intersección no está vacía, se evalúa como True; 
    # de lo contrario, se evalúa como False.


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
