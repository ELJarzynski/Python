"""Iterator"""
from logging import raiseExceptions

imie = "Reks"
it = iter(imie)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

"""Definicja własnego iteratora"""

class Wspak:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        self.length -= 1
        return self.data[self.length]


przyklad_1 = Wspak("Kamil")
print(next(przyklad_1))
print(next(przyklad_1))
print(next(przyklad_1))
print(next(przyklad_1))
print(next(przyklad_1))

"""collections.abc.Iterable collections.abc.Iterator
Klasa Iterable zapewnia implementację metody __iter__
Klasa Iterator zapewnia implementację metody __iter__ oraz __next__

Przetestowanie czy obiekt jest iterowalny czy nie można wykonać za pomocą wbudowanych metod isinstance() oraz issubclass() 
albo poprzez opakowanie rzutowania obiektu na iterator poprzez wywołanie iter(obiekt) i obsłużenie wyjątku TypeError.
"""

import collections.abc
some_types_to_ceck = [str, int, tuple, list, dict, set]

def check(objects_to_check):
    for obj in objects_to_check:
        print(f'Obiekt {obj} dziedziczy po collections.abc.Iterable: {issubclass(obj, collections.abc.Iterable)}')
        print(f'Obiekt {obj} dziedziczy po collections.abc.Iterator: {issubclass(obj, collections.abc.Iterator)}')
        print(f'Obiekt {obj} posiada metodę __next__: {hasattr(obj, '__next__')}')
        print(f'Obiekt {obj} posiada metodę __iter__: {hasattr(obj, '__iter__')}')
        # rzutowanie na obiekt iteratora
        # obj to nazwa klasy lub funkcji – np. list, tuple, str, iter, range, dict, map, itp.
        # obj() to tworzenie instancji tej klasy/funkcji, czyli obiektu, np. list() tworzy pustą listę, range()
        # bez argumentów da błąd, iter([]) tworzy iterator z pustej listy.

        try:
            obj_iter = iter(obj())
            print(f' Obiekt iteratora dla obiekty {obj} to {obj_iter.__class__.__name__}')
        except TypeError as e:
            print(f'Rzutwanie zakończone błędem',e)
        print('-'*20)

check(some_types_to_ceck)


# wyrażenia generujące
"""Podobnie do wyrażeń listowych (Python comprehension) możliwe jest również zapisanie wyrażenia generatora w analogiczny
 sposób. Używamy do tego celu nawiasów zwykłych. Przykład pniżej."""

# wyrażenia generujące
litery = (litera for litera in "Zdzisław")
print(litery)
print(next(litery))
print(next(litery))
print(next(litery))

# i cała reszta
print(list(litery))
