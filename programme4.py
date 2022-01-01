class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:

    def __init__(self, origiX, origY, extremX, extremY):
        self.origin = Point(origiX, origY)
        self.extreme = Point(extremX, extremY)

    def printSegment(self):
        print("Origin: ({0},{1})".format(self.origin.x, self.origin.y))
        print("Extremite : ({0},{1})".format(self.extreme.x, self.extreme.y))


# creation d'un instance
mySegment = Segment(1, 2, 3, 4)
mySegment.printSegment()
