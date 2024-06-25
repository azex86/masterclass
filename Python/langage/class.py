"""
Les classes sont des structures de données définies par l'utilisateur qui permettent de regrouper des données et des fonctionnalités associées. 
Elles sont fondamentales dans la programmation orientée objet (POO).

Introduction aux Classes et Objets

Une classe est un modèle (blueprint) pour créer des objets. Les objets sont des instances de classes, contenant des données (attributs) et des comportements (méthodes).
"""
#Exemple :
class Personne:
    pass

p1 = Personne()
p2 = Personne()

#Définition d'une Classe

#Une classe est définie en utilisant le mot-clé class suivi du nom de la classe et de deux points :. Le corps de la classe contient les attributs et les méthodes.
#Exemple :
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

#Instances de Classes
#Une instance est un objet créé à partir d'une classe. On crée des instances en appelant le nom de la classe comme une fonction.
#Exemple :
p1 = Personne("Alice", 30)
p2 = Personne("Bob", 25)

print(p1.se_presenter())  # Affiche "Je m'appelle Alice et j'ai 30 ans."
print(p2.se_presenter())  # Affiche "Je m'appelle Bob et j'ai 25 ans."

#Attributs de Classe et d'Instance

#Les attributs de classe sont partagés par toutes les instances, tandis que les attributs d'instance sont propres à chaque instance.
#Exemple :
class Personne:
    espece = "Homo sapiens"  # Attribut de classe

    def __init__(self, nom, age):
        self.nom = nom  # Attribut d'instance
        self.age = age  # Attribut d'instance

p1 = Personne("Alice", 30)
p2 = Personne("Bob", 25)

print(p1.espece)  # Affiche "Homo sapiens"
print(p2.espece)  # Affiche "Homo sapiens"
Personne.espece = "Homo erectus"
print(p1.espece)  # Affiche "Homo erectus"
print(p2.espece)  # Affiche "Homo erectus"

#Méthodes de Classe et d'Instance

#Les méthodes de classe sont définies à l'intérieur d'une classe et prennent self comme premier argument. self fait référence à l'instance actuelle de la classe.
#Exemple :
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

p1 = Personne("Alice", 30)
print(p1.se_presenter())  # Affiche "Je m'appelle Alice et j'ai 30 ans."

#Constructeur (__init__)

#Le constructeur __init__ est une méthode spéciale appelée lors de la création d'une instance de la classe. Il initialise les attributs de l'instance.
#Exemple :
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p1 = Personne("Alice", 30)
print(p1.nom)  # Affiche "Alice"
print(p1.age)  # Affiche "30"

#Héritage

#L'héritage permet de créer une nouvelle classe à partir d'une classe existante. La nouvelle classe hérite des attributs et des méthodes de la classe parent.
#Exemple :
class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)  # Appelle le constructeur de la classe parent
        self.salaire = salaire

    def afficher_salaire(self):
        return f"Le salaire de {self.nom} est {self.salaire}."

e1 = Employe("Alice", 30, 50000)
print(e1.se_presenter())  # Affiche "Je m'appelle Alice et j'ai 30 ans."
print(e1.afficher_salaire())  # Affiche "Le salaire de Alice est 50000."

#Polymorphisme

#Le polymorphisme permet d'utiliser une interface commune pour des objets de types différents. 
# En Python, cela se fait principalement via l'héritage et les méthodes redéfinies.
#Exemple :
class Chat:
    def parler(self):
        return "Miaou"

class Chien:
    def parler(self):
        return "Wouf"

def faire_parler(animal):
    print(animal.parler())

chat = Chat()
chien = Chien()

faire_parler(chat)  # Affiche "Miaou"
faire_parler(chien)  # Affiche "Wouf"

#Encapsulation

#L'encapsulation est le concept de restreindre l'accès direct à certains composants d'un objet. En Python, cela se fait principalement par convention en utilisant un ou deux traits de soulignement pour les attributs et les méthodes privés.
#Exemple :
class Personne:
    def __init__(self, nom, age):
        self.__nom = nom  # Attribut privé
        self.__age = age  # Attribut privé

    def afficher_nom(self):
        return self.__nom

    def afficher_age(self):
        return self.__age

p1 = Personne("Alice", 30)
print(p1.afficher_nom())  # Affiche "Alice"
print(p1.afficher_age())  # Affiche "30"

"""
Bonnes Pratiques

    Utilisez des noms explicites : Donnez des noms clairs et significatifs à vos classes, méthodes et attributs.
    Utilisez les docstrings : Documentez vos classes et méthodes avec des docstrings pour expliquer leur fonction.
    Favorisez la composition sur l'héritage : Utilisez la composition lorsque cela est plus approprié que l'héritage.
    Encapsulez les détails d'implémentation : Utilisez l'encapsulation pour protéger les détails d'implémentation et exposer une interface claire.

Exemple de Bonne Pratique :
"""
class CompteBancaire:
    """Classe représentant un compte bancaire."""

    def __init__(self, titulaire, solde=0):
        """Initialise un compte bancaire avec un titulaire et un solde."""
        self.titulaire = titulaire
        self.__solde = solde  # Attribut privé

    def deposer(self, montant):
        """Dépose un montant sur le compte."""
        if montant > 0:
            self.__solde += montant

    def retirer(self, montant):
        """Retire un montant du compte."""
        if 0 < montant <= self.__solde:
            self.__solde -= montant

    def afficher_solde(self):
        """Affiche le solde du compte."""
        return f"Le solde du compte de {self.titulaire} est {self.__solde}."

# Utilisation de la classe
compte = CompteBancaire("Alice", 100)
compte.deposer(50)
print(compte.afficher_solde())  # Affiche "Le solde du compte de Alice est 150."


"""

En Python, les méthodes spéciales, aussi connues sous le nom de "méthodes magiques" ou "méthodes dunder" (double underscore), permettent de surcharger les opérateurs et d'autres comportements intégrés. 
Voici une liste des principales méthodes spéciales surchargables en Python :


Méthodes d'Opérateurs Arithmétiques

    __add__(self, other) : Addition (+)
    __sub__(self, other) : Soustraction (-)
    __mul__(self, other) : Multiplication (*)
    __truediv__(self, other) : Division (/)
    __floordiv__(self, other) : Division entière (//)
    __mod__(self, other) : Modulo (%)
    __pow__(self, other[, modulo]) : Puissance (**)
    __matmul__(self, other) : Multiplication matricielle (@)

Méthodes d'Opérateurs d'Assignation Composée

    __iadd__(self, other) : Addition en place (+=)
    __isub__(self, other) : Soustraction en place (-=)
    __imul__(self, other) : Multiplication en place (*=)
    __itruediv__(self, other) : Division en place (/=)
    __ifloordiv__(self, other) : Division entière en place (//=)
    __imod__(self, other) : Modulo en place (%=)
    __ipow__(self, other) : Puissance en place (**=)
    __imatmul__(self, other) : Multiplication matricielle en place (@=)

Méthodes d'Opérateurs Unaires

    __neg__(self) : Négation (-)
    __pos__(self) : Positif (+)
    __abs__(self) : Valeur absolue (abs())
    __invert__(self) : Inversion (~)

Méthodes d'Opérateurs de Comparaison

    __lt__(self, other) : Moins que (<)
    __le__(self, other) : Moins que ou égal (<=)
    __eq__(self, other) : Égal (==)
    __ne__(self, other) : Différent (!=)
    __gt__(self, other) : Plus que (>)
    __ge__(self, other) : Plus que ou égal (>=)

Méthodes d'Opérateurs Logiques

    __and__(self, other) : ET (&)
    __or__(self, other) : OU (|)
    __xor__(self, other) : XOR (^)
    __lshift__(self, other) : Décalage à gauche (<<)
    __rshift__(self, other) : Décalage à droite (>>)

Méthodes de Conversion de Type

    __int__(self) : Conversion en entier (int())
    __float__(self) : Conversion en flottant (float())
    __complex__(self) : Conversion en nombre complexe (complex())
    __bool__(self) : Conversion en booléen (bool())
    __str__(self) : Conversion en chaîne de caractères (str())
    __repr__(self) : Représentation officielle (repr())

Méthodes de Conteneurs

    __len__(self) : Longueur (len())
    __getitem__(self, key) : Accès à un élément (self[key])
    __setitem__(self, key, value) : Assignation d'un élément (self[key] = value)
    __delitem__(self, key) : Suppression d'un élément (del self[key])
    __iter__(self) : Itérateur (iter())
    __next__(self) : Prochaine valeur d'un itérateur (next())
    __contains__(self, item) : Vérifie la présence de item dans l'objet (in).

Méthodes de Gestion de Contexte

    __enter__(self) : Entrée dans un bloc with
    __exit__(self, exc_type, exc_value, traceback) : Sortie d'un bloc with

Méthodes de Gestion de l'Instance et de la Classe

    __new__(cls, *args, **kwargs) : Création d'une nouvelle instance
    __init__(self, *args, **kwargs) : Initialisation d'une instance
    __del__(self) : Destruction d'une instance (appelée quand un objet est sur le point d'être détruit)

Méthodes d'Attributs

    __getattr__(self, name) : Accès à un attribut inexistant
    __setattr__(self, name, value) : Assignation d'un attribut
    __delattr__(self, name) : Suppression d'un attribut
    __dir__(self) : Liste des attributs (dir())


Méthodes de Conversion et de Représentation

    __str__(self) : Conversion en chaîne de caractères (str()).
    __repr__(self) : Représentation officielle de l'objet (repr()).
    __format__(self, format_spec) : Formatage de l'objet selon format_spec.
    

Méthode autre:
    __call__(self,args*) : fonction utilisé quand l'objet est utilisé comme une fonction : a = Personne() ; a()
"""