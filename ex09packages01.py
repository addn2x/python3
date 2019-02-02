from my_packages.my_math.my_math import pi, my_factoriel

from my_packages.my_class.my_box.Box import Box

from my_packages.my_class.my_employee.Employee import Employee, Person


print(pi)
print(my_factoriel(4))

b = Box('My Box', 1, 2, 3)
print(b)

p = Person('Q', 'W', 32)
print(p)

e = Employee('A', 'B', 21, 'Admin')
print(e)
