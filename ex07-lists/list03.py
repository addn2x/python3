
r = range(1, 10)
n = list(r)

print('n type: ', type(n))
print('n: ', n)

for i in n:
    print('i: ', i)

# for i in n:
#     if (i % 2 == 0):
#         print('odd: ', i)

# for i in n:
#     if (i >= 5) and (i % 2 == 0):
#         print('numbers >= 5: ', i)

# append -> Add an item (object) to the end of the list
n.append(12)
print('n: ', n)

# extend -> Add to the end of a list all values passed to extend
n.extend([23, 41, 11])
print('n: ', n)

#insert -> Insert an item (object) at a given position
# n.insert(index, value)
n.insert(4, 98)
print('n: ', n)

# insert the last item
# n.insert(len(n), value)