# Functions
# if statement and loops in fuctions

def odd_number(number):
    if number % 2 != 0:
        print(number, ' number is odd')
    else:
        print(number, ' number is even')


def range_odd_numbers(a, b):
    print('range of numbers is ', a, 'to b ', b)
    for num in range(a, b + 1):
        odd_number(num)

print(odd_number(43))

print(range_odd_numbers(1, 20))