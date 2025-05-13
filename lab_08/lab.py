class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# próba rzutowania
try:
    iter(4)
except TypeError as e:
    print(e)

import collections.abc

some_types_to_check = [str, int, tuple, list, dict, set]

def check(objects_to_check):
    for obj in objects_to_check:
        print(f'Obiekt {obj} dziedziczy po collections.abc.Iterable: {issubclass(obj, collections.abc.Iterable)}')
        print(f'Obiekt {obj} dziedziczy po collections.abc.Iterator: {issubclass(obj, collections.abc.Iterator)}')
        print(f'Obiekt {obj} posiada metodę __next__: {hasattr(obj, '__next__')}')
        print(f'Obiekt {obj} posiada metodę __iter__: {hasattr(obj, '__iter__')}')
        # rzutowanie na obiekt iteratora
        try:
            # wywołujemy (nag. call) obiekty zapisane na liście
            obj_iter = iter(obj())
            print(f'Obiekt iteratora dla obiektu {obj} to {obj_iter.__class__.__name__}')
        except TypeError as e:
            print("Rzutowanie zakończone błędem!")
            print(e)
        print('-' * 20)

# testujemy obiekty wg. zaimplementowanej logiki
check(some_types_to_check)

class Vector2d:

    def __init__(self):
        self.values = [0,0]

    def set_values(self, x,y):
        self.values[0] = x
        self.values[1] = y

    def __getitem__(self, idx):
        if idx >= len(self.values):
            raise IndexError
        return self.values[idx]

print(check([Vector2d]))
vec = Vector2d()
vector_iterator = iter(vec)
print(next(vector_iterator))
print(next(vector_iterator))

# przykład implementacji iteratora dla skończonego ciągu liczb Fibonacciego
class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration

        fibonacci_number = self.a
        self.a, self.b = self.b, self.a + self.b

        return fibonacci_number

fib_iter = FibonacciIterator(100)
for fib in fib_iter:
    print(fib)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


gen = reverse("Feliks")
print(next(gen))
print("Marek")
print(next(gen))

def gen_tic_tac_toe():
    yield 'TIC'
    yield 'TAC'
    yield 'TOE'

# gen = gen_tic_tac_toe()
# print(next(gen))
# print('Kolejny krok...')
# print(next(gen))
# print('Kolejny krok...')
# print(next(gen))
#
# print(next(gen))

# wyrażenia generujące
litery = (litera for litera in "Zdzisław")
print(litery)
print(next(litery))
print(next(litery))
print(next(litery))

# i cała reszta
print(list(litery))
