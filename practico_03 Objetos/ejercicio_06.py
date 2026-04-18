"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        self.name = name

    # NO MODIFICAR - FIN

 # Los métodos mágicos (magic methods) son métodos especiales que comienzan y 
 # terminan con dos guiones bajos (__). 
 # Estos métodos permiten a las clases personalizar su comportamiento en ciertas situaciones, 
 # como la conversión a string, la comparación de objetos, la suma de objetos, entre otros.
 # Al implementar estos métodos, puedes definir cómo se comporta tu clase en diferentes contextos.
 
    def __repr__(self) -> str:
        return f"Article({self.name!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Article):
            return NotImplemented
        return self.name == other.name


# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    # NO MODIFICAR - FIN

    # Completar
    def __str__(self) -> str:
        return str([article.name for article in self.articles])

    def __repr__(self) -> str:
        return f"ShoppingCart({self.articles!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        this_names = sorted(article.name for article in self.articles)
        other_names = sorted(article.name for article in other.articles)
        return this_names == other_names

    def __add__(self, other: object) -> ShoppingCart:
        if not isinstance(other, ShoppingCart):
            return NotImplemented
        return ShoppingCart(self.articles + other.articles)


# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# NO MODIFICAR - FIN


# En Article, método repr:
# Devuelve un texto reproducible tipo Article('Manzana'), para que eval(repr(objeto)) pueda reconstruirlo.

# En Article, método eq:
# Compara dos artículos por su nombre, no por si son el mismo objeto en memoria.

# En ShoppingCart, método str:
# Devuelve los nombres como lista de strings, por eso queda exactamente "['Manzana', 'Pera']".

# En ShoppingCart, método repr:
# Devuelve algo reproducible tipo ShoppingCart([Article('Manzana'), Article('Pera')]).

# En ShoppingCart, método eq:
# Compara carritos por contenido ignorando el orden (ordena los nombres antes de comparar).

# En ShoppingCart, método add:
# Permite sumar carritos con + y devuelve un carrito nuevo con los artículos combinados.