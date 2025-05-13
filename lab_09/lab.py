import os
import sys

print(sys.builtin_module_names)

lista = [1,2,3]
print(f'Lista {lista} ma rozmiar {sys.getsizeof(lista)} bajtów')

lista2 = list()
lista2.append(1)
lista2.append(2)
lista2.append(3)
print(f'Lista2 {lista2} ma rozmiar {sys.getsizeof(lista2)} bajtów')

lista3 = [] + [1,2,3]
print(f'Lista3 {lista3} ma rozmiar {sys.getsizeof(lista3)} bajtów')

def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name

listas = [lista, lista2, lista3]

lista.append(5)
lista2.append(5)
lista2.append(6)
lista3.append(5)
lista3.append(6)
lista3.append(7)


for list_obj in listas:
    print(f'{get_var_name(list_obj)} {list_obj} ma rozmiar {sys.getsizeof(list_obj)} bajtów')

print(list(filter(lambda x: not (x.startswith('__') or x.startswith('_')),dir(sys.stdin))))


print(os.environ['username'])
