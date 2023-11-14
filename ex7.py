#Exercice 7: Fichiers : Écrivez un programme qui lit un fichier texte, compte le nombre de mots et écrit le résultat dans un autre fichier.

#On ouvre le fichier "ex7_input.txt", contenant un Lorem Ipsum de 100 mots.
with open('ex7_input.txt', 'r') as input:
    #On lit le contenu du fichier.
    contenu = input.read()

#On sépare les mots.
mots = contenu.split()

#On compte les mots.
nb_mots = len(mots)

#On ouvre le fichier "ex7_output.txt".
with open('ex7_output.txt', 'w') as output:
    #On écrit le nombre de mots dans le fichier.
    output.write(str(nb_mots))
