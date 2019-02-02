# Static field
# to access static field class name is used
# with "dot" (access operator) and static field's name 

class Box:

    box_number = 0 # Static field

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height
        #
        #self.number_of_box += 1
        #print("Box %d is created" % (self.number_of_box))
        #
        Box.box_number += 1 
        print("Box %d is created" % (Box.box_number))


    def __del__(self):
        print("Box %d deleted" % (Box.box_number))
        Box.box_number -= 1

    def info(self):
        return "Box: %s, length = %d, width = %d, height = %d" % (self.label, self.length, self.width, self.height)

###############################################################################

b01 = Box("First", 50, 30, 20)
print(Box.box_number)
b02 = Box("Second", 30, 20, 10)
print(Box.box_number)

#Box.box_number = 22

print(b01.info())
print(b02.info())

b03 = Box("Third", 1, 2, 3)
b03.height = 7
print(Box.box_number)
print(b03.info())

#Box.box_number = 22 vs b01.box_number = 11 ???