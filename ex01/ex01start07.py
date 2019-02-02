# Exchange value between two variables
# without using any other variables

a = -3
b = 5

print('a = ', a, 'b = ',b)

a = a - b
b = b + a
a = b - a

print('a = ', a, 'b = ',b)
