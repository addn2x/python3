# Fuctions 

# factoriel exmple
#   5! = 5 * 4 * 3 * 2 * 1

# sum of factoriel example
#   sum = 5! + 4! + 3! + 2! + 1!

def my_fakt(n):
    fakt = 1
    for i in range(1, n + 1):
        fakt *= i
    return fakt

def fact_sum(n):
    my_sum = 0
    for i in range(1, n + 1):
        my_sum += my_fakt(i)
    return my_sum


print(my_fakt(5))
print(fact_sum(5))