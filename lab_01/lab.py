class Dummy():
    """Doc string"""

    #zmienna klasowa - współdzielona pomiędz instancje klas Dummy
    class_counter = 0

    # inicjalizator
    def __init__(self):
        print("__init__()")
        # Dostęp do zmiennej klasowej
        Dummy.class_counter += 1

        # zmienna instancji
        self.foo = ' foo foo'

    """Metoda new() jest wywoływana przed inicjalizatorem i zwraca obiekt wywołanego typu (czyli tu Dummy) 
       można to nazwać konstruktorem"""
    def __new__(cls, *atgs, **kwargs):
        print('__new__()')
        return super().__new__(cls)

    """Metoda del jest wywoływana w momencie usuwania obiektu z pamięci czyli w momencie "śmierci" obiekty
       (spadek liczby referencji do 0 do obszaru w pamięci zajmowanego przez przez obiekt), nazywana jest destruktorem"""
    def __dedl__(self):
        print(('__del__()'))

def main_l1():
    d = Dummy()
    print(d.__doc__)
    print(d.class_counter)
    print(d.foo)

    # zmienna obiektu
    d.so_what = "Who am I?"
    print(d.__dict__)

    del d

    d1 = Dummy()
    print(d1.class_counter)
    print(d1.foo)
    print(d1.__dict__)

# Listing 2
# czy to ejst poprawny składniowo kod Python?
class whoops: pass

wh = whoops()

# a to?
class whoopsi: ...

"""Podobny do powyższego zapis znajdziemy w plikacj z rozszerzeniem .pyi, które są plikami zawierającymi tylko szkielety
   (ang. stub), który może zawierać tylko sygnatury funkcji, klas i ich metod, które pełnią funkcje interfejsów
    w Pythonie, których nie możemy impplementować w sposób znany chociażby z języka Java czy C#. Można to np. zobaczyć 
    w pliku builtins.pyi ale i w wielu innych"""

wh2 = whoopsi()

def main_l2():
    print(wh.__class__, wh2.__class__)

# Więcej o wyrażeniu pass: https://docs.python.org/3/tutorial/controlflow.html#pass-statements
# Więcej o wyrażeniu ... (Ellipsis): https://docs.python.org/3/library/constants.html#Ellipsis


# Listing 4

class Square:
    """Klasa do obsługi figury typu kwadrat"""

    def __init__(self, side=1):
        self.side = side

    def __str__(self) -> str:
        return f"Square({self.side})"

    # tu możemy się zastanowić jak zrealizować dodawanie dwóch kwadratów
    # czy sumujemy długość boku (stworzymy kwadrat o boku, który opisuje dwa kwadraty?, czy też sumujemy pole i wyznaczamy nową wartość size?
    # przyjmijmy ten drugi scenariusz
    # nazwa pierwszego argumenty metody, która w dokumentacji zawsze nosi nazwę self, jest tylko umową, ale wymogiem jest to, że będzie przekazywana
    # do metody zawsze jako pierwszy argument. Więc jak wolimy this to ...
    def __add__(this, other):
        import math
        if isinstance(other, type(this)):
            new_side = math.sqrt(this.side**2 + other.side**2)
            return type(this)(new_side)
        else:
            raise TypeError(
                "unsupported operand for : "
                f"'{type(this).__name__}' and '{type(other).__name__}"
            )

    def __mul__(self, scale: int | float) -> float:
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float) -> float:
        return Square(self.side / scale)


    def __eq__(self, other):
        if isinstance(other, Square): # lub # if isinstance(other, type(self))
            return self.side == other.side
        return False

def main_l4():
    s = Square(2)
    s2 = Square(3)

    print(s, ' + ', s2, ' to ', s + s2)
    print(s * 3)
    print(s / 2)
    print(s == s2)


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Field({self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.value == other.value
        else:
            return False


class KoloFortuny:
    def __init__(self, *fields):
        self.fields = [tuple[int, Field]]
        if fields:
            self.fields = list(zip(range(1, len(fields) + 1), [Field(val) for val in fields]))

    def __str__(self):
        return f"KoloFortuny({self.fields})"

    def __getitem__(self, idx):
        return self.fields[idx][1]

    def __setitem__(self, idx, val:Field):
        if isinstance(val,Field):
            self.fields[idx] = (idx + 1, val)
        else:
            raise TypeError("Można wstawić tylko wartość typu Field!")

    def __iter__(self):
        return iter(self.fields)

    def __contains__(self, other):
        if isinstance(other, Field):
            return other in [val for _, val in self.fields]
        else:
            raise TypeError("Nie umiem znaleźć innych elementów niż te typu FIeld!")



def main_l6():
    kolo = KoloFortuny(100, 'Bankrut', 50, 300, 'Niespodzianka', 1000)
    print(kolo)
    print(kolo[3])
    kolo[3] = Field(750)
    # odkomentuj poniższą linię i sprawdź działanie
    # kolo[3] = 750

    for field in kolo:
        print(field)

    print(Field(750) in kolo)

if __name__ == "__main__":
    main_l6()