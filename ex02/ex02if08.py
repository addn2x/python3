
a = 31
b = 12
c = 4
d = 88

if a > b:
    maxvar = a
else:
    maxvar = b



if (a > b) and (a > c) and (a > d):
    maxvar = a
elif (b > c) and (b > d):
    maxvar = b
elif (c > d):
    maxvar = c
else:
    maxvar = d
    
print("max = ", maxvar)