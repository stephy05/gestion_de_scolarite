"""
Module : Bulletin
Couche : Model (MVC)
Description : Gestion des données d'un bulletin scolaire
"""


class Matiere:
    """Représente une matière avec ses différentes notes."""

    def __init__(self, nom: str, cc: float = 0.0, tp: float = 0.0,
                 tpe: float = 0.0, examen: float = 0.0, coefficient: float = 1.0):
        self.nom = nom
        self.cc = cc          # Contrôle Continu
        self.tp = tp          # Travaux Pratiques
        self.tpe = tpe        # Travaux Personnels Encadrés
        self.examen = examen  # Note d'examen final
        self.coefficient = coefficient


    def calculer_moyenne_matiere(self) -> float:
        """
        Calcule la moyenne selon les 4 cas exacts :
        1. TP=5%, TPE=5%, CC=20%, Examen=70%
        2. TPE=10%, CC=20%, Examen=70%  (TP=0)
        3. CC=30%, Examen=70%           (TP=0, TPE=0)
        4. Examen=100%                  (CC=0, TP=0, TPE=0)
        """
        # Cas 4 : Examen seul
        if self.examen > 0 and self.cc == 0 and self.tp == 0 and self.tpe == 0:
            return round(self.examen, 2)

        # Cas 3 : CC + Examen seulement
        if self.cc > 0 and self.examen > 0 and self.tp == 0 and self.tpe == 0:
            moyenne = (self.cc * 0.30) + (self.examen * 0.70)
            return round(moyenne, 2)

        # Cas 2 : TPE + CC + Examen seulement
        if self.tpe > 0 and self.cc > 0 and self.examen > 0 and self.tp == 0:
            moyenne = (self.tpe * 0.10) + (self.cc * 0.20) + (self.examen * 0.70)
            return round(moyenne, 2)

        # Cas 1 : Cas complet par défaut
        moyenne = (self.cc * 0.20) + (self.tp * 0.05) + (self.tpe * 0.05) + (self.examen * 0.70)
        return round(moyenne, 2)

    def to_dict(self) -> dict:
        return {
            "nom": self.nom,
            "cc": self.cc,
            "tp": self.tp,
            "tpe": self.tpe,
            "examen": self.examen,
            "coefficient": self.coefficient,
            "moyenne": self.calculer_moyenne_matiere()
        }

    @staticmethod
    def from_dict(data: dict) -> "Matiere":
        return Matiere(
            nom=data["nom"],
            cc=data.get("cc", 0.0),
            tp=data.get("tp", 0.0),
            tpe=data.get("tpe", 0.0),
            examen=data.get("examen", 0.0),
            coefficient=data.get("coefficient", 1.0)
        )

    


class Bulletin:
    """Représente le bulletin scolaire d'un élève."""

    def __init__(self, id_bulletin: int, nom_eleve: str, prenom_eleve: str,
                 classe: str, annee_scolaire: str, semestre: int = 1):
        self.id_bulletin = id_bulletin
        self.nom_eleve = nom_eleve
        self.prenom_eleve = prenom_eleve
        self.classe = classe
        self.annee_scolaire = annee_scolaire
        self.semestre = semestre
        self.matieres: list[Matiere] = []
        self.appreciation: str = ""
        self.moyenne_generale: float = 0.0

    def ajouter_matiere(self, matiere: Matiere):
        """Ajoute une matière au bulletin."""
        self.matieres.append(matiere)
        self._recalculer_moyenne_generale()

    def modifier_matiere(self, nom_matiere: str, cc: float, tp: float,
                         tpe: float, examen: float):
        """Modifie les notes d'une matière existante."""
        for matiere in self.matieres:
            if matiere.nom == nom_matiere:
                matiere.cc = cc
                matiere.tp = tp
                matiere.tpe = tpe
                matiere.examen = examen
                break
        self._recalculer_moyenne_generale()

    def _recalculer_moyenne_generale(self):
        """Recalcule la moyenne générale pondérée de toutes les matières."""
        if not self.matieres:
            self.moyenne_generale = 0.0
            return

        total_points = sum(
            m.calculer_moyenne_matiere() * m.coefficient
            for m in self.matieres
        )
        total_coefficients = sum(m.coefficient for m in self.matieres)
        self.moyenne_generale = round(
            total_points / total_coefficients if total_coefficients > 0 else 0.0, 2
        )

    def get_mention(self) -> str:
        """Retourne la mention selon la moyenne générale."""
        if self.moyenne_generale >= 16:
            return "Très Bien"
        elif self.moyenne_generale >= 14:
            return "Bien"
        elif self.moyenne_generale >= 12:
            return "Assez Bien"
        elif self.moyenne_generale >= 10:
            return "Passable"
        else:
            return "Insuffisant"

    def nom_complet(self) -> str:
        return f"{self.prenom_eleve} {self.nom_eleve}"

    def to_dict(self) -> dict:
        return {
            "id_bulletin": self.id_bulletin,
            "nom_eleve": self.nom_eleve,
            "prenom_eleve": self.prenom_eleve,
            "classe": self.classe,
            "annee_scolaire": self.annee_scolaire,
            "semestre": self.semestre,
            "matieres": [m.to_dict() for m in self.matieres],
            "appreciation": self.appreciation,
            "moyenne_generale": self.moyenne_generale,
            "mention": self.get_mention()
        }

    @staticmethod
    def from_dict(data: dict) -> "Bulletin":
        b = Bulletin(
            id_bulletin=data["id_bulletin"],
            nom_eleve=data["nom_eleve"],
            prenom_eleve=data["prenom_eleve"],
            classe=data["classe"],
            annee_scolaire=data["annee_scolaire"],
            semestre=data.get("semestre", 1)
        )
        b.appreciation = data.get("appreciation", "")
        b.matieres = [Matiere.from_dict(m) for m in data.get("matieres", [])]
        b._recalculer_moyenne_generale()
        return b


class BulletinRepository:
    """
    Couche d'accès aux données pour les bulletins.
    (Simulation en mémoire — à remplacer par une vraie BDD)
    """

    def __init__(self):
        self._bulletins: dict[int, Bulletin] = {}
        self._next_id: int = 1

    def ajouter(self, bulletin: Bulletin) -> Bulletin:
        """Ajoute un nouveau bulletin et lui assigne un ID."""
        bulletin.id_bulletin = self._next_id
        self._bulletins[self._next_id] = bulletin
        self._next_id += 1
        return bulletin

    def modifier(self, bulletin: Bulletin) -> bool:
        """Met à jour un bulletin existant."""
        if bulletin.id_bulletin in self._bulletins:
            self._bulletins[bulletin.id_bulletin] = bulletin
            return True
        return False

    def supprimer(self, id_bulletin: int) -> bool:
        """Supprime un bulletin par son ID."""
        if id_bulletin in self._bulletins:
            del self._bulletins[id_bulletin]
            return True
        return False

    def get_par_id(self, id_bulletin: int) -> Bulletin | None:
        """Récupère un bulletin par son ID."""
        return self._bulletins.get(id_bulletin)

    def get_tous(self) -> list[Bulletin]:
        """Retourne la liste de tous les bulletins."""
        return list(self._bulletins.values())

    def get_par_eleve(self, nom: str, prenom: str) -> list[Bulletin]:
        """Retourne les bulletins d'un élève spécifique."""
        return [
            b for b in self._bulletins.values()
            if b.nom_eleve.lower() == nom.lower()
            and b.prenom_eleve.lower() == prenom.lower()
        ]
