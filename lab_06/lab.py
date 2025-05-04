text = r"""Adam Malinowski
.gitignore
2023-01-17 error "Page not found"
[2025-03-06] NOTICE "User admin logged in"
Code 3300 was invalid
https://www.onet.pl 200 176353
File /etc/passwd: permission denied
Józef
C:\Program Files
Ania
JOLA
marek
Kowalski
bodo363
PIN 0000 was invalid
/users/test is not a valid directory name
192.168.0.1 access denied
1000
666
"""

import re

# zwraca łańcuchy rozpoczynające się od A
p1 = re.findall(r'\AA.+', text, flags=re.DEBUG)
print(p1)

# zwraca wyrazy, które rozpoczynają się od znaku /
p2 = re.findall(r'\b/[a-z]+', text)
print(p2)

# zwraca wyrazy, które kończą się znakiem ciągiem ski
p3 = re.findall(r'[a-zA-Z]+ski\b', text)
print(p3)


# zwraca wszystkie wyrazy
p4 = re.findall(r'\w+', text)
print(p4)

# znajduje wszystkie wyrazy, które rozpoczynają się wielką literą i kolejne znaki to też wielkie litery
p5 = re.findall(r'\b[A-Z]+', text)
print(p5)

# znajduje wszystkie wyrazy, które rozpoczynają się wielką literą i kolejne znaki to też wielkie litery
p6 = re.findall(r'\b[A-Z]+', text)
print(p6)

p7 = re.findall(r'\b[^\d\W]+\b', text)
print(p7)

text = "Python 3.10 is awesome, but Python 2.7 is outdated."

# Znajdź wszystkie wystąpienia "Python", po których występuje wersja zaczynająca się od "3", ale wersji nie wyświetlaj
pattern = r"Python(?=\s3\.\d+)"
matches = re.findall(pattern, text)

print("Konsumowanie w przód:", matches)

# Znajdź wszystkie wersje, które są poprzedzone słowem "Version"
text = "Version 3.10 is stable, but version 2.7 is deprecated."

pattern = r"(?<=Version\s)\d\.\d+"
matches = re.findall(pattern, text, flags=re.I)

print("Konsumowanie w tył:", matches)

text = "Standardowa cena to $100, ale cena po rabacie to $80."

# Znajdź liczby, które są poprzedzone znakiem dolara i następują po nich przecinki lub kropki
pattern = r"(?<=\$)\d+(?=[,.])"
matches = re.findall(pattern, text)

print("Konsumowanie w przód oraz w tył:", matches)


text = "cat, caterpillar, dog, catalog"

# Znajdź wszystkie słowa zaczynające się od "cat", ale nie kończące się na "er"
pattern = r"cat(?!er)"
matches = re.findall(pattern, text)

print("Negatywne konsumowanie w przód:", matches)


text = "error404, success200, error500, success404"

# Znajdź wszystkie kody błędów, które nie są poprzedzone słowem "success"
pattern = r"(?<!success)\d{3}"
matches = re.findall(pattern, text)

print("Negatywne wyszukiwanie w tył:", matches)


# przykład 1
text1 = 'Data narodzin Adama to 1995-05-20'

p1 = re.findall(r'(\d{4})-(\d{2})-(\d{2})', text1)
print("p1",p1)

# dla ciekawości przetestuj
p2 = re.findall(r'(\d{4})-(\d{2})-(\d{2})', text1, flags=re.DEBUG)
print("p2", p2)

p3 = re.findall(r'(\d{4})(-)(\d{2})(\2)(\d{2})', text1)
print("p3", p3)

# przykład 3
# grupom możemy nadać nazwy
p4 = re.findall(r'(?P<rok>\d{4})-(?P<miesiac>\d{2})-(?P<dzien>\d{2})', text1)
print("p4", p4)

# przykład 4 - grupa nie przechwytująca
# jeżeli chcemy określić grupę we wzorcu, ale nie umieszczać jej dopasowania w wynikach to poprzedzamy
# wyrażenie w danej grupie znakami ?:
p5 = re.findall(r'(\d{4})-(?:\d{2})-(\d{2})', text1)
print("p5", p5)

# przykład z grupą oraz alternatywnym wyrażeniem, wyszukuje początek ścieżki w stylu Unix oraz Windows
p6 = re.findall(r'(\b/[a-z]+|\b[a-zA-Z]:\\\w+)', text)
print("p6",p6)