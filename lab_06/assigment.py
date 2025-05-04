import re

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

tel = ['+48 555 444 333',
'(48) 555-444-333',
'(+48)555444333',
'+48 555444333',
 '+48555444333',
 '48555444333']

tekst = """
Komputer: 3999.00 PLN, myszka: $30.0, monitor: 399.00 Euro, podkładka: 39 zł
"""

# Zad 1.1
as1_1 = re.findall(r'\b\d+\b', text)
print("Assigment 1.1:\n", as1_1)
# Zad 1.2

as1_2 = re.findall(r'\b\d{2,}\b', text)
print("Assigment 1.2:\n", as1_2)

# Zad 1.3
as1_3 = re.findall(r'\b\d*00\d*\b', text)
print("Assigment 1.3:\n", as1_3)

# Zad 1.4
as1_4 = re.findall(r'\b[^\W\d_]+\b', text)
print("Assigment 1.4:\n", as1_4)

# Zad 2
pattern = re.compile(r'\D*(\d{2})\D*(\d{9})')

as2 = [match.groups() for number in tel if (match := pattern.match(re.sub(r'\D', '', number)))]
print("Assigment 2:\n", as2)

# Zad 3
as3 = re.findall(r'\d+(?:\.\d+)?', tekst)
print("Assigment 3:\n", as3)