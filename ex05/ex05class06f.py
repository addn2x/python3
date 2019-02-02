# Class documentation

class Box:

    'This is class documentation for Box class'

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height
        self.__private = 5

    def __del__(self):
        print(self.__class__.__name__, self.label, 'destroyed')

a = Box('A', 1, 2, 3)

print(Box.__sizeof__)
print('Class documentation: ', Box.__doc__)
print('Class name: ', Box.__name__)
print('Class module: ', Box.__module__)
print('Class dictionary: ', Box.__dict__)

print(hasattr(Box, '__doc__'))
print(hasattr(Box, '__name__'))

setattr(Box, '__name__', 'ASD')
print(Box.__name__)