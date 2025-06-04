import os
import csv
from time import perf_counter

# plik: fibo_threads.py
import threading

# plik fibo_processes.py
import multiprocessing as mp


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)

def main():
    fibo_number = 45
    threads = []
    print('Uruchamianie wątków...')
    t0 = perf_counter()

    for _ in range(os.cpu_count()):
        threads.append(threading.Thread(target=fib, args=(fibo_number,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'Czas wykonania: {perf_counter() - t0}.')
    t_threads = perf_counter() - t0

    processes = []
    print('Uruchamianie procesów...')
    t0 = perf_counter()

    for _ in range(os.cpu_count()):
        processes.append(mp.Process(target=fib, args=(fibo_number,)))

    for t in processes:
        t.start()

    for t in processes:
        t.join()

    print(f'Czas wykonania: {perf_counter() - t0}.')
    t_process = perf_counter() - t0

    # Zapis do CSV
    filename = 'results.csv'
    write_header = not os.path.exists(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(['fibo_number', 't_threads', 't_process'])
        writer.writerow([fibo_number, t_threads, t_process])

if __name__ == '__main__':
    main()