# Concatenating Strings

a = 'Hello'
space = ' '
b = 'everyone'
c = a + space + b

print(c) # print(a + space + b)

d = c + space

print(d * 3)

number = 65
#print(d + number) #TypeError: Can't convert 'int' object to str implicitly
print(d + str(number))
