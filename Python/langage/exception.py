"""Cours sur les Exceptions en Python

Les exceptions sont un mécanisme important de la gestion des erreurs en Python. 
Elles permettent de gérer des conditions d'erreur de manière propre et contrôlée. 


Une exception est un événement qui survient lors de l'exécution d'un programme et qui perturbe le flux normal d'instructions. En Python, lorsque ces erreurs surviennent, elles génèrent des exceptions. Si ces exceptions ne sont pas gérées, elles provoqueront l'arrêt du programme.
Exemple :
"""
# Exemple d'une division par zéro
print(10 / 0)

"""Ce code lève une exception ZeroDivisionError parce qu'une division par zéro est mathématiquement indéfinie.
2. Syntaxe de base pour la gestion des exceptions

La gestion des exceptions en Python se fait à l'aide des mots-clés try, except, else et finally.

    try : Le bloc de code à essayer, où l'exception peut se produire.
    except : Le bloc de code à exécuter si une exception survient.
    else : Le bloc de code à exécuter si aucune exception ne survient (facultatif).
    finally : Le bloc de code à exécuter quoi qu'il arrive (facultatif).

Exemple de base :"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro.")
else:
    print("La division a réussi.")
finally:
    print("Bloc finally exécuté.")

"""

Python propose plusieurs types d'exceptions prédéfinies, parmi les plus courantes :

    ZeroDivisionError : Tentative de division par zéro.
    ValueError : Inadéquation de la valeur.
    TypeError : Type d'objet inapproprié.
    IndexError : Index non valide pour une séquence.
    KeyError : Clé non trouvée dans un dictionnaire.
    FileNotFoundError : Fichier ou répertoire demandé introuvable.

Exemple de différents types d'exceptions :
"""


# ValueError
try:
    number = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# KeyError
my_dict = {'key1': 'value1'}
try:
    value = my_dict['key2']
except KeyError as e:
    print(f"KeyError: {e}")


#Il est possible de définir ses propres exceptions en créant des classes dérivées de la classe Exception.
#Exemple de personnalisation d'exception :

class MaPropreException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MaPropreException("Ceci est une exception personnalisée.")
except MaPropreException as e:
    print(e.message)



#Exemple de bonnes pratiques :



try:
    with open("somefile.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
finally:
    print("Opération de lecture terminée.")



#Les exceptions en Python sont un outil puissant pour la gestion des erreurs. En utilisant des blocs try/except/else/finally, en connaissant les types d'exceptions et en suivant les bonnes pratiques, vous pouvez écrire des programmes robustes et fiables.