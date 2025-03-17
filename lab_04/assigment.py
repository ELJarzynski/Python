# Zadanie 1
from datetime import datetime
from functools import wraps


def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args and not kwargs:
            return f'[{datetime.now()}] Użyto funkcji: {func.__name__} z wartościami {args}'
        if kwargs and not args:
            return f'[{datetime.now()}] Użyto funkcji: {func.__name__} z wartościami  {kwargs}'
        else:
            return f'[{datetime.now()}] Użyto funkcji: {func.__name__} z wartościami {args}, {kwargs}'
    return wrapper

@logging
def suma(a,b):
    return a + b

class User:
    def __init__(self, permissions):
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions


def require_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if not user.has_permission(permission):
                return f'Nie masz pozwolenia bratku'
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_permission('admin')
def delete_user(user, user_id):
    print(f"User {user_id} deleted")

# Zadanie 3

def Singleton(cls):
    """
    Singleton zapewnia, że klasa będzie miała tylko jedną instancję.
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@Singleton
class Car:
    def __init__(self, model):
        self.model = model
        print(f"The best car brand is: {self.model}")

    def car_brand_no_1(self):
        return f"Of course it is {self.model}"


def main():
    #Zadanie 1
    print(suma(1, 2))

    # Zadanie 2
    # Przykładowe wywołanie
    admin_user = User(permissions=['admin'])
    print(delete_user(admin_user, 123))

    npc_user = User(permissions=['bot'])
    print(delete_user(npc_user, 2798))

    # Zadanie 3
    db1 = Car("BMW")
    print(db1.car_brand_no_1())

    db2 = Car("AUDI")
    print(db2.car_brand_no_1())

if __name__ == '__main__':
    main()

