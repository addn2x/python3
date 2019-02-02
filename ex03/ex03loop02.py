
zero = 0
one = 1

t11_n = 2
t11_m = 4
t11_p = one
for i in range(zero, t11_m + one):
    t11_p = t11_p * (t11_n + i * t11_m)
print(t11_p)
print("---------------------------")

sign = 1
t11_pb = 1

for i in range(one, t11_m + one):
    t11_pb = t11_pb * (t11_n + sign * i * t11_m)
    sign = -sign
print(t11_pb)
print("---------------------------")

sign = 1
t11_pc = 0.0
for i in range(one, t11_m):
    t11_pc = sign * (1 / (t11_n + i * t11_m))
    sign = -sign
print(t11_pc)