""" Comprehension w Pythonie to specjalne wyrażenia, które pozwalają na tworzenie nowych kolekcji: list, słowników,
zbiorów, generatorów, w sposób bardziej zwięzły i czytelny. Są to bardzo potężne narzędzia, które umożliwiają
szybkie i eleganckie tworzenie nowych kolekcji na podstawie już istniejących"""

"""List Comprehension
Umożliwiają tworzenie list w jednej linii, co poprawia wydajność i czytelność. 
Podążają one za określonym wzorcem, aby przekształcić lub filtrować dane z istniejącego iterowalnego obiektu.

Składnia:
[expression for item in iterable if condition]
expression: wyrażenie, które będzie wstawione do nowej listy.
item: elementy, które są pobierane z iterable (np. lista, zakres, itp.).
condition (opcjonalne): warunek, który sprawdza, czy dany element zostanie dodany do listy.
"""
# Przykład nr 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res)

# Przykład nr 2
res = [num**2 for num in range(1,6)]
print(res)

"""Dictionary comprehension
Jest używane do konstrukcji słowników w zwartej formie, co umożliwia łatwe generowanie par klucz-wartość dynamicznie na podstawie iterowalnego obiektu.

Składnia:
{key_expression: value_expression for item in iterable if condition}

key_expression: Określa klucz słownika.
value_expression: Oblicza wartość.
iterable: Kolekcja źródłowa.
condition (opcjonalnie): Filtruje elementy przed ich dodaniem.
"""

# Przykład nr 1
res = {num: num**3 for num in range(1, 6)}
print(res)

# Przykład nr 2
a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res = {state: capital for state, capital in zip(a, b)}
print(res)


"""Set comprehensions
Jest podobne do list comprehensions ale rezultat w set automatyczne eliminuje zduplikowane wartości 
przy zachowaniu zwięzłej składni.

Składnia:
{expression for item in iterable if condition}

expression: Operacja stosowana do każdego elementu.
iterable: Kolekcja źródłowa.
condition (opcjonalnie): Filtruje elementy przed ich dodaniem.
"""
# Przykład 1
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)

# Przykład 2
res = {num**2 for num in range(1, 6)}
print(res)


"""Generator comprehesions
Skrócone tworzenie generatorów (Generator Comprehensions) tworzy iteratory, które generują wartości leniwie, 
co sprawia, że są one efektywne pamięciowo, ponieważ elementy są obliczane dopiero w momencie ich dostępu.

Składnia:

(expression for item in iterable if condition)

Gdzie:

expression: Operacja stosowana do każdego elementu.
iterable: Kolekcja źródłowa.
condition (opcjonalnie): Filtruje elementy przed ich uwzględnieniem.
"""

# Przykład 1 Ten generator produkuje liczby parzyste od 0 do 9, ale wartości są obliczane dopiero w momencie ich dostępu.
res = (num for num in range(10) if num % 2 == 0)
print(list(res))

# Przykład 2 Generator tworzy wartości kwadratowe na żądanie i zwraca je jako krotkę po dokonaniu konwersji.
res = (num**2 for num in range(1, 6))
print(tuple(res))


