# Functions
# that return value


def my_sum(a, b):
    return a + b

def my_sqr(n):
    return n ** 2

def my_sqr_sum(n):
    tsum = 0
    for i in range(1, n + 1):
        tsum += my_sqr(i)
    return tsum

print("sum of sqrs ", my_sqr_sum(5)) 

# my_sum_variable = my_sqr_sum(5)
# print("sum of sqrs ", my_sum_variable) 