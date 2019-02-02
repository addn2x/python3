# print()

r = range(2, 10)
n = list(r)

# clear -> Will remove all items from the list

c = list(r)
print('c: ', c)
print('c: ', c.clear())

# pop -> returns poped item
# if index is not passed than last item will be returned

p = list(r)
print('p: ', p)
print('p: ', p.pop())
print('p: ', p.pop(3))

# remove -> remove first mach of passed value
# ValueError if item is not found

r = [2, 7, 4, 4, 3, 9, 9, 9]
print('r: ', r)
r.remove(4)
print('r: ', r)
r.remove(9)
print('r: ', r)