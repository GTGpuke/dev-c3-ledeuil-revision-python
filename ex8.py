#Exercice 8: Dictionnaires : Créez un dictionnaire avec des noms d'élèves et leurs notes. Trouvez l'élève avec la meilleure note.


#On crée un dictionnaire avec les noms et les notes des étudiants.
notes_des_etudiants = {
    "Alice Martin": 18,
    "Bob Johnson": 15,
    "Charlie Dubois": 7,
    "David Leroux": 14,
    "Émilie Davis": 19,
    "Alice Martin": 20  #Ajout d'un homonyme avec une note différente, pour le test.
}

#Fonction pour traiter les homonymes.
def gerer_homonymes(nom, dictionnaire):
    suffixe = 1
    while nom in dictionnaire:
        nom = f"{nom} ({suffixe})"
        suffixe += 1
    return nom

#On traite les homonymes.
nouveau_dictionnaire = {}
for nom, note in notes_des_etudiants.items():
    nom_unique = gerer_homonymes(nom, nouveau_dictionnaire)
    nouveau_dictionnaire[nom_unique] = note

#On trouve l'étudiant avec la meilleure note.
meilleur_etudiant = max(nouveau_dictionnaire, key=nouveau_dictionnaire.get)

print("L'étudiant avec la meilleure note est : ",meilleur_etudiant)