import re

text = """
Adam Malinowski
.gitignore
2023-01-17 error "Page not found"
[2025-03-06] NOTICE "User admin logged in"
Code 3300 was invalid
https://www.onet.pl 200 176353
File /etc/passwd: permission denied
Józef
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

# Zad 1
as1 = re.findall('^[A-Z].*',text, flags=re.MULTILINE)

# Zad 2
# as2 = re.finditer('[0-9]',text,flags=re.MULTILINE)
# for figure in as2:
#     print(figure)

as2 = re.findall(r'\S*\d\S*', text)

# Zad 3
as3 = re.findall(r'^.*\..*$', text, re.MULTILINE)

# Zad 4
as4 = re.findall(r'\b\d{3,}\b', text)

# Zad 5
as5 = [line for line in text.splitlines() if re.search(r'\b\d{3,}\b', line)]

# Zad 6
as6 = [line for line in text.splitlines() if re.fullmatch(r'[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+', line)]

# Zad 7
as7 = [line for line in text.splitlines() if re.fullmatch(r'\d+', line)]

# Zad 8
as8 = re.findall(r'\b(?:in)?valid\b', text)

# Zad 9
as9 = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)

# Zad 10
as10 = re.findall(r'/\S*/\S*', text)

# Zad 11
as11 = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)

# Zad 12
as12 = re.findall(r'"([^"]+)"', text)

# Zad 13
as13 = [line for line in text.splitlines() if len(line) == 4]

print("1", as1)
print("2", as2)
print("3", as3)
print("4", as4)
print("5", as5)
print("6", as6)
print("7", as7)
print("8", as8)
print("9", as9)
print("10", as10)
print("11", as11)
print("12", as12)
print("13", as13)