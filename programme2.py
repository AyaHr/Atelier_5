class Vecteur2D():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def Vector1(self):
        print('v1 = ({1},{0})'.format(self.x, self.y))

    def Vector2(self):
        print('v2 = ({0},{1})'.format(self.x, self.y))

    def Vector(self):
        print('v1 + v2 = ({0},{1})'.format(self.x, self.y))

    def __add__(self, other):
        result = Vecteur2D(self.x+other.x, self.y+other.y)
        return result


v1 = Vecteur2D(2, 3)
v2 = Vecteur2D(11, -6)

v1.Vector1()
v2.Vector2()

somme = v1 + v2
somme.Vector()
