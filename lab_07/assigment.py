from functools import reduce
from operator import mul


# Zad 1
tekst = "BMW Bóg Mnie Wybrał."
samogloski = "aeiouyąę"

as1 = lambda txt: reduce(lambda acc, char: acc + (1 if char in samogloski else 0), txt, 0)
print(as1(tekst))

# Zad 2
tekst = [('Adam', 'Nowak', '13 pkt'), ('Anna','Górka', '15 pkt'), ('Wojtek', 'Bonk', '8 pkt')]

as2 = sorted(
    [(imie, nazwisko, x.split()[0]) for imie, nazwisko, x in tekst],
    key=lambda x: int(x[2])
)
print(as2)

# Zad 3
fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
as3 = reduce(mul, fib_series(10)[1:])
print(as3)

# Zad 4
