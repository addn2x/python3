#lint:enable
#lint:disable

import math

one = 1

product01 = 1.0
n01 = 5

for i in range(one, n01 + one):
    sumcos01 = 0.0
    sumsin01 = 0.0
    for j in range(one, i + one):
        sumcos01 += math.cos(j)
        sumsin01 += math.sin(j)
    product01 *= (sumcos01 / sumsin01)
print("product01 ", product01)  # lint:ok
print("---------------------------")

print(" S = 3! - 6! + 9! + .. + (-1)^(n+1) * (3n)! ")

sum02 = 0
n02 = 5

for i in range(one, n02 + one):
    sign = 1
    for k in range(one, i + one + one):
        sign = (-sign) ** k
        # math.pow(-sign, k)
    print(sign)
    tmpn = 3 * i
    fakt = 1
    for j in range(one, tmpn + one):
        fakt *= j
    sum02 += sign * fakt
print("sum02: ",sum02)  # lint:ok
print("---------------------------")

sum03 = 0
n03 = 3

for i in range(one, n03 + one):
    tmpI = i + one
    p = 1
    for j in range(i, tmpI + one):
        p *= j
    sum03 += p
print("sum03 ", sum03)
