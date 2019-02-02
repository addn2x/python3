# bool value of result is true
#     if given values a, b, c are
#     a) all equal 
#     b) all even numbers

true = True
false = False

print('true', true)
print('false', false)
print()

a = 2
b = 5
c = 2

resultA = (a == b) and (a == c) and (b == c)
resultB = ((a % 2) == 0) and ((b % 2) == 0) and ((c % 2) == 0)

print('A = ', resultA, type(resultA), 'B = ', resultB, type(resultB))
