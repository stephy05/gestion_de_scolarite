class Etudiant:
    def __init__(self, id_etudiant, nom, prenom):
        self.id_etudiant = id_etudiant
        self.nom = nom
        self.prenom = prenom
        self.cours_inscrits = []  # liste des cours où l'étudiant est inscrit

    def inscrire_cours(self, cours):
        if cours not in self.cours_inscrits:
            self.cours_inscrits.append(cours)
            cours.ajouter_etudiant(self)  # on met à jour des 2 côtés

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Cours:
    def __init__(self, id_cours, titre):
        self.id_cours = id_cours
        self.titre = titre
        self.etudiants_inscrits = []  # liste des étudiants inscrits

    def ajouter_etudiant(self, etudiant):
        if etudiant not in self.etudiants_inscrits:
            self.etudiants_inscrits.append(etudiant)

    def __str__(self):
        return self.titre

class GestionInscription:
    def __init__(self):
        self.etudiants = []
        self.cours = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def ajouter_cours(self, cours):
        self.cours.append(cours)

    def afficher_etudiants_dun_cours(self, id_cours):
        for c in self.cours:
            if c.id_cours == id_cours:
                print(f"Étudiants inscrits à {c.titre} :")
                for e in c.etudiants_inscrits:
                    print(f" - {e}")
                return
        print("Cours introuvable")

    def afficher_cours_dun_etudiant(self, id_etudiant):
        for e in self.etudiants:
            if e.id_etudiant == id_etudiant:
                print(f"Cours de {e} :")
                for c in e.cours_inscrits:
                    print(f" - {c}")
                return
        print("Étudiant introuvable")

    def afficher_tous_les_inscrits(self):
        for e in self.etudiants:
            if e.cours_inscrits:
                print(f"{e} est inscrit à : {[c.titre for c in e.cours_inscrits]}")
