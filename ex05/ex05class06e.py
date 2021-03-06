# 'setattr' built in function
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

print('a.label : ', getattr(a, 'label'))
setattr(a, 'label', 'B')

print('a.label : ', getattr(a, 'label'))
delattr(a, 'label')

print('a.label : ', getattr(a, 'label'))