import itertools
import string
import re


# Zad 1
class EvenIndex:
    """Iterator zwracający wartości na parzystych indeksach"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 2
        return value


# Zad 2
class PrimeGenerator:
    """Prime numbers generator"""

    def __init__(self, length):
        self.length = length
        self.index = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration

        while self.index < self.length:
            is_prime = True
            for j in range(2, self.index):
                if self.index % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result = self.index
                self.index += 1
                return result
            self.index += 1
        raise StopIteration

# Zad 3
class DaysIter:
    """Day after day Night after night"""

    def __init__(self, start_day):
        self.days = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
        if start_day not in self.days:
            raise ValueError('Nieprawidłowy dzień tygodnia')
        self.index = self.days.index(start_day)


    def __iter__(self):
        return self

    def __next__(self):
        day = self.days[self.index]
        self.index = (self.index + 1) % len(self.days)
        return day


# Zad 4
class TextIter:
    """This works well"""

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.words = re.findall(r'\w+', text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration

        word = self.words[self.index]
        self.index += 1
        return word


# Zad 5
def text_generator(text):
    """This works Yield well"""

    words = re.findall(r'\w+', text)

    for word in words:
        yield word


# Zad 6
def code_generator(letter_pos, num_pos):
    """Homework done"""

    alphabet = string.ascii_uppercase
    num_range = range(10**(num_pos - 1), 10**num_pos)

    for letter_tuple in itertools.product(alphabet, repeat=letter_pos):
        letter_part = ''.join(letter_tuple)
        for num in num_range:
            num_part = str(num).zfill(num_pos)
            yield f"{letter_part}_{num_part}"

if __name__ == "__main__":

    # Zad 1
    list_1 = [1,2,3,4,5,6,7,8]
    as_1 = EvenIndex(list_1)
    for _ in as_1:
        print(_)

    # # Zad 2
    as_2 = PrimeGenerator(20)
    for _ in as_2:
        print(_)

    # Zad 3
    as_3 = DaysIter('czwartek')
    for _ in range(10):
        print(next(as_3))

    # Zad 4
    text = """
        abba kaba papa 
        baba fran
        siema cisz
        BMW ek
        aUDI
    """
    as_4 = TextIter(text)
    for _ in as_4:
        print(_)

    # Zad 5
    as_5 = text_generator(text)
    for _ in as_5:
        print(_)

    gen = code_generator(1, 2)
    for _ in range(5):
        print(next(gen))

    gen = code_generator(2, 3)
    for _ in range(5):
        print(next(gen))
