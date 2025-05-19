import sys
from array import array
import random

# tablica zawierająca wartości typu unsigned int
# inicjalny rozmiar = 0 elementów
tab = array('I')
print(len(tab))

# możemy dodać element na koniec tablicy
tab.append(1)
print(len(tab))

# użycie metody extend
tab.extend([2, 3, 4])
print(tab)
print(len(tab))

# poniższy fragment zgłosi błąd TypeError
# tab.extend([2, 3.0, 4])
print(tab)
print(len(tab))

# tablicę możemy również inicjować z istniejących obiektów
# z listy - wywołana zostanie metoda from list klasy array (patrz dokumentacja)
tab_from_list = array('I', [i for i in range(10)])
print(tab_from_list)

# zapisanie tablicy do pliku oraz jej wczytanie
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

# with open('floats_array.bin', 'wb') as file_arr:
#     tab_of_floats.tofile(file_arr)
#
# # wczytujemy ponownie dane do tablicy floatów
# tab_of_floats_loaded = array('f')
# file_arr  = open('floats_array.bin', 'rb')
# tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
# file_arr.close()
# print(tab_of_floats[:10])
#
# # i analogiczna operacja dla listy
# list_of_floats = [random.random() for _ in range(1_000_000)]
# with open('floats_list.txt', 'w') as file_arr:
#     file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
#
# with open('floats_list.txt', 'r') as file_list:
#     list_of_floats_loaded = file_list.readlines()
#
# list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
# print(list_of_floats_loaded[:10])
#
# # i analogiczna operacja dla listy
# list_of_floats = [random.random() for _ in range(1_000_000)]
# with open('floats_list.txt', 'w') as file_arr:
#     file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
#
# with open('floats_list.txt', 'r') as file_list:
#     list_of_floats_loaded = file_list.readlines()
#
# list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
# print(list_of_floats_loaded[:10])

import datetime

# składowe modułu
dir(datetime)

# zakres wartości składowej year w module datetime
print(datetime.MINYEAR, datetime.MAXYEAR)

d = datetime.date(2000, 1, 1)
print(d)
print(d.year, d.month, d.day)

# metody statyczne
print(datetime.date.today())

# epoch start
print(datetime.date.fromtimestamp(0))

# 1000 dni później
# sekundy * minuty * godziny * dni
stamp = 60 * 60 * 24 * 1000
print(datetime.date.fromtimestamp(stamp))

# inne funkcje tej klasy
data = datetime.date.today()

print(data.weekday())
print(data.isoweekday())
print(data.isocalendar())
print(data.isoformat())
print(data.ctime())

now = datetime.datetime.today()
print(now)

print(datetime.datetime.now())

# lista wszystkich dostępnych nazw stref czasowych
import pytz

print('Timezones')
for timeZone in pytz.all_timezones:
    print(timeZone)

from zoneinfo import ZoneInfo

# jaki aktualnie czas w Los Angeles?
print(datetime.datetime.now(ZoneInfo("America/Los_Angeles")))

print(datetime.datetime.strptime('2024/02/03', "%Y/%m/%d"))

print(datetime.datetime.strptime('24/2/3', "%y/%m/%d"))

start_of_this_year = datetime.datetime(2025, 1, 1)
print(start_of_this_year.timestamp())

print(start_of_this_year.replace(year=2020))

print(start_of_this_year.isoformat())
