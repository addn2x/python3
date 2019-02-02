# Each method within a class takes instance of itself as a
# first parametar / self
# It's needed so we can access it's class fields

class Box:

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def info(self):
        return "Box: %s, length = %d, width = %d, height = %d " % (self.label, self.length, self.width, self.height)


b01 = Box("First", 50, 30, 20)
b02 = Box("Second", 30, 20, 10)

#print("Box: ", b01.label, " length = ", b01.length, " width = ", b01.width, " height = ", b01.height)

#print("Box: ", b02.label, " length = ", b02.length, " width = ", b02.width, " height = ", b02.height)

print(b01.info())
# print(Box.info(b01))

print(b02.info())
# print(Box.info(b02))

b03 = Box("Third", 1, 2, 3)
b03.height = 7
print(b03.info())
