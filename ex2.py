#Exercice 2: Manipulation de chaînes : Demandez à l'utilisateur de saisir une phrase, puis affichez la phrase en majuscules, en minuscules et le nombre de mots.

#On demande à l'utilisateur de saisir une phrase.
phrase = input("Entrez une phrase : ")

#On convertit la phrase en majuscules et en minuscules.
majuscules = phrase.upper()
minuscules = phrase.lower()

#On compte le nombre de mots dans la phrase.
mots = phrase.split()
nombre_mots = len(mots)

#On affiche les résultats.
print("Phrase en majuscules : ", majuscules)
print("Phrase en minuscules : ", minuscules)
print("Nombre de mots : ", nombre_mots)
