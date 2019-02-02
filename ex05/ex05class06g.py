# Class documentation

class Box:

    'This is class documentation for Box class'

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def __del__(self):
        print(self.__class__.__name__, self.label, 'destroyed')

    def __repr__(self):
        # Meant for debug and log
        return "Box('{}', '{}', '{}', '{}')". format(self.label, self.length, self.width, self.height)

    def __str__(self):
        return "Box - '{}' '{}' '{}' '{}' ". format(self.label, self.length, self.width, self.height)
    
a = Box('A', 1, 2, 3)

print(a)