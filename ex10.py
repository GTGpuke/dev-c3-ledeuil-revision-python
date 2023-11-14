#Exercice 10: Tri par insertion : Implémentez l'algorithme de tri par insertion, la fonction prendra en paramètre une liste.

def tri_insertion(liste):
    #On parcours de la liste à partir du deuxième élément jusqu'à la fin.
    for i in range(1, len(liste)):
        #La clé est l'élément que nous allons insérer dans la partie triée de la liste.
        cle = liste[i]
        
        #Initialisation de l'index pour parcourir la partie triée de la liste.
        j = i - 1

        #Déplacement des éléments plus grands que la clé vers la droite.
        #pour faire de la place à la clé dans la partie triée.
        while j >= 0 and cle < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        
        #Insertion de la clé à la position correcte dans la partie triée de la liste.
        liste[j + 1] = cle

#Exemple d'utilisation:
result_liste = [12, 11, 13, 5, 6]
print("Liste avant le tri par insertion :", result_liste)

#Appel de la fonction de tri par insertion.
tri_insertion(result_liste)

print("Liste après le tri par insertion :", result_liste)