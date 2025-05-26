# przykład ze strony z dokumentacją modułu threading, lekko zmodyfikowany:
# https://docs.python.org/3/library/threading.html

import threading
import time
import random

def crawl(link, delay=3):
    print(f"crawl started for {link} with delay {delay}")
    time.sleep(delay)  # Blocking I/O (simulating a network request)
    print(f"crawl ended for {link}")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]

# Start threads for each link
threads = []
for link in links:
    # Using `args` to pass positional arguments and `kwargs` for keyword arguments
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": random.randint(3, 6)})
    threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()


print('Po wykonaniu wszystkich wątków')

# funkcja wykonująca obliczenia "wolno"
from numbers import Number
import time

def slow_sum(vals: list[Number], result_list: list) -> Number:

    delay = 0.1
    result = 0
    print(f'Sumuję {vals}')
    for num in vals:
        result = result + num
        time.sleep(delay)

    result_list.append(result)

# scenariusz obejmuje porównanie czasu wykonania obliczenia bez wykorzystania wątków oraz w kilku wątkach

nums = list(range(2, 101, 2))
results = []

start = time.perf_counter()
slow_sum(nums, results)
print(f"Czas wykonania: {time.perf_counter() - start}")
print(f"Wynik: {sum(results)}")

# teraz tworzymy kilka wątków i dzielimy listę na kilka fragmentów, a następnie dla każdego wątku przekażemy jeden fragment
import itertools

# w tym przykładzie chcielibyśmy 4 wątki, więc dzielimy dane
# jednak ze względu na to, że podział może nie być równy to paczek może być 4 lub 5
batch_size = len(nums) // 4
threads = []
results = []

start = time.perf_counter()

for batch in itertools.batched(nums, batch_size):
    t = threading.Thread(target=slow_sum, kwargs={"vals": batch, "result_list": results})
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Czas wykonania: {time.perf_counter()  - start}")
print(f"Wynik: {sum(results)}")