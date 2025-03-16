from dataclasses import fields
from enum import Enum
import inspect

class FieldType(Enum):
    INTEGER = 1
    FLOAT = 2
    STRING = 3
    DATE = 4


class Field:

    def __init__(self, field_type: FieldType):
        self.field_type = field_type

    def get_fieldtype(self):
        return  self.field_type

    def __str__(self):
        return self.field_type.__class__.__name__


class Model:

    def __init__(self, db_table=None):
        if db_table is None:
            self.db_table = f'db_{self.__class__.__name__.lower()}'
        else:
            self.db_table =db_table

    def get_fields(self):
        fields = {}
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, Field):
                fields[name] = obj.get_fieldtype()
        return fields

    def __setattr__(self, attr, val):
        for name, obj in inspect.getmembers(self):
            if name == attr and isinstance(obj, Field):
                obj.value = val
                return
        super().__setattr__(attr, val)

    @staticmethod
    def generate_table_for_name(name: str):
        """ metoda statyczna wzracająca nazwę tabeli dla przykładowej nazwy modelu """
        return f'db_{name.lower()}'

    @classmethod
    def from_dict(cls, name: str, fields: dict[str, Field]):
        # wykorzystanie match ase z mapowaniem słownika
        for field in fields.items():

            match field:
                case (str(), Field()):
                    setattr(cls, field[0], field[1])

        model = cls()
        model.db_table = f'db_{name.lower()}'
        return model

print(FieldType.INTEGER)
print(FieldType.INTEGER.name)
print(FieldType.INTEGER.value)
print(FieldType)

# wywołanie metoddy statycznej
print(Model.generate_table_for_name('Osoba'))

# Czy można stworzyć instancje klasy model?
model = Model()
# Jeszcze jak klasa nie jet abstrakcyjna
print(model.get_fields())

model.id = Field(FieldType.INTEGER)
print(model.get_fields())

"""Deklaracja klasy dziedzicznej po Model"""
class Person(Model):
    id = Field(FieldType.INTEGER)
    firstname = Field(FieldType.STRING)
    lastname = Field(FieldType.STRING)
    age = Field(FieldType.INTEGER)

p = Person()
print(p.db_table)
print(p.id)
print(p.get_fields())
test = Model.from_dict('Movie',{'id': Field(FieldType.INTEGER), 'name': Field(FieldType.STRING)})

print(test.get_fields())
print(test.db_table)


"""Abstrakcyjne klasy bzowe (ABC - Abstract Base Classes)"""
from abc import ABC, abstractmethod


class Field(ABC):

    def __init__(self):
        self.value = None

    def get_fieldtype(self):
        return self.__class__.__name__

    def __setattr__(self, attr, val):
        if attr == 'value':
            self._set_field_value(val)
        else:
            super().__setattr__(self, attr, val)

    @abstractmethod
    def _get_field_value(self):
        ...

    @abstractmethod
    def _set_field_value(self, val):
        ...

    def __str__(self):
        return self.__class__.__name__

class StringField(Field):

    def _set_field_value(self, val):
        if isinstance(val, str):
            self.value = val

    def _get_field_value(self):
        return self.value





class RefactoredModel(Model):

    def __init__(self, db_table=None):
        super().__init__(db_table if db_table else self.generate_table_for_name(self.__class__.__name__))

# kod w klasie Model pozwala na przypisanie właściwości typu Field do instancji klasy model
class Movie(RefactoredModel):
    title = StringField()
    director = StringField()

def main():
    m = Movie()
    print(m.db_table)

if __name__ == "__main__":
    main()