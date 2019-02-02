r = range(1, 10)
n = list(r)

custom = []
for i in n:
    custom.append(i * 2)
print('custom : ', custom)

double = [i * 2 for i in n]
print('double: ', double)


even = [i for i in n if (i % 2 == 0)]
odd = [i for i in n if (i % 2 != 0)]

print('even: ', even)
print('odd: ', odd)