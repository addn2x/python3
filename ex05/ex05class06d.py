# 'getattr' built in function
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
print('a.length: ', getattr(a, 'length'))
print('a.width: ', getattr(a, 'width'))
print('a.height: ', getattr(a, 'height'))
#print('a.__private: ', getattr(a, '__private'))