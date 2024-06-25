"""
Les chaînes de caractères, ou strings, sont l'une des structures de données les plus couramment utilisées en Python.
Elles permettent de représenter et de manipuler du texte. 

Une string est une séquence immuable de caractères. 
En Python, les strings sont créées en utilisant des guillemets simples (') ou doubles (").

Exemple :
"""
mon_texte = "Bonjour, Python!"

#Création de Strings

#Les strings peuvent être créées de plusieurs façons :

#    Guillemets simples ou doubles :
str1 = 'Bonjour'
str2 = "Python"

#Guillemets triples pour les strings multilignes :
str3 = '''Ceci est une
string sur plusieurs lignes'''

#Avec la fonction str() :
str4 = str(123)  # "123"

#Accès aux Caractères

#Les caractères individuels d'une string sont accessibles par leurs indices, commençant à 0.
#Exemple :
texte = "Python"
print(texte[0])  # Affiche 'P'
print(texte[-1])  # Affiche 'n'

#Slicing (Découpage) des Strings
#Le slicing permet d'extraire des sous-chaînes d'une string en utilisant des indices.
#Exemple :
texte = "Python"

print(texte[1:4])  # Affiche 'yth'
print(texte[:2])  # Affiche 'Py'
print(texte[3:])  # Affiche 'hon'
print(texte[:])  # Affiche 'Python'
print(texte[::2])  # Affiche 'Pto'

#Opérations de Base sur les Strings

#Les strings supportent plusieurs opérations de base :

#    Concaténation :
str1 = "Bonjour"
str2 = "Python"
str3 = str1 + ", " + str2  # "Bonjour, Python"

#Répétition :
str4 = "Ha" * 3  # "HaHaHa"

#Appartenance :
"Pyt" in "Python"  # True
"Java" in "Python"  # False

#Méthodes Utiles pour les Strings

#Les strings possèdent de nombreuses méthodes intégrées pour leur manipulation.

#    lower() et upper() :
texte = "Bonjour"
print(texte.lower())  # "bonjour"
print(texte.upper())  # "BONJOUR"

#strip(), lstrip(), rstrip() :
texte = "  Bonjour "
print(texte.strip())  # "Bonjour"
print(texte.lstrip())  # "Bonjour "
print(texte.rstrip())  # "  Bonjour"

#replace() :
texte = "Bonjour Python"
print(texte.replace("Python", "le Monde"))  # "Bonjour le Monde"

#split() et join() :
texte = "Bonjour le Monde"
mots = texte.split()  # ["Bonjour", "le", "Monde"]
nouvelle_texte = " ".join(mots)  # "Bonjour le Monde"

#find() et index() :
texte = "Bonjour Python"
print(texte.find("Python"))  # 8
print(texte.index("Python"))  # 8

#Formatage des Strings

#Python propose plusieurs méthodes pour formater des strings.

#    Opérateur % :
nom = "Alice"
age = 30
texte = "Je m'appelle %s et j'ai %d ans." % (nom, age)  # "Je m'appelle Alice et j'ai 30 ans."

#Méthode format() :
texte = "Je m'appelle {} et j'ai {} ans.".format(nom, age)  # "Je m'appelle Alice et j'ai 30 ans."

#F-strings (depuis Python 3.6) méthode à priviligier ! :
texte = f"Je m'appelle {nom} et j'ai {age} ans."  # "Je m'appelle Alice et j'ai 30 ans."

#Manipulation Avancée des Strings

#    Échapper les caractères spéciaux :
texte = "Ceci est un \"exemple\"."

#Raw strings (pour les expressions régulières) et les chemin:
chemin = r"C:\nouveau\chemin"