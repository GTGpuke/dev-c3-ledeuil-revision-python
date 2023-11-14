#Exercice 6: Modules : Utilisez le module datetime pour afficher la date et l'heure actuelles.
import datetime

#Initialisation variables... date et heure...
date_heure = datetime.datetime.now()
print("Date et heure actuelles : ")
print(date_heure.strftime("%Y-%m-%d %H:%M:%S"))