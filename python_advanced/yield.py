"""Generator yield służy do generowania iteratywnie wyników, zamiast prztrzymywania całej operacji i na końcu jej
    wywoływania, co służy pomocnie przy dużych zbiorach danych, nie obciążając wtedy jej pamięci aż tak"""


def fun(m: int) -> list:
    for i in range(m):
        yield i # Produces values one at a time

print(fun(5))

for i in fun(5):
    print(i)

"""
Difference between return and yield in Python
The yield keyword in Python is similar to the return statement in that both are used for returning values. However,
there are some key differences:

Feature                 return                              yield
Execution               Terminates function execution	    Pauses execution and maintains state
Memory Efficiency	    Stores entire result in memory	    Uses lazy evaluation, saving memory
Resumption	Function    does not retain its state	        Function resumes execution after yield
"""

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
for _ in range(10):
    print(next(gen), end=" ")