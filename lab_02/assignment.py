# Zadanie 1
from collections import namedtuple
import csv


def csv_to_namedtuple(filename):
    """Nagłówki są przekształcane na małe litery, a spacje są zamieniane na znak podkreślenia, zwraca liste krotek"""
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)

        headers = [header.lower().replace(' ', '_') for header in headers]
        Order = namedtuple('Order', headers)

        orders = [Order._make(row) for row in reader]

    return orders


orders = csv_to_namedtuple('dataset/zamowienia.csv')


# Zadanie 2
Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
p4 = Point(4, 3)


# Zadanie 3
from dataclasses import make_dataclass


slownik = {
    1: {
        'class_name': 'Osoba',
        'props': [('name', 'str'), ('is_admin', 'bool', 'False')]},
    2: {
        'class_name': 'Produkt',
        'props': [('name', 'str'), ('price', 'float', '0.0'), ('quantity', 'float', '0.0')]},
}

new_data_classes = {}

for key, value in slownik.items():
    new_data_classes[value['class_name']] = make_dataclass(value['class_name'], value['props'])


def main():
    print("Zadanie 1")
    for order in orders[:10]:
        print(order)

    print("\nZadanie 2")
    print(dir(p1))
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 != p3: {p1 != p3}")
    print(f"p1 < p3: {p1 < p3}")
    print(f"p1 <= p2: {p1 <= p2}")
    print(f"p3 > p4: {p3 > p4}")
    print(f"p3 >= p4: {p3 >= p4}")

    # Arytmetyczne
    p5 = Point(p1.x + p4.x, p1.y + p3.y)
    p6 = Point(p3.x - p1.x, p4.y - p1.y)
    p7 = Point(p1.x * 2, p1.y * 2)
    p8 = Point(p4.x / 2, p3.y / 2)
    print(f'Dodawanie {p5}')
    print(f'Odejmowanie {p6}')
    print(f"Mnożenie {p7}")
    print(f'Dzielenie {p8}')

    #Zadanie 3
    print("\nZadanie 3")
    print(new_data_classes.keys())
    osoba = new_data_classes['Osoba'](name='Jan', is_admin=True)
    produkt = new_data_classes['Produkt'](name='Laptop', price=2500.0, quantity=10.0)
    print(osoba)
    print(produkt)

if __name__ == "__main__":
    main()