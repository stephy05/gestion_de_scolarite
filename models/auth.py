from models.admin import Admin
from models.etudiant import Etudiant

class Authentification:
    def init(self):
        self.admins = []
        self.etudiants = []
        self.utilisateur_connecte = None

    def ajouter_admin(self, admin):
        self.admins.append(admin)

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def connecter(self, email, mot_de_passe):
        # Vérifier si c'est un admin
        for admin in self.admins:
            if admin.email == email and admin.mot_de_passe == mot_de_passe:
                self.utilisateur_connecte = admin
                admin.connecte = True
                print(f"Connecté en tant qu'Admin : {admin.prenom} {admin.nom}")
                return "admin"

        # Vérifier si c'est un étudiant
        for etudiant in self.etudiants:
            if etudiant.email == email and etudiant.mot_de_passe == mot_de_passe:
                self.utilisateur_connecte = etudiant
                print(f"Connecté en tant qu'Étudiant : {etudiant.prenom} {etudiant.nom}")
                return "etudiant"

        print("Email ou mot de passe incorrect.")
        return None

    def deconnecter(self):
        if self.utilisateur_connecte:
            print(f"Au revoir {self.utilisateur_connecte.prenom} !")
            self.utilisateur_connecte = None
        else:
            print("Aucun utilisateur connecté.")

    def est_connecte(self):
        return self.utilisateur_connecte is not None

    def est_admin(self):
        return isinstance(self.utilisateur_connecte, Admin)

    def str(self):
        if self.utilisateur_connecte:
            return f"Connecté : {self.utilisateur_connecte}"
        return "Aucun utilisateur connecté."