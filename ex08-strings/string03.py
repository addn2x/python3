a = 'This is some text'
b = '123456'

print(a.find('is'))
print(a.find('other'))

print(a.isalpha())
print(a.isdigit())

print(b.isalpha())
print(b.isdigit())

print(a.upper())
print(a.lower())

print(a.split())

print(a.join(b))
print(a + b)

print(a.replace('is', 'was'))