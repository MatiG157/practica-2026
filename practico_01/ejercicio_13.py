"""Clousures, Generadores, Generadores Delegados

Esta guia muestra uno de los patrones avanzados de programación para evitar
el uso de variables globales. El método descripto se llama closure y consiste
en vincular una función con datos que persistan luego de la ejecución, sin
recurrir a variables globales. Esto se hace mediante la declaración de una
función dentro de otra y permite comportamiento que sería imposible lograr de
otra manera.
"""


from typing import Iterator, Callable


def generar_pares_clousure(initial: int = 0) -> Callable[[], int]: #Devuelve otra función
    """Toma un número inicial y devuelve una función que cada vez que es
    invocada devuelve el número par siguiente al devuelto la última vez que
    fue invocada.

    Restricciones:
        - Usar closures
        - Usar el modificador nonlocal
    """
    numero_actual = initial

    def siguiente_par() -> int:#Tiene el numero actual aunque generar_pares_clousure 
        #aya terminado su ejecución, es decir, 
        # el valor de numero_actual persiste entre las llamadas a siguiente_par
        
        nonlocal numero_actual #Asi indico que si modifico numero_actual, 
        #quiero modificar la variable del scope de generar_pares_clousure 
        # y no una nueva variable local a siguiente_par
        resultado = numero_actual
        numero_actual += 2
        return resultado

    return siguiente_par


# NO MODIFICAR - INICIO
generador_pares = generar_pares_clousure(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4
# NO MODIFICAR - FIN


###############################################################################


"""Este tipo de comportamiento es conocido com semi-corutina, las semi-corutinas
en Python son llamadas funciones generadoras y se caracterizan por utilizar el
yield en lugar del return.
"""


def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    """Re-Escribir utilizando Generadores
    Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators
    """
    numero_actual = initial
    while True:
        yield numero_actual #El yield es similar al return, 
        # pero en lugar de finalizar la función, 
        # permite que la función se suspenda y pueda reanudarse posteriormente,
        # manteniendo su estado entre llamadas.
        numero_actual += 2


# NO MODIFICAR - INICIO
generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_generator_send(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando send para saltear numeros"""
    numero_actual = initial
    while True:
        received = yield numero_actual
        if received is not None:
            numero_actual = received
        numero_actual += 2


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_generator_send()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
    assert generador_pares.send(10) == 10
    assert next(generador_pares) == 12
    assert next(generador_pares) == 14
    assert next(generador_pares) == 16
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_delegados(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando Generadores delegados (yield from)"""
    yield from generar_pares_generator(initial)
    # El yield from delega la generación de valores a otro generador,
    # en este caso generar_pares_generator.
    
    # Esto permite que generar_pares_delegados produzca los mismos valores que 
    # de generar_pares_generator sin tener que escribir explícitamente el código de generación de pares.
    # Es una forma de simplificar el código y 
    # mejorar la legibilidad al delegar la responsabilidad de generar 
    # los valores a otro generador. 


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
# NO MODIFICAR - FIN
