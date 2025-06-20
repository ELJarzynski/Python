# plik: process_pool_2.py
import multiprocessing as mp
from time import perf_counter


def sum_nums(*nums):
    return sum(nums)


if __name__ == '__main__':

    print('Uruchamianie procesów...')
    t0 = perf_counter()

    # tworzymy pulę 8 procesów
    with mp.Pool(processes=8) as pool:
        # wyniki są zbierane do listy
        results = pool.map(sum_nums, range(40), chunksize=4)
        for i, result in enumerate(results):
            print(f"sum_nums({i}) = {result}")

    print(f'Czas wykonania: {perf_counter() - t0}.')