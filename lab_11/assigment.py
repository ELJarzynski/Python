from tqdm import tqdm
import threading
import requests
import random
import psutil
import string
import this
import time


# Zad 2
def enigma():
    encoding_dict = this.d
    to_encode = input("Wprowadź zdanie do zakodowania: ")
    encoded = ''.join(encoding_dict.get(c, c) for c in to_encode)
    print("Encoded sentence")

    return encoded

# Zad 3
def crawl(link, delay=3):
    print(f"crawl started for {link} with delay {delay}")
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()

        # Tworzenie nazwy pliku na podstawie url
        filename = link.replace("https://", "").replace("/", "_") + ".html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"crawl ended for {link} saved to {filename}")
    except Exception as e:
        print(f"Błąd podczas pobierania {link}: {e}")

def crawl_links(links):
    threads = []
    for link in links:
        t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": random.randint(1, 3)})
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('Po wykonaniu wszystkich wątków')

# Zad 4
class RamMonitorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        while not self._stop_event.is_set():
            ram_usage = psutil.virtual_memory().percent
            print(f"\rRAM Usage: {ram_usage}%", end="")
            time.sleep(5)

# Zad 5
# generwanie txtków
def generate_random_line(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

def create_random_txt_files(filenames, lines_per_file=100, line_length=40):
    for filename in filenames:
        with open(filename, 'w', encoding='utf-8') as f:
            for _ in range(lines_per_file):
                f.write(generate_random_line(line_length) + '\n')
    print("Pliki zostały utworzone.")

# zadanie
# Funkcja odczytująca plik linia po linii z opóźnieniem i tqdm
def slow_read(file_path: str, result_list: list, thread_id: int):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total = len(lines)
            result = []

            print(f"[Wątek {thread_id}] Odczytuję {file_path} ({total} linii)")
            for line in tqdm(lines, desc=f"Wątek {thread_id}", position=thread_id):
                result.append(line.strip())
                time.sleep(0.05)

            result_list.append((file_path, result))
    except FileNotFoundError:
        print(f"[Wątek {thread_id}] Plik nie znaleziony: {file_path}")

def file_reader():
    file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    threads = []
    results = []

    start = time.perf_counter()

    for idx, file in enumerate(file_names):
        t = threading.Thread(target=slow_read, args=(file, results, idx))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    print(f"\nCzas wykonania: {elapsed:.2f} sekund")


def main():
    # Zad 1
    # zmienna binary to string
    binary = '111'

    # 1. wyświetla poprostu ciąg znaków dla zmiennej binary
    print(binary)
    # 2. Zmienia ciąg znaków binary na int liczbe dziesiętną, bin przekszztałca liczbe dziesiętną w reprezentacje binarną
    print(bin(int(binary)))
    # 3. Zmienia string binary na int liczbę dziesiętną
    print(int(binary))
    # 4 Zmienia ciąg znaków binary na int liczbe dziesiętną, hex przekszztałca liczbe dziesiętną w reprezentacje szesnastkową
    print(hex(int(binary)))
    # 5. binary zostaje traktowana jako int, traktuję ją jako liczbę w systemie binarnym,
    # oblicza wartość dziesiętną i zwraca liczbę całkowitą
    print(int(binary, base=2))
    # 6. binary zostaje traktowana jako int, traktuję ją jako liczbę w systemie ósemkowym,
    # oblicza wartość dziesiętną i zwraca liczbę całkowitą
    print(int(binary, base=8))
    # 7. binary zostaje traktowana jako int, traktuję ją jako liczbę w systemie szesnastkowym,
    # oblicza wartość dziesiętną i zwraca liczbę całkowitą
    print(int(binary, base=16))

    # Zad 2
    print(this.d)
    print(enigma())

    # Zad 3
    links = [
        "https://python.org",
        "https://stackoverflow.com",
        "https://github.com",
        "https://www.wikipedia.org",
        "https://www.bbc.com",
    ]

    crawl_links(links)

    # Zad 4
    # Uruchomienie monitorowania RAM
    monitor = RamMonitorThread()
    monitor.start()

    # Monitorowanie i zakończnie
    time.sleep(15)
    monitor.stop()
    monitor.join()
    print("\nMonitorowanie zakończone.")

    # Zad 5
    # file_names = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    # create_random_txt_files(file_names, lines_per_file=100, line_length=40)
    file_reader()


if __name__ == "__main__":
    main()