import csv
import random
from array import array
from timeit import timeit
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Porównanie dla integerów
setup_int = """
from array import array
tab = array('i', range(10000))
"""

setup_list_int = """
lst = list(range(10000))
"""

stmt_access_tab = "tab[5000]"
stmt_access_list = "lst[5000]"

stmt_insert_tab = """
for i in range(1000):
    tab.insert(0, i)
"""

stmt_insert_list = """
for i in range(1000):
    lst.insert(0, i)
"""

# Porównanie dla stringów (array nie wspiera stringów – tylko pojedyncze znaki, więc porównujemy listę znaków)
setup_str_array = """
tab = ['a' for _ in range(10000)]
"""

setup_str_list = """
lst = ['a' for _ in range(10000)]
"""

stmt_access_tab_str = "tab[5000]"
stmt_access_list_str = "lst[5000]"

stmt_insert_tab_str = """
for i in range(1000):
    tab.insert(0, 'x')
"""

stmt_insert_list_str = """
for i in range(1000):
    lst.insert(0, 'x')
"""



# ==== TABLICA ====
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

# Zapis tablicy
start_save_array = datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
end_save_array = datetime.now()

# Wczytanie tablicy
start_load_array = datetime.now()
tab_of_floats_loaded = array('f')
with open('floats_array.bin', 'rb') as file_arr:
    tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
end_load_array = datetime.now()

# ==== LISTA ====
list_of_floats = [random.random() for _ in range(1_000_000)]

# Zapis listy
start_save_list = datetime.now()
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
end_save_list = datetime.now()

# Wczytanie listy
start_load_list = datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()
list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end_load_list = datetime.now()



def powitanie_z_wiekiem(birthday_date_str):
    birthday_date = datetime.strptime(birthday_date_str, "%Y-%m-%d").date()
    now = datetime.today().date()

    # Obliczenia wieku
    how_old = relativedelta(now, birthday_date)
    days_from_birth = (now - birthday_date).days

    # Najbliższe urodziny
    this_year_birthday = birthday_date.replace(year=now.year)
    if this_year_birthday < now:
        next_birthday = this_year_birthday.replace(year=now.year + 1)
    else:
        next_birthday = this_year_birthday
    to_nearest_birthday = relativedelta(next_birthday, now)

    # Poprzednie urodziny
    if this_year_birthday > now:
        previous_birthday = this_year_birthday.replace(year=now.year - 1)
    else:
        previous_birthday = this_year_birthday
    since_previous_birthday = relativedelta(now, previous_birthday)

    print(f"Witaj! Na dzień dzisiejszy masz {how_old.years} lat oraz {how_old.months * 30 + how_old.days} dni.")
    print(f"Razem daje to imponujące {days_from_birth} dni!")
    print(f"Twoje najbliższe urodziny będą miały miejsce w dniu {next_birthday} "
          f"czyli za {to_nearest_birthday.months} miesięcy oraz {to_nearest_birthday.days} dni.")
    print(f"Od poprzednich urodzin minęło {since_previous_birthday.months} miesięcy i {since_previous_birthday.days} dni.")


path = '../lab_02/dataset/zamowienia.csv'
dates = []

with open(path, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date_str = row["Data zamowienia"]
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        dates.append(date)

if __name__ == "__main__":

    # Zad 1
    print(f"Inicjalizacja array: {timeit(setup_int, number=100)}")
    print(f"Inicjalizacja list:  {timeit(setup_list_int, number=100)}")

    print(f"Dostęp: array: {timeit(stmt_access_tab, setup_int, number=1000000)}")
    print(f"Dostęp: list:  {timeit(stmt_access_list, setup_list_int, number=1000000)}")

    print(f"Insert: array: {timeit(stmt_insert_tab, setup_int, number=10)}")
    print(f"Insert: list:  {timeit(stmt_insert_list, setup_list_int, number=10)}")

    print("\n Str (list vs list of chars)\n")
    print(f"Inicjalizacja 'tab' (lista znaków): {timeit(setup_str_array, number=100)}")
    print(f"Inicjalizacja listy:               {timeit(setup_str_list, number=100)}")

    print(f"Dostęp: tab:  {timeit(stmt_access_tab_str, setup_str_array, number=1000000)}")
    print(f"Dostęp: list: {timeit(stmt_access_list_str, setup_str_list, number=1000000)}")

    print(f"Insert: tab:  {timeit(stmt_insert_tab_str, setup_str_array, number=10)}")
    print(f"Insert: list: {timeit(stmt_insert_list_str, setup_str_list, number=10)}")

    # Zad 2
    print("Czas zapisu tablicy:", end_save_array - start_save_array)
    print("Czas odczytu tablicy:", end_load_array - start_load_array)
    print("Czas zapisu listy:", end_save_list - start_save_list)
    print("Czas odczytu listy:", end_load_list - start_load_list)

    # Zad 3
    print(powitanie_z_wiekiem("2001-06-29"))

    # Zad 4
    oldest = min(dates)
    newest = max(dates)
    difference = (oldest - newest).days

    print("Oldest date:", oldest)
    print("Newest date:", newest)
    print("Difference in days:", difference)