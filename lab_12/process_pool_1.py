# plik: process_pool_1.py
import multiprocessing as mp
from time import perf_counter


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


if __name__ == '__main__':

    print('Uruchamianie procesów...')
    t0 = perf_counter()

    # tworzymy pulę 8 procesów
    with mp.Pool(processes=8) as pool:
        # wyniki są zbierane do listy
        results = pool.map(fib, range(40))
        for i, result in enumerate(results):
            print(f"fib({i}) = {result}")

    print(f'Czas wykonania: {perf_counter() - t0}.')