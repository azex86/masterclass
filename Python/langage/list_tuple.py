"""
Les listes sont l'une des structures de données les plus fondamentales et polyvalentes en Python. 
Elles permettent de stocker des collections d'éléments et offrent une grande flexibilité dans leur manipulation. 

Une liste est une séquence ordonnée d'éléments. 
Les listes sont mutables, ce qui signifie que leurs éléments peuvent être modifiés après leur création. 
Elles peuvent contenir des éléments de différents types, y compris d'autres listes.

Exemple :"""

ma_liste = [1, 2, 3, "Python", [4, 5]]

#Création de Listes

#Les listes peuvent être créées de plusieurs façons :

#Avec des crochets [] :
ma_liste = [1, 2, 3, "Python"]

#Avec la fonction list() :
ma_liste = list([1, 2, 3, "Python"])

#À partir d'un itérable :
ma_liste = list(range(5))  # [0, 1, 2, 3, 4]

#Accès aux Éléments d'une Liste
#Les éléments d'une liste sont accessibles par leurs indices, commençant à 0. Les indices négatifs peuvent être utilisés pour accéder aux éléments depuis la fin de la liste.
#Exemple :
ma_liste = [1, 2, 3, "Python"]

print(ma_liste[0])  # Affiche 1
print(ma_liste[-1])  # Affiche "Python"

#Modification d'Éléments

#Les éléments d'une liste peuvent être modifiés en assignant de nouvelles valeurs à des indices spécifiques.
#Exemple :
ma_liste = [1, 2, 3, "Python"]
ma_liste[1] = "deux"
print(ma_liste)  # Affiche [1, "deux", 3, "Python"]

#Ajout d'Éléments
"""
Les listes offrent plusieurs méthodes pour ajouter des éléments :

    append() : Ajoute un élément à la fin de la liste.
    insert() : Insère un élément à une position spécifique.
    extend() : Ajoute les éléments d'un itérable à la fin de la liste.

Exemple :
"""
ma_liste = [1, 2, 3]

ma_liste.append(4)  # [1, 2, 3, 4]
ma_liste.insert(1, "deux")  # [1, "deux", 2, 3, 4]
ma_liste.extend([5, 6])  # [1, "deux", 2, 3, 4, 5, 6]

#Suppression d'Éléments

"""Les listes offrent plusieurs méthodes pour supprimer des éléments :

    remove() : Supprime la première occurrence d'un élément.
    pop() : Supprime l'élément à une position spécifique et le retourne.
    del : Supprime un élément par son indice.
"""
#Exemple :
ma_liste = [1, 2, 3, 4, 2]

ma_liste.remove(2)  # [1, 3, 4, 2]
element = ma_liste.pop(1)  # [1, 4, 2], element = 3
del ma_liste[0]  # [4, 2]

#Parcours des Listes

#Les listes peuvent être parcourues en utilisant des boucles, notamment des boucles for.
#Exemple :
ma_liste = [1, 2, 3, 4]

for element in ma_liste:
    print(element)

#Méthodes Utiles pour les Listes
"""
Les listes possèdent plusieurs méthodes intégrées utiles pour diverses opérations :

    sort() : Trie la liste en place.
    reverse() : Inverse les éléments de la liste en place.
    index() : Retourne l'indice de la première occurrence d'un élément.
    count() : Retourne le nombre d'occurrences d'un élément.
    copy() : Retourne une copie superficielle de la liste.
    clear() : Supprime tous les éléments de la liste.
"""
#Exemple :
ma_liste = [3, 1, 4, 2, 2]

ma_liste.sort()  # [1, 2, 2, 3, 4]
ma_liste.reverse()  # [4, 3, 2, 2, 1]
print(ma_liste.index(2))  # Affiche 2
print(ma_liste.count(2))  # Affiche 2

copie_liste = ma_liste.copy()
ma_liste.clear()  # []

#Listes Imbriquées

#Les listes peuvent contenir d'autres listes, ce qui permet de créer des structures de données plus complexes comme des matrices.
#Exemple :
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[0][1])  # Affiche 2

#Compréhensions de Listes

#Les compréhensions de listes permettent de créer des listes de manière concise et élégante.
#Exemple :
carres = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
pairs = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

#Bonnes Pratiques
"""
    Utilisez des noms explicites : Donnez des noms clairs et significatifs à vos listes.
    Préférez les compréhensions : Utilisez les compréhensions de listes pour des transformations simples.
    Manipulez les exceptions : Soyez attentif à la gestion des erreurs lors de l'accès aux indices.
    Évitez les modifications pendant l'itération : Modifiez la liste avec prudence lors de son parcours pour éviter des comportements inattendus.
"""

# Mauvaise pratique : modification pendant l'itération
ma_liste = [1, 2, 3, 4]
for i in ma_liste:
    if i % 2 == 0:
        ma_liste.remove(i)

# Bonne pratique : créer une nouvelle liste
ma_liste = [1, 2, 3, 4]
ma_liste = [i for i in ma_liste if i % 2 != 0]  # [1, 3]











"""
Les tuples sont similaires aux listes, mais ils présentent une différence clé : ils sont immuables, c'est-à-dire que leurs éléments ne peuvent pas être modifiés après leur création. Cette immuabilité rend les tuples particulièrement utiles pour représenter des collections de données qui ne doivent pas changer. Ce cours va couvrir les points suivants :
"""

#Un tuple est une séquence ordonnée d'éléments, similaire à une liste, mais immuable.
# Les tuples peuvent contenir des éléments de différents types.
#Exemple :
mon_tuple = (1, 2, 3, "Python")

#Création de Tuples

#Les tuples peuvent être créés de plusieurs façons :

#    Avec des parenthèses () :
mon_tuple = (1, 2, 3, "Python")

#Sans parenthèses (utilisation de la virgule) :
mon_tuple = 1, 2, 3, "Python"

#À partir d'un itérable avec tuple() :
mon_tuple = tuple([1, 2, 3, "Python"])

#Tuple vide et singleton :
tuple_vide = ()
singleton = (1,)  # Notez la virgule

#Accès aux Éléments d'un Tuple

#Comme pour les listes, les éléments d'un tuple sont accessibles par leurs indices, commençant à 0.
#Exemple :
mon_tuple = (1, 2, 3, "Python")

print(mon_tuple[0])  # Affiche 1
print(mon_tuple[-1])  # Affiche "Python"

#Opérations sur les Tuples

#Les tuples supportent plusieurs opérations similaires aux listes, comme la concaténation et la répétition.
#Exemple :
tuple1 = (1, 2)
tuple2 = (3, 4)

# Concaténation
tuple_concat = tuple1 + tuple2  # (1, 2, 3, 4)

# Répétition
tuple_repete = tuple1 * 3  # (1, 2, 1, 2, 1, 2)

#Immutabilité et Tentatives de Modification

#Les tuples sont immuables, ce qui signifie que vous ne pouvez pas modifier leurs éléments après leur création. 
# Toute tentative de modification entraîne une erreur.
#Exemple :
mon_tuple = (1, 2, 3)

try:
    mon_tuple[0] = 4  # Provoque une erreur
except TypeError as e:
    print(e)  # Affiche "TypeError: 'tuple' object does not support item assignment"

#Utilisation des Tuples

#Les tuples sont souvent utilisés pour :

#    Retourner plusieurs valeurs depuis une fonction :
def divmod(a, b):
    return a // b, a % b

quotient, reste = divmod(10, 3)

#Stocker des collections hétérogènes :
personne = ("Alice", 30, "Ingénieur")

#Utiliser comme clés dans les dictionnaires :
coordonnees = (45.0, -93.0)
lieux = {coordonnees: "Minneapolis"}

#Déballage des Tuples
#Le déballage des tuples permet d'assigner les éléments d'un tuple à des variables individuelles de manière concise.
#Exemple :
mon_tuple = (1, 2, 3)
a, b, c = mon_tuple

print(a)  # Affiche 1
print(b)  # Affiche 2
print(c)  # Affiche 3

# Déballage avec l'astérisque (*)
mon_tuple = (1, 2, 3, 4, 5)
a, *b, c = mon_tuple
print(a)  # Affiche 1
print(b)  # Affiche [2, 3, 4]
print(c)  # Affiche 5