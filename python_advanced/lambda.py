"""
Funkcja Lambda w Pythonie jest anonimowa czyli funkcja nie posiada nazwy i jest tworzona w jednej linii,
jak wiemy def służy do definiowania funkcji w Pythonie. Podobnie lambda służy do definiowania anonimowej funkcji.
"""

s1 = 'Kamil Jarzyn'
s2 = lambda func: func.upper()
print(s2(s1))

"""Syntax funkcji lambdy:
lambda arguments: expression
arguments – argumenty funkcji, które są przekazywane do niej.
expression – wyrażenie, które jest wykonywane i zwracane przez funkcję.

lambda: The keyword to define the function.
arguments: A comma-separated list of input parameters (like in a regular function).
expression: A single expression that is evaluated and returned."""

"""Możemy używać lambdy do instrukcji warunkowej"""
# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

""" Difference Between lambda and def Keyword
Lambda jest zwięzła ale mnie potężna niżeli def w baedziej skomplikowanej logice

Feature	        lambda Function	                        Regular Function (def)
Definition	    Single expression with lambda.	        Multiple lines of code.
Name	        Anonymous (or named if assigned).	    Must have a name.
Statements	    Single expression only.	                Can include multiple statements.
Documentation	Cannot have a docstring.	            Can include docstrings.
Reusability	    Best for short, temporary functions.	Better for reusable and complex logic.
"""
s= lambda x: x ** 2
print(s(3))

"""Lambde możemy używać z List Comprehension"""
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

"""
The lambda function squares each element.
The list comprehension.py iterates through li and applies the lambda to each element.
This is ideal for applying transformations to datasets in data preprocessing or manipulation tasks."""

"""Lambda z wielokrotnymi instrukcjami"""
calc = lambda x, y: (x + y, x * y)
res = calc(3,4)
print(res)