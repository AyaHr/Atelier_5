class Vecteur2D:
    def __init__(self, x0=0, y0=0):

        self.x = x0
        self.y = y0

    def __str__(self):
        return "x = %d, y = %d" % (self.x, self.y)


# Auto-test
if __name__ == '__main__':
    print("Une instance par defaut ")
    print (Vecteur2D())
    print("Une instance initialisee ")
    print (Vecteur2D(-2.2, 5.3))
