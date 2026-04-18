"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si letra es una vocal o
    no.

    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    pass # Completar
    if letra.lower() == "a":
        return True
    if letra.lower() == "e":
        return True
    if letra.lower() == "i":
        return True
    if letra.lower() == "o":
        return True
    if letra.lower() == "u":
        return True
    return False



# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    """Re-escribir utilizando un sólo IF y el operador IN.
    Referencia: https://docs.python.org/3/reference/expressions.html#membership-test-operations
    """
    pass # Completar

    vocales = "aeiouAEIOU"
    if letra in vocales:
        return True
    return False


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    """Re-escribir utilizando el operador IN pero sin utilizar IF."""
    pass # Completar
    vocales = "aeiouAEIOU"
    return letra in vocales
#De esta forma, 
# el resultado de la expresión "letra in vocales" 
# ya es un booleano, por lo que se puede retornar directamente sin necesidad de un if para evaluar su valor.

# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
