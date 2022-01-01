class Rectangle:
    def __init__(self, lon=2, lar=3, nom="rectangle"):
        self.lon = lon
        self.lar = lar
        self.nom = nom

    def surface(self):
        return self.lon*self.lar

    def afficher(self):
        print("Le {0} de longeur {1} et de largeure {2} a une surface de {3}".format(
            self.nom, self.lon, self.lar, self.surface()))


class Carre(Rectangle):
    def __init__(self, cote=6):
        Rectangle.__init__(self, cote, cote)
        self.nom = "carre"


"""Le programme principal"""
rec = Rectangle()
rec.afficher()
car = Carre()
car.afficher()
