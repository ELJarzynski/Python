def decorator(obj):
    return obj

def say_hello():
    print('Hello')

@decorator
def say_bla():
    print('Bla!')

# # wywołanie dekoratora jest ekwiwalentem powniższego wywołania
# # zapisujemy do zmiennej obiekt zwrócony przez dekorator, czyli tu funkcję
say_hello = decorator(say_hello)


# inny przykład
# tutaj wywołanie funkcji udekorowanej wywoluje inną funkcję

def cos_innego():
    print("cos innego")

def decorator(obj):
    return cos_innego

@decorator
def main():
    print("hello")



# Funkcja dekorowana jest wywoływana wewnątrz funkcji dekorującej

def zrob_zrob(obj):
    obj()
    obj()

@zrob_zrob
def main():
    print("Do roboty")



# W praktyce opakowujemy wewnątrz dekoratora funkcję dekorującą jeszcze jedną funkcją
"""
Taka konstrukcja również nie jest w pełni funkcjonalna. Obiekt zwracany jest tu typu wrapper, a nie naszej funkcji
dekorowanej i jeżeli funkcja main coś zwraca, to ta informacja jest tracona. Nie ma tutaj również obsługi
ewentualnych argumentów przekazanych do funkcji."""
def zrob_zrob(obj):
    def wrapper():
        obj()
        obj()
    return wrapper

@zrob_zrob
def main():
    print("Do pracy")



# dodanie argumentów do wnętrza dekoratora

def zrob_zrob(obj):
    def wrapper(*args, **kwargs):
        obj(*args, **kwargs)
        obj(*args, **kwargs)
    return wrapper

@zrob_zrob
def main(x):
    print(f'{x}')



# jednak jeżeli nasza funkcja coś zwraca to ta informacja jest nadal tracona
# dodatkowo obiekt zwracany to funkcja wrapper

def zrob_zrob(obj):
    def wrapper(*args, **kwargs):
        obj(*args, **kwargs)
        obj(*args, **kwargs)
    return wrapper


@zrob_zrob
def main(x):
    return f'{x}'



# args i kwargs pozwal na obsługiwanie dwowolnych arggumentów

def zrob_zrob(obj):
    def wrapper(*args, **kwargs):
        """to wrapper"""
        print("dekoruję...")
        res = obj(*args, **kwargs) # przekazywane argumentów do oryginalnej funkcji
        return res
    return wrapper


@zrob_zrob
def main(x):
    """udekorowana"""
    return f'{x}'



# nadal obiekt zwracany jest typu wrapper, co może być problemem w przypadku kontroli typów
# wywołujemy return dla funkcji dekorowanej
# ale również dla wrapper

def zrob_zrob(obj):
    def wrapper(*args, **kwargs):
        print("dekoruje..")
        obj(*args, **kwargs)
        return obj(*args, **kwargs)
    wrapper.__name__ = obj.__name__
    wrapper.__doc__ = obj.__doc__
    return wrapper

@zrob_zrob
def main(x):
    """Udekorowana"""
    return f'{x}'


# Żeby się z tym nie męczyć wykorzystujemy stworzony dekorator z functools
from functools import wraps

def zrob_zrob(obj):
    @wraps(obj)
    def wrapper(*args, **kwargs):
        print("Gotuje")
        obj(*args, **kwargs)
        return obj(*args, **kwargs)
    return wrapper

@zrob_zrob
def main(x):
    """udekorowana"""
    return f'{x}'
print(main, main(10), main.__name__, main.__doc__)

"""Przydatne użycie dekoratorów"""

from time import perf_counter

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        print(f"Funkcja wykonała się w {stop - start:.2f}s")
        return result
    return wrapper

@execution_time
def milion(val):
    (val for _ in range(1000000))

print(milion(0))
print(milion('boom!'))
print(milion(1/3))

import time

def sleep(sleep_time):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f'Czekam {sleep_time} sekund...')
            time.sleep(sleep_time)
            return func(*args,**kwargs)
        return wrapper
    return inner

@sleep(sleep_time=5)
def wakeup():
    print("Czas minął")

@sleep(sleep_time=2)
def wakeup_fast():
    print("Czas minął tak szybko!")

# wakeup()
# wakeup_fast()

def sleep(_func=None, *, sleep_time=3):
    def inner(func):
        # functools.wraps(func)
        def wrapper(*args,**kwargs):
            # print(sleep_time)
            # sleep_time = sleep_time if isinstance(sleep_time, int) else 3
            print(f'Czekam {sleep_time} sekund...')
            time.sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper
    if _func is None:
        return inner
    else:
        return inner(_func)

@sleep(sleep_time=5)
def wakeup():
    print("Czas minął!")

@sleep(sleep_time=2)
def wakeup_fast():
    print("Czas minął tak szybko!")

# wakeup()
# wakeup_fast()

def wakeup(name='Jan'):
    return f"Czas minął {name}!"


class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja {self.func.__name__} wykonała się w czasie {end_time - start_time:.08f} sekund")
        return result


@TimerDecorator
def powtorz(co, ile):
    return co * ile


print(powtorz('Foo ', 20))