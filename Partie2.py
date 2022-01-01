class Etudiant:
    """defintion du class"""

    def __init__(self, nom, prenom, age, cne, moyenne):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


etudiantsList = [Etudiant("Aya", "Harfouch", 21, "P148024707", 14),
                 Etudiant("Mounia", "Zaid", 21, "P148024706", 13),
                 Etudiant("Safae", "Hajjaj", 22, "P13090878", 12.5),
                 Etudiant("Taoufiq", "Amin", 25, "P143565378", 11),
                 Etudiant("Sanae", "Mourad", 23, "P130344878", 10.5)]


def sortByAge(etudiant):
    return etudiant.age


etudiantsList.sort(key=sortByAge)

print("Liste ordonner selon l'age".center(50, '='))
for etudiant in etudiantsList:
    print(etudiant.nom)
    print(etudiant.prenom)
    print(etudiant.age)
    print("---------")


def sortByAverage(student):
    return student.moyenne


etudiantsList.sort(key=sortByAverage)

print("Liste ordonner selon la moyenne ".center(50, '='))
for student in etudiantsList:
    print(student.nom)
    print(student.prenom)
    print(student.moyenne)
    print("---------")
