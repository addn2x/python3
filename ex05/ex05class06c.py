# 'hasattr' built in function
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

print('Box instance a has a label attribute: ', hasattr(a, 'label'))
print('Box instance a has a length attribute: ', hasattr(a, 'length'))
print('Box instance a has a width attribute: ', hasattr(a, 'width'))
print('Box instance a has a height attribute: ', hasattr(a, 'height'))
print('Box instance a has a __private attribute: ', hasattr(a, '__private'))