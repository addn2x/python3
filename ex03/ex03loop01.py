
for i in range(0, 11):
    if i % 2 == 0:
        print(i, " is even number")
    else:
        print(i, " is odd number")
print("----------------------------")

mysum = 0
for i in range(1, 101):
    #mysum = mysum + i
    mysum += i
print("sum = ", mysum)
print("----------------------------")

#sum numbers odd/even form 1 to 20

print("----------------------------")

sumsqr = 0
for i in range(1, 10 + 1):
    #sumsqr = sumsqr + i **2
    sumsqr += i ** 2
print("sum of sqrs", sumsqr)
print("----------------------------")

initialsum = 10.0
first = 6
second = 9
for i in range(first, second + 1):
    #initialsum = initialsum + (1 / first ** 2)
    initialsum += (1 / first ** 2)
print("initialsum ", initialsum)
print("----------------------------")

myfakt = 1
for i in range(6, 0, -1):
    #myfakt = myfakt + i
    myfakt *= i
print("myfakt: ", myfakt)
print("----------------------------")

print(" task 10 (...(((x + a)^2 + a)^2 + a)^2 ... + a)^2")
task10_one = 1
task10_n = 3
task10_a = 1
task10_x = 3
task10_sum = task10_x

for i in range(task10_one, task10_n + 1):
    #task10_sum += a ** 2 ????????
    task10_sum = (task10_sum + task10_a) ** 2
    print(i)
print("task10_sum ", task10_sum)

