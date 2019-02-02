# Private methods

class Box:

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height
        self.__private = 5

    def __del__(self):
        pass
    
    def __private_method(self):
        return 'This is private method'

o = Box("A", 3, 4, 5)

# print(o.__private)
# print(o.__private_method)

print(dir(o))

print(o._Box__private)
o._Box__private = 6
print(o._Box__private)

print(o._Box__private_method())