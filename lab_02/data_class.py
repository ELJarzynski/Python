"""Sygnatura dekoratora wygląda jak poniżej:
def dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
                match_args=True, kw_only=False, slots=False, weakref_slot=False)"""

from dataclasses import dataclass, field, make_dataclass


@dataclass
class User:
    username: str # adnotacja
    email: str # adnotacja
    is_active: bool = False # adnotacja z wartością domyślną
    is_admin = False # pole na poziomie klasy (nie instancji)

u = User('zealot','zealot@student.uwm.edu.pl', True)


from copy import deepcopy
u1 = deepcopy(u)
u == u1

u1.username = 'adept'
print(u1)
print(u)
u == u1

"""
pola klasy dataclass można również deklarować z użyciem jawnego wywołania dataclass.field
sygnatura: dataclasses.field(*, default=MISSING, default_factory=MISSING, init=True, repr=True, 
hash=None, compare=True, metadata=None, kw_only=MISSING)"""

