# store values in a sequence

a = []
b = [4, 7, 2, 9]
c = [1.3, 5.2, 4.0, 1.45]
d = [True, False, False, True, True]
e = ['a', 'bc', 'abc', 'some text']
f = [1, 2, 3, [4, 5, 6]]
mix = ['a', False, 1.54, 6, True, 'some text']

print('b[0] = %d\nb[1] = %d\nb[2] = %d\nb[3] = %d\n' % (b[0], b[1], b[2], b[3]))

for i in range(len(b)):
    print('b[%d] = %d' % (i, b[i]))

print()
print(b)

print('first slice: ', mix[2:4])
print(mix[:4])

e.append('appended text')
print(e)

print(max(b))
print(sum(c))
# print(min(f)) Error