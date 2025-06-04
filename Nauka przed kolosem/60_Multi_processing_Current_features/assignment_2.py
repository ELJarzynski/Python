# Zad 2
import os
import requests
from concurrent.futures.thread import ThreadPoolExecutor



def crawl(link, delay=3):
    print(f"crawl started for {link} with delay {delay}")
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()

        # Tworzenie folderu, jeśli nie istnieje
        folder = "html_python"
        os.makedirs(folder, exist_ok=True)

        # Tworzenie nazwy pliku na podstawie URL
        filename = link.replace("https://", "").replace("/", "_") + ".html"
        filepath = os.path.join(folder, filename)

        # Zapis do pliku w podfolderze
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"crawl ended for {link} saved to {filepath}")
    except Exception as e:
        print(f"Błąd podczas pobierania {link}: {e}")


def main():
    data = [
        "https://python.org",
        "https://stackoverflow.com",
        "https://github.com",
        "https://www.wikipedia.org",
        "https://www.bbc.com",
    ]

    max_workers = os.cpu_count() // 2

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        feature = executor.map(crawl, data)
        futures.append(feature)

if __name__ == '__main__':
    main()