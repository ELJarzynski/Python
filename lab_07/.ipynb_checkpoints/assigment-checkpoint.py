from itertools import cycle, dropwhile, islice, permutations, product, starmap
from functools import reduce
from operator import mul



# Zad 1
text = "BMW Bóg Mnie Wybrał."
vowel  = "aeiouyąę"
as1 = lambda txt: reduce(lambda acc, char: acc + (1 if char in vowel  else 0), txt, 0)

# Zad 2
text_2 = [('Adam', 'Nowak', '13 pkt'), ('Kamil','Kot', '15 pkt'), ('Wojtek', 'Bonk', '8 pkt')]

as2 = sorted(
    [(name, surname, x.split()[0]) for name, surname, x in text_2],
    key=lambda x: int(x[2])
)

# Zad 3
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
as3 = reduce(mul, fib_series(10)[1:])

# Zad 4
as4 = lambda start_day, n: next(islice(
    dropwhile(lambda d: d != start_day, cycle(
        ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
    )), n, None))

# Zad 5
as5 = list(map(lambda x: ''.join(x), permutations('ABCD', 2)))

# Zad 6
nominals = [20, 10, 50, 5]
limits = [4, 3, 2, 2]
combinations = product(*[range(limit + 1) for limit in limits])

as6 = list(filter(lambda x: sum([x[i] * nominals[i] for i in range(len(x))]) == 100, combinations))

# Zad 7
arguments = [(12345.6789, "{:.2f}"), (98765.4321, "{:,.2f}")]
as7 = list(starmap(lambda value, fmt: fmt.format(value), arguments))


# Zad 1
print(as1(text))
# Zad 2
print(as2)
# Zad 3
print(as3)
# Zad 4
print(as4('wtorek', 3))
# Zad 5
print(as5)
# Zad 6
print("Liczba możliwych kombinacji:", len(as6))
# Zad 7
print(as7)




