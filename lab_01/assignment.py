import math
from abc import abstractmethod


class Figure:

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_field(self):
        pass

    @abstractmethod
    def get_circumference(self):
        """Abstrakcyjna metoda zwracająca obwód figury"""
        pass

class Square(Figure):
    """ Klasa do obsługi figury typu kwadrat"""
    def __init__(self, side=1):
        self.side = side

    def get_field(self):
        return self.side ** 2

    def get_circumference(self):
        return self.side * 4

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self.side = math.sqrt(self.side**2 + other.side**2)
        elif isinstance(other, int):
            self.side += other
        else:
            raise TypeError(
                "unsupported operand for +=: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        return self

    def __radd__(self, other: int):
        import math
        if isinstance(other, int):
            new_side = math.sqrt(other**2 + self.side**2)
            return Square(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __add__(this, other):
        if isinstance(other, type(this)):
            new_side = math.sqrt(this.side**2 + other.side**2)
            return type(this)(new_side)
        elif isinstance(other, int):
            new_side = this.side + other
            return type(this)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(this).__name__}' and '{type(other).__name__}'"
            )

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        if isinstance(other, Square):
            # lub
            # if isinstance(other, type(self)):
            return self.side == other.side
        return False


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self) -> str:
        return f"Circle({self.radius})"

    def get_field(self):
        """Oblicza pole koła"""
        return math.pi * self.radius ** 2

    def get_circumference(self):
        """Oblicza obwód koła"""
        return 2 * math.pi * self.radius


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

    # Dzięki 'name' możemy rozróżnić, który atrybut obiektu próbujemy ustawić i zastosować odpowiednią logikę
    def __setattr__(self, name, value):
        if name == "value":
            if isinstance(value, int):
                if 10 <= value <= 2000:
                    super().__setattr__(name, value)
                else:
                    raise ValueError("Wartość dla typu int musi być w zakresie 10-2000.")
            elif isinstance(value, str):
                super.__setattr__(name, value)
            else:
                raise TypeError(f"Unsupported type {type(value)} for 'value'.")
        else:
            super().__setattr__(name, value)


def main():
    print("Zadanie 1 \n")
    square1 = Square(3)
    print(f'Adres square1 = {id(square1)}')
    square2 = Square(4)
    print(f'Adres square2 = {id(square2)}')

    # __iadd__
    square1 += square2
    print(f"Square1 {square1} a jego id = {id(square1)} adres się nie zimenia")

    # __add__
    square3 = square1 + square2
    print(f"Po Square1 + Square2: {square3} nowy adres = {id(square1)}")

    # __add__ z int
    square4 = square1 + 5
    print(f"Po Square1 + 5: {square4} nowy adres = {id(square4)}")

    # __radd__
    square5 = 5 + square1
    print(f"Po 5 + Square1: {square5} nowy adres = {id(square5)}\n")

    print("Zadanie 2\n")

    circle = Circle(3)
    print(f'Obwód koła o promieniu 3 = {circle.get_circumference()}')

    print(f'Obwód kwadratu o krawędzi 5 = {square1.get_circumference()}\n')

    print("Zadanie 3\n")

    field1 = Field(100)
    print(f"field1: {field1}")

    field1.value = 5
    print(f"Field1 po przypisaniu za małej wartości 5: {field1}")

    field1.value = "Testowa wartość"
    print(f"Field1 po przypisanu stringa: {field1}")


    # Test dla przypisania wartości float (niedozwolone)
    field1.value = 3.14


    field1.value = 1500
    print(f"Field1 po przypisaniu 1500: {field1}")


if __name__=="__main__":
    main()