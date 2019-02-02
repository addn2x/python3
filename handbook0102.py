# Comparing Strings

str01 = 'a'
str02 = 'A'

str03 = 'ABC'
str04 = 'abc'

str05 = 'z'
str06 = 'A'

str07 = 'Hello'
str08 = 'everyone'

a = str01
b = str02

if a == b:
    print('Strings are equal')
elif a > b:
    print('a %s is greater than b %s', % (a, b))
elif a < b:
    print('a is lower than b')

if a != b:
    print('Strings are not equal')
