"""
Les modules en Python sont des fichiers contenant des définitions et des instructions Python. 
Ils permettent de structurer un programme en le divisant en sous-programmes, ce qui facilite la gestion et la réutilisation du code. 



Un module est un fichier contenant du code Python (fonctions, classes, variables, etc.) que vous pouvez réutiliser dans d'autres programmes. 
Les modules permettent de mieux organiser votre code en le divisant en parties logiques.

Exemple :

    math : Un module standard pour les opérations mathématiques.
    datetime : Un module pour travailler avec les dates et les heures.
"""

#Importation de Modules

#Il existe plusieurs façons d'importer des modules en Python :

#    Importation complète :
import math
print(math.sqrt(16))  # Affiche 4.0

#Importation avec alias :
import math as m
print(m.sqrt(16))  # Affiche 4.0

#Importation partielle :
from math import sqrt
print(sqrt(16))  # Affiche 4.0

#Importation partielle avec alias :
from math import sqrt as racine
print(racine(16))  # Affiche 4.0

#Importation de tous les éléments (à éviter généralement) :
from math import *
print(sqrt(16))  # Affiche 4.0

#Création de Modules

#Pour créer un module, il suffit de sauvegarder du code Python dans un fichier avec l'extension .py. Par exemple, créez un fichier mon_module.py :

# mon_module.py

def saluer(nom):
    return f"Bonjour, {nom}!"

pi = 3.14159

#Ensuite, vous pouvez importer et utiliser ce module dans un autre fichier Python :
# utilisation_module.py

import mon_module

print(mon_module.saluer("Alice"))  # Affiche "Bonjour, Alice!"
print(mon_module.pi)  # Affiche 3.14159

#Utilité des Modules

"""
Les modules offrent plusieurs avantages :

    Réutilisabilité : Vous pouvez réutiliser le même code dans différents programmes.
    Organisation : Les modules permettent de structurer le code en parties logiques, facilitant la compréhension et la maintenance.
    Namespaces : Les modules créent leur propre espace de noms, réduisant les conflits de noms.
    Modularité : Les modules facilitent le développement collaboratif en permettant à plusieurs développeurs de travailler sur différentes parties du projet.

Durée de Vie des Modules

Lorsqu'un module est importé, Python charge son contenu et le garde en mémoire pour la durée de vie du programme. 
Si vous essayez de réimporter le même module, Python utilise la version déjà chargée pour éviter les redondances et améliorer les performances.

    Module déjà importé :
"""
import mon_module
import mon_module  # Ce deuxième import ne recharge pas le module

#Forcer le rechargement d'un module (utile pour le développement) :
import importlib
importlib.reload(mon_module)



#Dans le cas le module à importer n'est pas un fichier python local
#ou un modul python intégré il est nécessaire de l'installer avec le gestionnaire de paquets
#'pip' qui recherche dans Python Package Index (PyPI)

#dans un terminal
#pip install [module]


#exemple
#dans un terminal
#pip install numpy   

import numpy

