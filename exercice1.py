class Employe:
    def __init__(self, nom, salaire_base):
        self.nom = nom
        self.salaire_base = salaire_base

    def salaire_total(self):
        return self.salaire_base

    def __str__(self):
        return f"{self.nom} gagne {self.salaire_total()} €"

class Manager(Employe):
    def __init__(self, nom, salaire_base, prime):
        super().__init__(nom, salaire_base)
        self.prime = prime

    def salaire_total(self):
        return self.salaire_base + self.prime

class Developpeur(Employe):
    def __init__(self, nom, salaire_base, technologie):
        super().__init__(nom, salaire_base)
        self.technologie = technologie

    def salaire_total(self):
        bonus = 500 if self.technologie == 'Python' else 300
        return self.salaire_base + bonus
if __name__ == '__main__':
    e = Employe("Alice", 2000)
    m = Manager("Bob", 2500, 800)
    d = Developpeur("Charlie", 2200, "Python")

    for personne in [e, m, d]:
        print(personne)   