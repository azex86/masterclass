"""
    La programmation peut se résumer en trois action : 
                                lire la mémoire
                                tester cette mémoire
                                écrire sur la mémoire
    En somme la manipulation de la mémoire(RAM)
    pour nous, developpeur python la manipulation de la mémoire se fait à l'aide de "variable"
    Une variable est une données stockée en RAM à laquelle nous accédons par un nom et python s'occupe du reste

    En pratique, en python :
"""

a = 10 #déclaration d"une variable
#le nom 'a' va maintenant désigner une case mémoire dans laquelle se trouve le nombre 10

print(a) #print([variable]) permet d'afficer le contenu d'une variable
 
a = 5 #on va modifier la case mémoire pointer par 'a'

print(a)

#pour déclarer ou modifier le contenu d'une variable 
# nom_de_la_variable_sans_espace = valeur

"""
    chaque variable a donc une valeur (ou du moins une case en RAM dans laquelle se trouve cette valeur)
    cette 'valeur' est ce que nous appelons un objet
    un objet possède est caractérisé par son TYPE et par un ensemble de données et de fonctionnalitées
"""
a = 10 # a référence un objet de type int c'est à dire entier, pour simplifier on dira que a est un int
#int signifie integer en python

a = 0.5 # a est un float c'est à dire un nombre à virgule notée que les float

a = "hello world !" #a est un str c'est à dire une chaîne de caractères

a = False
a = True #a est un bool pour booléen

a = []#a est une list


a = (0,) # a est un tuple

a = {} #a est un dict (dictionnaire)


#il existe un nombre infini de type d'objet mais ceux-ci dessus sont les plus fréquents et "builtin" = intégrés au langage
#Nous pouvons également créer nos propres types, voir 'class'
#Chaque objet possède un ensemble de données, l'ensemble est accessible par le la variable 





#chose à savoir sur le type des variables
t = type(a) #donne le type de a

doc = dir(a) #donne l'ensemble des données de a

is_int = isinstance(a,int) # retourne si a est de type int


#nous savons maintenant écrire en mémoire

#maintenant comment lire ?
#c'est très simple, pour lire une variable il suffite de mettre son nom

b = a #on lit a et on écrit b
#b a maintenant le même espace mémoire que a

#Pour accéder à un seul élément de l'objet on utiliser '.' 
#exemple
a = {}
a.__doc__ #on accède à la données '__doc__' de l'objet pointé par la variable a
a.__doc__ = "alors voici la documentation"

#Pour tester le contenu d'une variable
# et comparer la valeur en stockant le résulat dans r 
a = 5
b = 10

r = a == b 
r = a > b
r = a >= b
r = a < b
r = a <= b
#à chaque étape r vaut False ou True


#pour tester si deux variables partagent la même case mémoire et donc le même objet
r = a is b