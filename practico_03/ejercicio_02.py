"""Variables y Métodos de Clase"""


class Articulo:
    """Clase con "nombre" como variable de instancia y un id incremental
    generado automáticamente.

    Restricciones:
        - Utilizar sólamente el constructor (__init__) y un método de
          clase (@classmethod) con una variable de clase
    """

    _last_id = 0 # Variable de clase para llevar el seguimiento del último id asignado

    def __init__(self, nombre: str = None):
        self.nombre = nombre
        Articulo._last_id += 1 # Incrementar la variable de clase para el próximo id
        self.id_ = Articulo._last_id # Asignar el id al artículo actual

    

# NO MODIFICAR - INICIO
art1 = Articulo("manzana")
art2 = Articulo("pera")
art3 = Articulo()
art3.nombre = "tv"

assert art1.nombre == "manzana"
assert art2.nombre == "pera"
assert art3.nombre == "tv"

assert art1.id_ == 1
assert art2.id_ == 2
assert art3.id_ == 3
assert Articulo._last_id == 3
# NO MODIFICAR - FIN
