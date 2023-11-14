#Exercice 9: Compréhension de liste : Utilisez la compréhension de liste de 10 éléments dans laquelle il faudra calculer le nombre élevé au carré de chaque élément

#Initialisation de la liste de nombres.
liste = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#On passe la liste au carré.
liste_carre = [x**2 for x in liste]

#Affichage des résultats.
print(liste_carre)
