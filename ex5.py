#Exercice 5: Fonctions : Écrivez une fonction qui calcule le factoriel d'un nombre.

#Fonction factoriel de n.
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

#Initialisation des variables.
nombre = input("Rentrez un nombre : ")
print(factoriel(nombre))