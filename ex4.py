#Exercice 4: Listes : Créez une liste de 10 nombres, trouvez le maximum, le minimum, et calculez la moyenne.

#Voici liste de 10 nombres.
numbers = [2, 5, 8, 10, 15, 20, 25, 30, 35, 40]

#On trouve le maximum.
maximum = max(numbers)
print("Le maximum est :", maximum)

#On trouve le minimum.
minimum = min(numbers)
print("Le minimum est :", minimum)

#On calcule la moyenne.
average = sum(numbers) / len(numbers)
print("La moyenne est :", average)