
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8]

print('Odd type: ', type(odd))

print('Odd numbers: ', odd )
print('Even numbers: ', even )

print('Odd lenght: ', odd.__len__())
print('Even length: ', len(even))

nubers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10)
n = list(r)

print('n: ', n)

# First index has value of 0

print('Odd index 1: ', odd[1] )
print('Odd index 2: ', odd[2] )
print('Odd index 4: ', odd[4] )

print('Even index 0: ', even[0] )
print('Even index 3: ', even[3] )

six = 6

isInList = six in odd
print(isInList)


isInList = six in even
print(isInList)

# First backwards index has value of -1

print('Even index 0: ', even[-1] )
print('Even index 3: ', even[-3] )