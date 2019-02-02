

zero = 0
one = 1

faktSum = 0
t13_n = 5

for i in range(one, t13_n + one):
    fakt = 1
    for j in range(one, i + one):
        fakt *= j
    faktSum += fakt

print("faktSum = ", faktSum)
print("---------------------------")

t14a_sum = 0.0
t14a_n = 2

for i in range(one, t14a_n + one):
    fakt = 1.0
    t14a_tmpSum = 0.0
    for j in range(one, i + one):
        fakt *= j
        t14a_tmpSum += 1 / (j + 1)
    t14a_sum += fakt / t14a_tmpSum
print("t14ab_sum = ", t14a_sum)
print("---------------------------")

t14c_sum = 0.0
t14c_n = 3
sign = 1
for i in range(one, t14c_n + one):
    fakt = 1.0
    t14c_tmpSum = 0.0
    for j in range(one, i + one):
        fakt *= j
        t14c_tmpSum += j
    t14c_sum += sign * (t14c_tmpSum / fakt)
    sign = -sign
print("t14c_sum = ", t14c_sum)
print("---------------------------")