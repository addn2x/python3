class Box:

    __instance = 0

    def __init__(self, label, length, width, height):
        self.label = label
        self.length = length
        self.width = width
        self.height = height
        Box.__instance += 1
    
    def __del__(self):
        Box.__instance -= 1

    def __str__(self):
        return 'Box %d label %s length %d width %d height %d' % (Box.__instance, self.label, self.length, self.width, self.height)
