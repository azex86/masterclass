# Cours sur l'écriture de documentation et de commentaires en Python

# Dans Python, la documentation et les commentaires jouent un rôle crucial pour rendre votre code compréhensible, maintenable et collaboratif. Ce cours couvre les bonnes pratiques pour écrire des docstrings et des commentaires efficaces.

# 1. Commentaires

# Les commentaires en Python commencent par le symbole # et sont utilisés pour expliquer le code.

# Exemple de commentaire :

# Définition d'une fonction qui calcule la somme de deux nombres
def addition(a, b):
    return a + b

# 2. Docstrings

# Les docstrings sont des chaînes de documentation utilisées pour décrire des fonctions, des classes, des méthodes et des modules. Ils sont encadrés par trois guillemets (""" """ ou ''' ''').

# Exemple de docstring pour une fonction :

def soustraction(a, b):
    """
    Cette fonction effectue la soustraction de deux nombres.
    
    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
        
    Returns:
        int: La différence entre a et b.
    """
    return a - b

# 3. Types de Docstrings

# Il existe différents styles de docstrings, notamment ceux basés sur Google, Numpy et reStructuredText (reST). Utilisez celui qui correspond aux conventions de votre projet.

# Exemple de docstring Google-style :

def multiplication(a, b):
    """
    Multiplie deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.

    Returns:
        int: Le produit de a et b.
    """

# 4. Documentation de Classe et de Méthodes

# Les classes et leurs méthodes doivent également être documentées pour expliquer leur objectif et leur fonctionnement.

# Exemple de docstring pour une classe et sa méthode :

class Calculatrice:
    """
    Une classe représentant une calculatrice simple.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de la calculatrice.
        """
        pass

    def addition(self, a, b):
        """
        Effectue l'addition de deux nombres.

        Args:
            a (int): Le premier nombre.
            b (int): Le deuxième nombre.

        Returns:
            int: La somme de a et b.
        """
        return a + b

# 5. Bonnes Pratiques

# - Utilisez des docstrings pour chaque fonction, méthode, classe et module.
# - Écrivez des commentaires clairs et concis pour expliquer des parties non évidentes du code.
# - Respectez la convention et le style de documentation adopté par votre équipe ou projet.

# Conclusion

# La documentation et les commentaires bien écrits rendent votre code plus facile à comprendre pour vous-même et pour les autres développeurs. Ils facilitent la maintenance, le débogage et la collaboration dans les projets Python.

# Exemple de sortie des docstrings :

# - Utilisation de l'outil `help()` dans l'interpréteur Python pour accéder à la documentation :
#   >>> help(soustraction)
#   Help on function soustraction in module __main__:
#
#   soustraction(a, b)
#       Cette fonction effectue la soustraction de deux nombres.
#
#       Args:
#           a (int): Le premier nombre.
#           b (int): Le deuxième nombre.
#
#       Returns:
#           int: La différence entre a et b.
