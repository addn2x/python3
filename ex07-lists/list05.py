n = [2, 7, 5, 4, 3, 9, 1, 9, 3, 6, 8, 8, 9]
print('n: ', n)
print(' 5th element: ', n.index(9))
print(' 3rd element: ', n.index(3))

print(' 1st value of 9: ', n.index(9, 0))
print(' 1st value of 9: ', n.index(9, 6))


# count -> how many times value occures in a list
print('count of 9 ', n.count(9))

# reverse -> reverses original list
n.reverse()
print('n: ', n)

# sort -> accending order
n.sort()
print('n: ', n)

# join -> not a list, but a string method
