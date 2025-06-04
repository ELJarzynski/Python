"""
    lambda argumenty: wyrażenie
"""
import inspect
from functools import reduce
"""inspect pozwala użyć signature czyli podaje wszystkie atrybuty funkcji"""

lista = [(4, 'a'), (3, 'c'), (2, 'b')]
posortowane = sorted(lista, key=lambda x:x[0])
# inspect.signature(sorted)
# inspect.signature(filter)
# inspect.signature(map)
# inspect.signature(reduce)
""" Funkcja map()
W Pythonie służy do zastosowania funkcji do każdego elementu iterowalnego (np. listy, krotki, zbioru) 
i zwraca iterator z wynikami."""

lista = [1,2,3,4,5,6,7]
kwadraty = list(map(lambda x: x**2, lista))


""" Funkcja filter()
W Pythonie służy do wybrania tylko tych elementów iterowalnych, które spełniają określony warunek 
(funkcja zwraca True), i zwraca iterator z wynikami.
"""

filtered = list(filter(lambda x: x%2 != 0, lista))



""" Funkcja reduce()
W Pythonie (z modułu functools) służy do redukowania całego iterowalnego obiektu do jednej wartości 
poprzez wielokrotne zastosowanie funkcji do kolejnych elementów
"""
reduced = reduce(lambda x,y: x*y, lista)
print(reduced)

""" ----------------------- Lambda_intertools Matma ------------------------------------"""
# Zadanie 1: Filtruj liczby podzielne przez 7, ale nie przez 5
numbers = list(range(1,101))
filtered_1 = list(filter(lambda x: x % 7 == 0 and x % 5 != 0,numbers))
print(filtered_1)

# Zadanie 2: Oblicz kwadraty tylko liczb parzystych
numbers = list(range(1,21))
nums = list(filter(lambda x: x%2 != 1, numbers))
as_2 = list(map(lambda x: x**2, nums))
print(as_2)

# Zadanie 3: Posortuj liczby według liczby dzielników
numbers = [10, 7, 6, 9, 15, 8, 12]
factors = sorted(numbers, key=lambda x: len([i for i in range(1, x + 1) if x % i == 0]))
print(factors)

# Zadanie 4: Usuń z listy liczby, które są wielokrotnością jakiejkolwiek innej liczby w liście
numbers = [2, 3, 4, 6, 9, 12, 15]
as_4 = list(filter(
    lambda x: not any((x != y and x % y == 0) for y in numbers),
    numbers
))

print("4",as_4)

# Zadanie 5: Posortuj liczby według odległości od liczby 50
numbers = [10, 40, 55, 60, 49, 51, 100]
as_5 = sorted(numbers, key=lambda x: abs(x- 50))
print(as_5)

# Zadanie 5: Posortuj liczby według odległości od liczby 50
def kutas(numbers):
    number = 50
    new_list = sorted([(abs(x - number), x) for x in numbers])
    end_list = [x[1] for x in new_list]
    return end_list

print(kutas(numbers))

# Zadanie 6: Suma cyfr każdej liczby
numbers6 = [123, 456, 789, 1010]
kurwa = [str(x) for x in numbers6]
mac = [(x, sum(int(y) for y in x)) for x in kurwa]
maciek = [x[1] for x in mac]
print(maciek)

# map tutaj jest stosowane jak bym napisał fora: for x in numbers6
beka = list(map(lambda x: sum(int(y) for y in str(x)), numbers6))
print(beka)

# Zadanie 7: Filtruj liczby, które są liczbami doskonałymi
numbers = range(2,1001)
perfect = list(
    filter(
            lambda x: x == sum(int(y) for y in str(x)) , numbers)
)
perfect2 = list(
    filter(
            lambda x: x==sum(i for i in range (1, x) if x % i == 0) , numbers)
)

print("Perfct",perfect2)

# Zadanie 7 z listy stringów wybierz te, które mają parzystą długość
lista_zwierz = ["kot", "pies", "lew", "krowa"]
zwierzeta = list(filter(lambda x: len(x) % 2 == 0, lista_zwierz))
print(zwierzeta)

# Zadanie 8 Podnieś każdą liczbę w liście do potęgi jej indeksu
print(list(enumerate(numbers6)))
potega_indeksu = list(map(lambda x:(y:= x[1] ** x[0]), list(enumerate(numbers6))))
print(potega_indeksu)

gloski = ["aaa", "kotaaaa", "król", "ouai"]
brudne = sorted(gloski, key=lambda x: sum(1 for i in x if i in ('a','e','i','o','u', 'ó','y')))
print(brudne)

# Zadanie zliczyć głoski w  texcie przy użyciu reduce
text = "BMW Bóg Mnie Wybrał."
vowel  = "aeiouyąę"

zliczenie = reduce(lambda x, y: x + (1 if y in vowel else 0), text, 0)
print(zliczenie)

# Zadanie 2
points_lista = [('Adam', 'Nowak', '13 pkt'), ('Anna','Górka', '15 pkt'), ('Wojtek', 'Bonk', '8 pkt')]
points = sorted(
    [(name, surname, c.split()[0]) for name, surname, c in points_lista],
    key=lambda x:int(x[2])
)
print(points)