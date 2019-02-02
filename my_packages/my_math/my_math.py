pi = 3.1415926

def my_factoriel(n):
    fakt = 1
    for i in range(1, n + 1):
        fakt *= i
    return fakt