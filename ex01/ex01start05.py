#  Three points in the same line (linear function)
#  The independent variable is x and the dependent variable is y.

x1 = 5.0
y1 = 11.0

x2 = -0.5
y2 = 0.0

x3 = 1.0
y3 = 3.0

k = 2.0
n = 1.0

result = (y1 == k * x1 + n) and (y2 == k * x2 + n) and (y3 == k * x3 + n)

print('Result ', result)
