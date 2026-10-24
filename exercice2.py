
import json


# Classe mère
class Document:
    def __init__(self, titre, annee):
        self.titre = titre
        self.annee = annee

    def afficher(self):
        print(f"{self.titre} ({self.annee})")

    def est_recent(self):
        return self.annee >= 2020

    def vers_dict(self):
        return {
            "type": "Document",
            "titre": self.titre,
            "annee": self.annee
        }


# Classe Livre
class Livre(Document):
    def __init__(self, titre, annee, auteur):
        super().__init__(titre, annee)
        self.auteur = auteur

    def afficher(self):
        print(
            f"Livre: {self.titre} par {self.auteur} "
            f"({self.annee})"
        )

    def vers_dict(self):
        return {
            "type": "Livre",
            "titre": self.titre,
            "annee": self.annee,
            "auteur": self.auteur
        }


# Classe Magazine
class Magazine(Document):
    def __init__(self, titre, annee, numero):
        super().__init__(titre, annee)
        self.numero = numero

    def afficher(self):
        print(
            f"Magazine: {self.titre} No. {self.numero} "
            f"({self.annee})"
        )

    def vers_dict(self):
        return {
            "type": "Magazine",
            "titre": self.titre,
            "annee": self.annee,
            "numero": self.numero
        }


# Classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.documents = []

    def ajouter(self, document):
        self.documents.append(document)

    def afficher_tous(self):
        for document in self.documents:
            document.afficher()

    def rechercher(self, titre):
        resultats = []

        for document in self.documents:
            if titre.lower() in document.titre.lower():
                resultats.append(document)

        return resultats

    def enregistrer_json(self, nom_fichier):
        donnees = []

        for document in self.documents:
            donnees.append(document.vers_dict())

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            json.dump(
                donnees,
                fichier,
                ensure_ascii=False,
                indent=4
            )

        print(f"Documents enregistrés dans {nom_fichier}")


# Programme principal
if __name__ == "__main__":

    # Création de la bibliothèque
    biblio = Bibliotheque()

    # Ajout des documents
    biblio.ajouter(Livre("1984", 1949, "George Orwell"))
    biblio.ajouter(Magazine("Science & Vie", 2023, 456))
    biblio.ajouter(
        Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")
    )

    # 1. Afficher tous les documents
    print(" Tous les documents ")
    biblio.afficher_tous()

    # 2. Vérifier si les documents sont récents
    print("\n Documents récents ")
    for document in biblio.documents:
        if document.est_recent():
            document.afficher()

    # 3. Rechercher un document
    print("\n Recherche : Science ")
    resultats = biblio.rechercher("Science")

    if resultats:
        for document in resultats:
            document.afficher()
    else:
        print("Aucun document trouvé.")

    # 4. Enregistrer en JSON
    print("\n Enregistrement JSON ")
    biblio.enregistrer_json("bibliotheque.json")
