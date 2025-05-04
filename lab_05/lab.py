import re

# rozpoczyna się od dowolnego znaku, a drugi znak to o
result = re.match('^.o', 'Kowalski')
print(type(result))

# obiekt Match zawiera informacje o tym jaka część łańcucha pasuje do wzorca
print(result)
print(result[0])

# gdybyśmy chcieli sprawdzić czy nazwa kończy się na 'ski` to
# wykorzystując poniższe wyrażenie - nie zadziała jak byśmy tego chcieli
# match dopasowuje tylko na początku wyrażenia
result = re.match('ski$', 'Kowalski')
print(result)

# ale kombinując nieco inaczej, możemy osiągnąć tutaj porządany efekt
result = re.match('.+ski', 'Kowalski')
print(result)


result = re.match('.+ski', 'Jan Kowalski')
print(result)

# w dokumentacji funkcji match wyczytamy również, że dopasowanie zostanie wykonane
# tylko dla pierwszej linii
result = re.match('.+ski', 'Jan Kowalski \n Adam Malinowski')
print(result)

"""Fullmatch"""
# podobnie jak match, ale dopasowuje wzorzec do całej sekwnecji, a nie szuka tylko pasującego fragmentu
result = re.fullmatch('^[A-Z].+ski$', 'Kowalski')
print(result)
result = re.fullmatch('^[A-Z].+ski$', 'Kowalski Jan')
print(result)

"""re.compile
Funkcja re.compile pozwala na kompilację wyrażenia do obiektu wyrażenia regularnego (więcej tu), an którym możemy 
później wywołać metody takie jak match() czy search() oraz inne. Możemy również zdefiniowac dodatkowe flagi 
dla tego wyrażenia.
"""

pattern = '^.o'

regexp = re.compile(pattern)
result = regexp.match('Kowalski')

# to to samo co wcześniejszy przykład
# result = re.match('^.o', 'Kowalski')

# jednak jeżeli chcemy to wyrażenie wykonać wielokrotnie w naszym skrypcie, to po kompilacji może to być bardziej efektywne
print(result)

"""pattern.search
Ta funkcja odnajduje pierwsze dopasowanie wzorca w zadanym łańcuchu znaków. Może przyjmować opcjonalne argumenty 
określające zakres w sekwencji do przeszukania (sekwencja[pos:endpos]).
"""
result = regexp.search('Kowalski')
print(result)

pattern = '[A-Z]'
regexp = re.compile(pattern)
result = regexp.search('Kowalski')
print(result)
result = regexp.search('Kowalski', 1)
print(result)

result = regexp.search('KOalski', 1)
print(result)

"""re.split
Podobnie jak funkcja str.split() dzieli sekwencje łańcucha znaków z wykorzystaniem podanego podłańcucha, tak re.split() 
dzieli łańuch z wykorzystaniem wyrażenia regularnego. Poprzez zdefiniowanie wartości argumentu maxsplit możemy również 
ograniczyc liczbę podziałów, po których funkcja powinna przestać to robić. Zwraca listę.
"""

seq = '1 Abracadabra 2 to 3 czary 4 i 5 magia'
result = re.split('[0-9]', seq)
print(result)
result = re.split('[0-9]', seq, maxsplit=3)
print(result)
print(re.findall('k[a-z]*', 'Ala ma kota, a kot to Filemon.'))
print(re.findall('[0-9]', '1 Abracadabra 2 to 3 czary 4 i 5 magia'))

# jedną z flag, którą możemy przekazać w celu zmiany domyślnego sposobu ewaluacji wyrażenia
# jest re.MULTILINE, które jest przydatne dla przeszukiwania tekstu wielowierszowego (oddzielonego znakami nowego wiersza)

# bez flagi
res = re.findall('^[A-Z].*', 'Bob był budowniczym\nNie bo nie\nco tam słychać?\n')
print(res)

# z flagą
res = re.findall('^[A-Z].+', 'Bob był budowniczym\nNie bo nie\nco tam słychać?\n', flags=re.MULTILINE)
print(res)

"""re.finditer
Funkcja ta zwraca iterator, który zwraca obiekty Match dla każdego odnalezionego dopasowania w łańcuchu znaków.
"""

result = re.finditer('[0-9]', '1 Abracadabra 2 to 3 czary 4 i 5 magia')
print(result)

for res in result:
    print(res)