a = 'this is some string'
b = "this is also a string"
c = 'Paul said "Hello everyone"'

print(a, type(a))
print(b, type(b))
print(c, type(c))

print('remove first 3 characters form string a:', a[3:])
print('remove all but first characters form stirng a:', a[:1])
print('remove all but last four characters form stirng a:',a[-4:])
print('all characters from position six to position nine from sting a:', a[5:9])

d = a[0:8] + c[0:4]
print(d)

print('a' > 'A') # in ASCII a = 97, A = 65
print('m' < 'A')
print('maxi' < 'mini')
print('ABC' == 'abc')
print('******************************************')
print('a' in 'abc')
print('a' in 'ABC')
print('an' in 'banana')
print('first' in 'second')
print('this' in 'this is string, this is great')