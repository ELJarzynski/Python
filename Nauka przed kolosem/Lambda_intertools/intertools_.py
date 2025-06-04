import itertools
import operator
from functools import reduce
from itertools import islice, cycle

"""ITERATORY NIESKOŃCZONE"""
""" itertools.count(start=0, step=1)
Tworzy nieskończony iterator, który generuje kolejne liczby zaczynając od start (domyślnie 0) i zwiększając je
o step (domyślnie 1). Działa jak licznik — zwraca start, start + step, start + 2 * step itd. Używa się go często
do numerowania elementów w zip() lub map() bez konieczności tworzenia pełnej listy liczb. Ponieważ jest nieskończony, 
trzeba go ograniczyć ręcznie np. islice(), next() lub break."""

countdown = 10

for num in itertools.count(countdown, -1):
    if num >= 0:
        print(f'T - {num}')
    else:
        print("Time is up!")
        break


""" itertools.cycle(iterable)
tworzy nieskończony iterator, który powtarza elementy podanej sekwencji w kółko. 
Nadaje się np. do powtarzalnych wzorców, takich jak kolory lub nazwy. Trzeba samodzielnie przerwać jego działanie, 
np. pętlą for z ograniczeniem lub islice() bądź next()."""

days_of_week = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
n = 10

for statement in itertools.cycle(days_of_week):
    if n != 0:
        n -= 1
        print(f'Dzień tygodnia {statement}')
    else:
        break

"""itertools.repeat(object, times=None) 
Zwraca iterator powtarzający object. Jeśli times nie zostanie podane, powtarza nieskończoną liczbę razy. 
Przydatne do zapełniania lub łączenia z innymi iteratorami."""

WF = "Nie będę kopał piłki od siatki nogą..."

for statement in itertools.repeat(WF, 10):
    print(statement)


"""ITERATORY SKOŃCZONE"""
"""itertools.accumulate(iterable, func=operator.add) 
Zwraca iterator, który zwraca skumulowane wyniki działania funkcji (domyślnie dodawania) na elementach iterable"""

"""Operatory do accumulate
operator.add(a, b)	    Dodawanie	a + b
operator.sub(a, b)	    Odejmowanie	a - b
operator.mul(a, b)	    Mnożenie	a * b
operator.truediv(a, b)	Dzielenie (float)	a / b
operator.floordiv(a, b)	Dzielenie całkowite	a // b
operator.mod(a, b)	    Reszta z dzielenia	a % b
operator.pow(a, b)	    Potęgowanie	a ** b
operator.neg(a)	        Negacja	-a
operator.abs(a)	        Wartość bezwzględna	abs(a)
"""

print(list(itertools.accumulate(range(1,6), operator.mul)))
print(list(itertools.accumulate(['A', 'B', 'C'])))


"""itertools.batched(iterable, n) 
Dzieli dane z iterable na listy (batch'e) po n elementów. Ostatni batch może być krótszy, jeśli nie starczy elementów. 
Przydaje się do przetwarzania danych w grupach."""

nums = list(range(1, 13))

for batch in itertools.batched(nums, 3):
    print(batch)

for batch in itertools.batched("Abracadabra nie wiem co napisać dalej", 3):
    print(batch)

"""itertools.starmap(func, iterable)
Działa jak map, ale rozpakowuje argumenty z każdego element (czyli krotki) w iterable i przekazuje je do funkcji. Czyli func(*args)
"""
paczki = itertools.batched(nums,2)
print(list(itertools.starmap(operator.mul, paczki)))

"""zip_longest(p, q, ..., fillvalue=None)
Łączy elementy z wielu iterowalnych obiektów jak zip, ale wydłuża wynik do najdłuższego z nich, uzupełniając brakujące wartości fillvalue."""
print(list(itertools.zip_longest('ABCDEF', [1,2,3])))
print(list(itertools.zip_longest('ABCDEF', [1,2,3], fillvalue='-')))
print(list(itertools.zip_longest('ABCDEF', [1,2,3], fillvalue=0)))

"""KOMBINATORYKA"""
"""itertools.product(p, q, ..., repeat=1)
Tworzy kartezjański iloczyn podanych iterowalnych obiektów. Zwraca wszystkie możliwe kombinacje elementów, jak zagnieżdżone pętle for."""
print(list(itertools.product([1,2,3])))
print(list(itertools.product([1,2,3], repeat=2)))
print(list(itertools.product([1,2,3],[1,2,3])))
print(list(itertools.product('!@#$', repeat=2)))

"""itertools.permutations(p[, r])
Zwraca wszystkie możliwe permutacje (czyli różne kolejności) r elementów z p. Jeśli r nie podano, to długość permutacji = długość p."""
print(list(itertools.permutations('ABC')))
print(list(itertools.permutations('ABC', 2)))

"""itertools.combinations(p, r)
Zwraca wszystkie możliwe kombinacje r elementów z p, bez powtórzeń i kolejność nie ma znaczenia."""
print(list(itertools.combinations('ABC', 2)))
list(itertools.combinations([3, 4, 5, 6], 2))

"""itertools.combinations_with_replacement(p, r)
Jak combinations(), ale elementy mogą się powtarzać. Nadaje się np. do zliczania kombinacji z powtórzeniami."""
print(list(itertools.combinations_with_replacement('ABC', 2)))
list(itertools.combinations_with_replacement([3, 4, 5, 6], 2))

print(reduce(lambda x, _: x + [x[-1] + x[-2]], range(10 - 2), [0,1]))

# Zadanie 3
fibonaci = reduce(lambda x, _: x + [x[-1] + x[-2]], range(10-2),[0,1])
print(fibonaci[1:])
print(reduce(operator.mul, fibonaci[1:]))

# Zadanie 5
def jaki_dzien(day, n):
    days_of_week = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

    for statement in days_of_week:
        n -= 1
        if n <= 0:
            break
        print(f'{n} dni po {day} to {statement}')

print(jaki_dzien('wtorek', 3))

oszaleje = lambda start_day, n: next(islice(
    itertools.dropwhile(lambda d: d !=start_day,
                        cycle(['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'])),
    n, None))
print(oszaleje('wtorek',5))

# Zadanie 6
print(list(itertools.permutations('ABCD', 2)))
permutacje_wakacje = list(map(lambda x: ''.join(x), itertools.permutations('ABCD', r=2)))
print(permutacje_wakacje)

# Zadanie 6
