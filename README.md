## Module Bulletin - Gestion des notes et des bulletins 

### Ce qui a été ajouté
Implémentation des classes `Matiere` et `Bulletin` pour gérer les notes et calculer les moyennes.

### Fonctionnement

Classe `Matiere`
- Stocke les notes : CC, TP, TPE, Examen
- Calcule la moyenne selon 4 cas :
 1. *Cas complet* : TP 5% + TPE 5% + CC 20% + Examen 70%
 2. *Sans TP* : TPE 10% + CC 20% + Examen 70%
 3. *Sans TP/TPE* : CC 30% + Examen 70%
 4. *Examen seul* : Examen 100%

Si une note est à 0, son poids est ignoré et redistribué automatiquement.

 Classe `Bulletin`
- Gère la liste des matières d'un élève
- Calcule la moyenne générale pondérée par coefficient
- Attribue la mention : Très Bien, Bien, Assez Bien, Passable, Insuffisant

 Classe `BulletinRepository`
- CRUD en mémoire pour les bulletins
- Elle sera utilisée comme notre DATABASE

### Exemple d'utilisation
```python
maths = Matiere("Maths", cc=15, tp=0, tpe=12, examen=14, credits =3)
bulletin = Bulletin(1, "Kone", "Awa", "tic l2", "2024-2025")
bulletin.ajouter_matiere(maths)
print(bulletin.moyenne_generale) # Moyenne calculée auto
```
pour calculer la moyenne générale nous faisons la moyenne obtenu par matière fois le nombre de crédits 
