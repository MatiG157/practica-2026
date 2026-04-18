"""Slicing."""


def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    # Un string es palíndromo si es igual a sí mismo leído al revés.
    # Con el slice [::-1] obtenemos una copia invertida del string.
    return palabra == palabra[::-1]


# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    # Queremos la mitad "hacia arriba": para longitud impar incluimos
    # el carácter del medio. Usamos división entera de (n + 1) // 2.
    n = len(palabra)
    mitad_superior = (n + 1) // 2
    # El slice [:mitad_superior] devuelve desde el inicio hasta ese índice
    # sin incluirlo.
    return palabra[:mitad_superior]


# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
