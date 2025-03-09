from collections import namedtuple

# definicja krotki nazwanej
User = namedtuple('User', ['firstname', 'lastname', 'age', 'email'])

# inicjalizacja obiekty krotki nazwanej
u = User('jan', 'Nowak', 34, 'jan.nowak@o2.pl')
print(u)

# jak to z krotkami - są niemutowalne (niezmienne)
# u.firstname = 'Adam'

# dodajmy jeszcze jedną krotkę na potrzeby przykładu z wczytaniem danych z pliku
Order = namedtuple('Order', 'Kraj, Sprzedawca, Data_zamowienia, idZamowienia, Utarg')

"""Krotki nazwane mogą nam się przydać np. przy wczytywaniu danych z plików czy baz danych, gdzie chcemy 
   na pewnym etapie mieć obiekt, którego nie można tak łatwo (celowo lub przypadkiem) zmodyfikować."""

# _make jest odpowiedzialne za utworzenie instancji obiektu krotki z przekazywanych argumentów
# orders = map(Order._make, csv.reader(open("zamowienia.csv", encoding='utf8'), delimiter=';'))
# orders = list(orders)

from lab_02.dataset.dataset import orders


for order in orders:
    print(order.Sprzedawca, order.Utarg, type(order))

orders[1]._asdict()

print(orders[1]._replace(Sprzedawca='Nowak'))

# ale nie podmienia tego w trybie in place
print(orders[1])

# istnieje również możliwość zdefiniowania wartości domyślnej, nieco w ograniczony sposób
Point = namedtuple('Point', ['x','y'], defaults=[0,0])

p = Point()

p._asdict()

p1 = Point(2,2)

# klasyczne krotki nazwane dostarczają również domyślnej implementacji
# metod zaimplementowanych w bazowej klasie tuple
print(p > p1, 0 in p, len(p1) == 2)


"""typing.NamedTuple"""
from typing import NamedTuple


class NewOrder(NamedTuple):
    kraj: str
    sprzedawca: str
    data_zamowienia: str
    id_zamowienia: int
    utarg: float


# dla ułatwiena introspekcji obiektów typu NamedTuple wsprowadzono dodatkowy atrybut
print(NewOrder.__annotations__)

# mimo iż wskazówki typów są określone, to nie otrzymujemy żadnego ostrzeżenia jeżeli
"""przypisujemy wartości innych typów -- mega fajne"""
new_order_1 = NewOrder(*orders[1]._asdict().values())
new_order_2 = NewOrder(*orders[2]._asdict().values())
print(new_order_1)
print(new_order_2)

print(new_order_1 == new_order_2, new_order_1 < new_order_2)

