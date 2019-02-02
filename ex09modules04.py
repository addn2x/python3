# Modules

from math import e, pi, factorial
from random import random, uniform, randrange, choice


# print(dir(math))

print(e)
print(pi)
print(factorial(6))

print(random()) # Random float:  0.0 <= x < 1.0
print(uniform(2.5, 10.0)) # Random float:  2.5 <= x < 10.0
print(randrange(10)) # Integer from 0 to 9 inclusive
print(randrange(0, 101, 2)) # Even integer from 0 to 100 inclusive
print(choice(['win', 'lose', 'draw'])) # Single random element from a sequence