"""Cours sur les Générateurs en Python

Les générateurs sont des objets en Python qui permettent de produire une séquence de valeurs au fur et à mesure, sans les stocker toutes en mémoire à la fois. 
Ils sont particulièrement utiles pour travailler avec des grandes données ou des flux de données continus. 

Les générateurs sont des fonctions spéciales qui retournent un itérateur. 
Ils permettent de créer des itérateurs de manière simple et efficace en utilisant le mot-clé yield. 
À chaque fois que la fonction est appelée, elle reprend l'exécution juste après le dernier yield.

Exemple Simple :
"""

def mon_generateur():
    yield 1
    yield 2
    yield 3

gen = mon_generateur()
print(next(gen))  # Affiche 1
print(next(gen))  # Affiche 2
print(next(gen))  # Affiche 3

#Création de Générateurs

#Les générateurs sont créés à l'aide de fonctions contenant une ou plusieurs instructions yield.
#Exemple de Générateur :
def compteur(max):
    i = 0
    while i < max:
        yield i
        i += 1

for nombre in compteur(5):
    print(nombre)

#Fonctionnement des Générateurs

#Lorsque la fonction génératrice est appelée, elle retourne un objet générateur mais ne commence pas son exécution immédiatement.
# La méthode __next__() est appelée pour exécuter la fonction jusqu'au prochain yield. Chaque appel de __next__() reprend l'exécution là où elle s'était arrêtée après le dernier yield.
#Exemple avec Explications :
def generateur_simple():
    print("Commence")
    yield 1
    print("Reprend")
    yield 2
    print("Reprend encore")
    yield 3

gen = generateur_simple()
print(next(gen))  # Affiche "Commence" puis 1
print(next(gen))  # Affiche "Reprend" puis 2
print(next(gen))  # Affiche "Reprend encore" puis 3

#Générateurs vs. Listes

#Les générateurs sont plus efficaces en termes de mémoire que les listes, surtout lorsque vous travaillez avec de grandes séquences de données, car ils produisent les éléments à la demande.
#Exemple de Comparaison :
# Générateur pour les nombres de 0 à 9999999
def generateur_nombres(max):
    i = 0
    while i < max:
        yield i
        i += 1

# Liste pour les nombres de 0 à 9999999
liste_nombres = [i for i in range(10000000)]

print(sum(generateur_nombres(10000000)))  # Utilise très peu de mémoire
print(sum(liste_nombres))  # Utilise beaucoup de mémoire

#Générateurs Infinis

#Les générateurs peuvent produire un nombre infini de valeurs. 
#Il faut être prudent avec les boucles infinies pour éviter les programmes qui ne se terminent jamais.
#Exemple de Générateur Infini :
def generateur_infini():
    i = 0
    while True:
        yield i
        i += 1

gen = generateur_infini()
for _ in range(5):  # Pour éviter une boucle infinie, on limite à 5 itérations
    print(next(gen))

#Méthodes Avancées pour Générateurs
"""
Les générateurs ont plusieurs méthodes avancées comme send(), throw(), et close().

    send(value) : Permet d'envoyer une valeur au générateur et de reprendre l'exécution jusqu'au prochain yield.
    throw(type, value=None, traceback=None) : Permet de lever une exception dans le générateur.
    close() : Permet de terminer le générateur.

Exemple Avancé :
"""
def generateur_avance():
    try:
        while True:
            valeur = (yield)
            print(f"Reçu : {valeur}")
    except GeneratorExit:
        print("Générateur fermé")

gen = generateur_avance()
next(gen)  # Prépare le générateur
gen.send(10)  # Affiche "Reçu : 10"
gen.send(20)  # Affiche "Reçu : 20"
gen.close()  # Affiche "Générateur fermé"

#Bonnes Pratiques

#    Utilisez les générateurs pour les grandes données : Les générateurs sont particulièrement utiles pour traiter des grandes quantités de données ou des flux continus de données.
#    Manipulez les exceptions : Soyez attentif à la gestion des exceptions dans les générateurs.
#    Fermez les générateurs : Utilisez la méthode close() pour libérer les ressources si nécessaire.

#Exemple de Bonne Pratique :
def lecture_fichier_ligne_par_ligne(nom_fichier):
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            yield ligne

def traiter(line):
    """traite une ligne du fichier"""
    pass

for ligne in lecture_fichier_ligne_par_ligne("grand_fichier.txt"):
    traiter(ligne)  # Fonction de traitement de chaque ligne


#Les générateurs sont une fonctionnalité puissante et flexible en Python, permettant de créer des itérateurs de manière concise et efficace. 
# Ils sont particulièrement utiles pour travailler avec des grandes données ou des flux continus, permettant des économies de mémoire importantes. 
