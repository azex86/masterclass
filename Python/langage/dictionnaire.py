"""Cours sur les Dictionnaires en Python

Les dictionnaires sont des structures de données très utiles en Python, permettant de stocker des paires clé-valeur. Ils sont optimisés pour la recherche, l'insertion et la suppression rapide d'éléments. Ce cours va couvrir les points suivants :

    Introduction aux dictionnaires
    Création de dictionnaires
    Accès aux éléments
    Ajout et modification d'éléments
    Suppression d'éléments
    Méthodes et opérations sur les dictionnaires
    Parcours des dictionnaires
    Dictionnaires imbriqués
    Compréhensions de dictionnaires
    Bonnes pratiques et conseils

1. Introduction aux Dictionnaires

Un dictionnaire en Python est une collection non ordonnée, modifiable et indexée de paires clé-valeur. Les clés doivent être uniques et immuables (comme les chaînes de caractères, les nombres ou les tuples), tandis que les valeurs peuvent être de n'importe quel type.
Exemple :"""



mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}

#Création de Dictionnaires

#Les dictionnaires peuvent être créés de plusieurs façons :

#    Avec des accolades {} :
mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}

#Avec la fonction dict() :
mon_dict = dict(nom="Alice", âge=25, ville="Paris")

#À partir d'une liste de tuples :
liste_tuples = [("nom", "Alice"), ("âge", 25), ("ville", "Paris")]
mon_dict = dict(liste_tuples)

#Accès aux Éléments

#Les éléments d'un dictionnaire sont accessibles via leurs clés.
#Exemple :
mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}
print(mon_dict["nom"])  # Affiche "Alice"

#Pour éviter des erreurs si la clé n'existe pas, utilisez la méthode get() :
print(mon_dict.get("nom"))  # Affiche "Alice"
print(mon_dict.get("adresse", "Non spécifié"))  # Affiche "Non spécifié"

#Ajout et Modification d'Éléments

#Pour ajouter ou modifier des éléments, utilisez simplement l'opérateur de clé.
#Exemple :
mon_dict["email"] = "alice@example.com"  # Ajoute une nouvelle paire clé-valeur
mon_dict["âge"] = 26  # Modifie la valeur associée à la clé "âge"

#Suppression d'Éléments
#Les éléments peuvent être supprimés à l'aide de la fonction del, de la méthode pop() ou de la méthode popitem().
#Exemple :
del mon_dict["ville"]  # Supprime l'élément avec la clé "ville"

age = mon_dict.pop("âge")  # Supprime et retourne la valeur associée à "âge"
print(age)  # Affiche 26

element = mon_dict.popitem()  # Supprime et retourne la dernière paire clé-valeur insérée
print(element)  # Affiche ('email', 'alice@example.com')

#Méthodes et Opérations sur les Dictionnaires

"""Les dictionnaires possèdent plusieurs méthodes utiles :

    keys() : Retourne une vue des clés du dictionnaire.
    values() : Retourne une vue des valeurs du dictionnaire.
    items() : Retourne une vue des paires clé-valeur.
    update() : Met à jour le dictionnaire avec les paires clé-valeur d'un autre dictionnaire ou d'un itérable de paires clé-valeur.

Exemple :
"""
mon_dict = {"nom": "Alice", "âge": 25}

print(mon_dict.keys())  # Affiche dict_keys(['nom', 'âge'])
print(mon_dict.values())  # Affiche dict_values(['Alice', 25])
print(mon_dict.items())  # Affiche dict_items([('nom', 'Alice'), ('âge', 25)])

autre_dict = {"ville": "Paris", "email": "alice@example.com"}
mon_dict.update(autre_dict)
print(mon_dict)
# Affiche {'nom': 'Alice', 'âge': 25, 'ville': 'Paris', 'email': 'alice@example.com'}

#Parcours des Dictionnaires

#Les dictionnaires peuvent être parcourus en utilisant des boucles.
#Exemple :
mon_dict = {"nom": "Alice", "âge": 25, "ville": "Paris"}

# Parcourir les clés
for key in mon_dict:
    print(key)

# Parcourir les valeurs
for value in mon_dict.values():
    print(value)

# Parcourir les paires clé-valeur
for key, value in mon_dict.items():
    print(f"{key}: {value}")

#Dictionnaires Imbriqués

#Les dictionnaires peuvent contenir d'autres dictionnaires.
#Exemple :
étudiant = {
    "nom": "Alice",
    "cours": {
        "maths": 90,
        "physique": 85
    }
}
print(étudiant["cours"]["maths"])  # Affiche 90

#Compréhensions de Dictionnaires

#Les compréhensions de dictionnaires permettent de créer des dictionnaires de manière concise.
#Exemple :
nombres = [1, 2, 3, 4]
carrés = {x: x ** 2 for x in nombres}
print(carrés)
# Affiche {1: 1, 2: 4, 3: 9, 4: 16}

#Clés immuables : Utilisez des types immuables (chaînes de caractères, nombres, tuples) comme clés.