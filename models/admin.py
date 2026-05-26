class Admin:
    def init(self, nom, prenom, email, mot_de_passe):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.connecte = False

    # --- AUTHENTIFICATION ---
    def connecter(self, mot_de_passe):
        if mot_de_passe == self.mot_de_passe:
            self.connecte = True
            print(f"Bienvenue {self.prenom} {self.nom} !")
        else:
            print("Mot de passe incorrect.")

    def deconnecter(self):
        self.connecte = False
        print("Déconnexion réussie.")

    # --- GESTION ÉTUDIANTS ---
    def afficher_etudiants(self, liste_etudiants):
        if not liste_etudiants:
            print("Aucun étudiant enregistré.")
        for etudiant in liste_etudiants:
            print(etudiant)

    def ajouter_etudiant(self, liste_etudiants, etudiant):
        liste_etudiants.append(etudiant)
        print(f"Étudiant {etudiant.prenom} {etudiant.nom} ajouté.")

    def modifier_etudiant(self, etudiant, nom=None, prenom=None, email=None):
        if nom:
            etudiant.nom = nom
        if prenom:
            etudiant.prenom = prenom
        if email:
            etudiant.email = email
        print(f"Étudiant {etudiant.matricule} modifié.")

    def supprimer_etudiant(self, liste_etudiants, matricule):
        for e in liste_etudiants:
            if e.matricule == matricule:
                liste_etudiants.remove(e)
                print(f"Étudiant {matricule} supprimé.")
                return
        print("Étudiant introuvable.")

    # --- GESTION NOTES ---
    def afficher_notes(self, etudiant):
        if not etudiant.notes:
            print(f"Aucune note pour {etudiant.prenom} {etudiant.nom}.")
        for cours, note in etudiant.notes.items():
            print(f"  {cours} : {note}/20")

    def ajouter_note(self, etudiant, cours, note):
        etudiant.notes[cours] = note
        print(f"Note {note}/20 ajoutée pour {etudiant.prenom} en {cours}.")

    def modifier_note(self, etudiant, cours, nouvelle_note):
        if cours in etudiant.notes:
            etudiant.notes[cours] = nouvelle_note
            print(f"Note de {cours} modifiée à {nouvelle_note}/20.")
        else:
            print(f"Cours {cours} introuvable.")

    def supprimer_note(self, etudiant, cours):
        if cours in etudiant.notes:
            del etudiant.notes[cours]
            print(f"Note de {cours} supprimée.")
        else:
            print(f"Cours {cours} introuvable.")

    # --- BULLETINS ---
    def afficher_bulletin(self, etudiant):
        print(f"\n===== BULLETIN DE {etudiant.prenom} {etudiant.nom} =====")
        print(f"Matricule : {etudiant.matricule}")
        for cours, note in etudiant.notes.items():
            print(f"  {cours} : {note}/20")
        print(f"Moyenne : {etudiant.calculer_moyenne():.2f}/20")
        print(f"Mention : {etudiant.obtenir_mention()}")
        print("=" * 40)

    def generer_bulletin(self, etudiant):
        bulletin = {
            "matricule": etudiant.matricule,
            "nom": f"{etudiant.prenom} {etudiant.nom}",
            "notes": etudiant.notes,
            "moyenne": etudiant.calculer_moyenne(),
            "mention": etudiant.obtenir_mention()
        }
        print(f"Bulletin généré pour {etudiant.prenom} {etudiant.nom}.")
        return bulletin

    def modifier_bulletin(self, etudiant, cours, nouvelle_note):
        self.modifier_note(etudiant, cours, nouvelle_note)
        print("Bulletin mis à jour.")

    def str(self):
        return f"Admin : {self.prenom} {self.nom} ({self.email})"