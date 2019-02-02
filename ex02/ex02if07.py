
n = -23

even = n % 2 == 0 # even can be True or False
odd = not even

positive = n > 0
negative = not positive

if even:
    print ("n is even")
else:
    print ("n is odd")
print()

if positive:
    print ("n is positive")
else:
    print ("n is negative")
print()
