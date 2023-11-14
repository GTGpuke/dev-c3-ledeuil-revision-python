#Exercice 3: Calculatrice simple : Écrivez un programme qui prend une chaine de caractère et effectue les opérations de base : addition, soustraction, multiplication, division.
import re

def evaluate_expression(expression):
    #Utilisation d'une expression régulière pour diviser la chaîne en nombres et opérations.
    elements = re.findall(r'(\d+|\D)', expression)

    #Initialisation du résultat avec le premier nombre.
    result = float(elements[0])

    #Parcours des éléments de la chaîne à partir du deuxième élément.
    for i in range(2, len(elements), 2):
        operator = elements[i - 1]
        number = float(elements[i])

        #Application de l'opération correspondante.
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
        elif operator == 'x':
            result *= number
        elif operator == '/':
            result /= number

    return result

#Initialisation des variables.
expression = input("Posez une opération : ")
result = evaluate_expression(expression)
print(f"Le résultat de l'expression est : {result}")