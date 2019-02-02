# Dynamically Created Attributes


class Box:

    def __init__(self):
        pass

b1 = Box()
b2 = Box()

b1.label = "First"
b1.length = 3
b1.width = 2
b1.height = 1

b2.label = "Second"
b2.length = 4
b2.width = 5
b2.height = 6

class Person:
    pass


p01 = Person()
p02 = Person()

p01.first = "Adam"
p01.last = "Benson"
p01.email = "a.benson@mail.com"

p02.first = "Alice"
p02.last = "Brown"
p02.email = "a.brown@mail.com"
