# przykład 1
# wbudowana funkcja map, mapuje podaną funkcję na dany obiekt iterowalny
# możemy oczywiście zrealizować taki scenariusz na wiele innych sposobów, np. poprzez listy składane (Python comprehensions)

names = ['marek', 'Damian', 'wojtas', 'maczuga333']
print(list(map(lambda x: len(x), names)))

# przykład 2
# lambdę możemy przypisać do zmiennej, dzięki czemu będzie można się do niej odwoływać

mypow = lambda x: x ** 2
print(mypow(2))


# przykład 3
# możemy również wywołać ją w taki sposób
num = 5

print((lambda x: x ** 2)(num))

# przykład 4
# lambdy nie muszą być jednoargumentowe

print((lambda x, y: x + y)(2, 3))

# przykład 5
# w funkcjach anonimowych nie możemy wykorzystać żadnych wyrażeń typu return, pass, assert,
# raise, pętli oraz wskazówek typów i jeżeli to zrobimy to zgłoszony zostanie wyjątek SyntaxError
# lambda x: assert x in list(range(1,11))

# przykład 6
# kolejnym powszechnym przykładem wykorzystania funkcji anonimowej jest połączenie
# jej z wbudowaną funkcją filter(), która pozwala przekazać funkcję filtrującą oraz obiekt
# iterowalny, do którego elementów filtr zostanie przyłożony, a następnie zwraca iterator
data = 'Marek ma 34 lata i 182 cm wzrostu.'.split()

p6 = list(filter(lambda x: x.isdigit(), data))

# tutaj można się chwilę zatrzymać, aby zrozumieć jak ta lambda działa
# w każdym jej wywołaniu przekazywany jest element ze zbioru data do zmiennej x
# jeżeli x.isdigit() to True w przeciwnym wypadku False
# filter mapuje wartości False i True na data i zwraca tylko te gdzie dla danego indeksu jest True
print(p6)

# przykład 7
# również funkcja reduce jest dość często wykorzystywana w połączeniu z lambdami
# obecnie znajduje się w module functools
# https://docs.python.org/3/library/functools.html#functools.reduce
from functools import reduce

# poniższy przykład działa jako konkatenacja odnalezionych cyfr
print(reduce(lambda x, y: x + y, filter(lambda x: x.isdigit(), data)))

# przykład 8
# teraz chcemy te wszystkie liczby zsumować, dorzucamy map i rzutowanie na typ int

print(reduce(lambda x, y: x + y, map(int, filter(lambda x: x.isdigit(), data))))

# wszystko w Pythonie jest obiektem, również mamy operatory w postaci stosownych obiektów funkcji
from operator import add
# efekt ten sam jak powyżej
print(reduce(add, map(int, filter(lambda x: x.isdigit(), data))))

# przykład 9
# patrząc tylko na ten przykład z dwoma elementami, które przetwarza reduce
# można nie zauważyć, że jej wykonanie odbywa się w sposób skumulowany, co oznacza,
# że po każdym jej wykonaniu zwracany jest rezultat, i kolejny krok wykonywany jest
# na tym zwróconym rezultacie i elemencie kolejnym, jeżeli występuje

nums = [1, 1, 1, 1, 1]

print(reduce(add, nums))

# co jest równoważne z
result = 0
for elem in nums:
    result = result + elem
print(result)


# przykład 10
# wykorzystanie lambdy w innej funkcji
# wywołanie samej funkcji zwróci obiekt typu lambda function, ale jeżeli
# zadeklarujemy ją jako wywołanie tej funkcji z określonym argumentem,
# do stworzymy sobie możliwość wywoływania jej w sposób jednolity dla różnych argumentów

def power(n):
  return lambda a : a ** n

square = power(2)
cube = power(3)

print(square(2), cube(5))

# rozpisując to bardziej obrazowo, wywołujemy to co powyżej tak jakbyśmy robili to tak
# jak poniżej
print(power(2)(2), power(3)(5))

# przykład 11
# funkcje anonimowe możemy ogólnie wykorzystać wszędzie tam, gdzie funkcję możemy przekazać jako argument
# np. w funkcji sorted, która służy do sortowania różnych obiektów iterowalnych

data = 'Abracadbra to czary i magia.'

# załóżmy, że chcemy to podzielić na wyrazy i posortować od nadłuższych do najkrótszych

# domyślne sortowanie dla łańcuchów znaków to sortowanie alfabetyczne
print(sorted(data.split()))

# https://docs.python.org/3/library/functions.html#sorted
# sorted przyjmuje jednak argument key, który może być funkcją, której użyjemy do wygenerowania wartości,
# wg. których to sortowanie się wykona
# ten przypadek sortowania po długości nie wymaga co prawda lambdy, ale zostanie również przedstawiony
# domyślny kierunek sortowania to rosnący (widać to dla sortowania alfabetycznego), więc go odwracamy
print(sorted(data.split(), key=lambda x: len(x), reverse=True))

# równie dobrze możemy lambdę pominąć
print(sorted(data.split(), key=len, reverse=True))

# ale gdybyśmy chcieli teraz posortować wyrazy w porządku malejącym, w zależności od tego ile liter 'i' zawierają?
print(sorted(data.split(), key=lambda x: x.count('i'), reverse=True))

# przykład 12
# tu nieco bardziej rozbudowany przykład z implementacją generowania
# listy z elementami ciągu Fibonacciego
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib_series(10))

# jej zrozumienie wymaga nieco dłuższej analizy
# popatrzmy najpierw na tę wewnętrzną lambdę
in_lam = lambda x, _: x + [x[-1] + x[-2]]

# poniższe wywołanie przypisze więc zmiennej x -> [0,1], a zmiennej _ -> 'cokolwiek'
in_lam([0,1], 'cokolwiek')
# czyli do [0, 1] doda sumę dwóch ostatnich elementów w postaci listy
# mamy więc [0, 1] + [1] -> [0, 1, 1] i zostanie to zwrócone

# dodając więc reduce i range(n - 2) osiągamy rekurencję
# wywołanie fib_series(3) ustawia zmienną n=3, ale w range mamy n - 2,
# co daje nam 1, więc mamy range(1), co zwróci tylko 0, a właściwie to
# chodzi o to, że lambda wykona się tylko jeden raz
# n = 3
print(reduce(lambda x, _: x + [x[-1] + x[-2]], range(3 - 2), [0, 1]))

# n = 4
print(reduce(lambda x, _: x + [x[-1] + x[-2]], range(4 - 2), [0, 1]))

# i teraz już wszystko jasne ;-)

import itertools

# count([start, [step]])
import time

# przykład 1
inf_count = itertools.count(2)
print(next(inf_count))
print(next(inf_count))
print(next(inf_count))
# ...

# przykład 2
countdown = 1

for num in itertools.count(countdown, -1):
    if num >= 0:
        print(f"T - {num}")
        time.sleep(1)
    else:
        print('Time is up!')
        break

# cycle(p)

dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']

day_cycle = itertools.cycle(dni_tygodnia)

print(f'Pierwszy dzień tygodnia to {next(day_cycle)}')

print(f'Drugi dzień tygodnia to {next(day_cycle)}')

# accumulate(p, [func])
# wykonuje dodawanie akumulacyjne elementów (domyślnie), ale może przyjąć również
# opcjonalny argument w postaci funkcji
from operator import mul

print(list(itertools.accumulate(range(1, 6))))

print(list(itertools.accumulate(['A', 'B', 'C'])))

print(list(itertools.accumulate([1, 3, 5, 7], mul)))

# batched(p, n)
# tnie podaną sekwencję na sekwencje o długości n

nums = list(range(1, 13))

for batch in itertools.batched(nums, 3):
    print(batch)

for batch in itertools.batched('Abracadabra to czary i magia', 3):
    print(batch)


# startmap(func, seq)
# jest to dość przydatna funkcja, która pozwala na przekazanie innej funkcji do
# wywołania oraz krotek argumentów dla każdego kolejnego wywołania
# argumenty są wypakowywane do wywołania funkcji za pomocą symbolu * (rozpakowanie sekwencji)

# tu można zobaczyc implementację, aby lepiej to zrozumieć
# https://docs.python.org/3/library/itertools.html#itertools.starmap

nums = list(range(1, 13))
# paczki po 3 liczby
paczki = itertools.batched(nums, 3)

def sumuj(*liczby):
    return sum(liczby)

# sumujemy po 3 kolejne liczby
list(itertools.starmap(sumuj, paczki))


# zip_longest(p, q, ..., fillvalue)
# podobna do działania wbudowanej funkcji zip, ale działa dla sekwencji o różnej
# długości

print(list(itertools.zip_longest('ABCDEF', [1,2,3])))
print(list(itertools.zip_longest('ABCDEF', [1,2,3], fillvalue='-')))
print(list(itertools.zip_longest('ABCDEF', [1,2,3], fillvalue=0)))


# product(p, q, ..., [repeat=1])
# zwraca iloczyn kartezjański elementów, tak jakbyśmy dla każdej sekwencji
# tworzyli kolejną zagnieżdżoną pętle for

print(list(itertools.product([1,2,3])))
print(list(itertools.product([1,2,3], repeat=2)))
print(list(itertools.product([1,2,3],[1,2,3])))

print(list(itertools.product('!@#$', repeat=2)))


# permutations(p[,r])
# zwraca permutacje długości r (krotki), w każdym możliwym porządku bez powtarzania elementów

print(list(itertools.permutations('ABC')))
print(list(itertools.permutations('ABC', 2)))

# combinations(p,r)
# zwraca krotki długości r, w porządku posortowanym bez powtórzeń elementów

print(list(itertools.combinations('ABC', 2)))
list(itertools.combinations([3, 4, 5, 6], 2))

# combinations_with_replacement(p, r)
# to co wyżej ale kombinacje z powtórzeniami

print(list(itertools.combinations_with_replacement('ABC', 2)))
list(itertools.combinations_with_replacement([3, 4, 5, 6], 2))