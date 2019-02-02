# 'isinstance' - bult in function

class Box:

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height
        self.__private = 5

    def __del__(self):
        pass


a = Box('A', 1, 2, 3)

if isinstance(a, Box):
    print('a is an instance of the Box')
else:
    print('a is not instance of the Box')

if isinstance(a, str):
    print('a is a string instance')
else:
    print('a is not a string instance')