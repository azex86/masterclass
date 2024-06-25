# Cours sur l'Usage du Module random en Python

# Le module random en Python fournit des fonctions pour générer des nombres pseudo-aléatoires, 
# permettant de réaliser des opérations comme le tirage au sort, 
# la génération de nombres aléatoires pour des jeux, des simulations, et d'autres applications. 
# Voici un aperçu complet de l'utilisation du module random.

import random

# 1. Génération de Nombres Aléatoires Simples

# random() - Retourne un flottant aléatoire entre 0.0 et 1.0
print(random.random())

# randint(a, b) - Retourne un entier aléatoire N tel que a <= N <= b
print(random.randint(1, 10))

# randrange(start, stop[, step]) - Retourne un entier choisi aléatoirement dans la séquence range(start, stop, step)
print(random.randrange(0, 101, 10))

# uniform(a, b) - Retourne un flottant N tel que a <= N <= b
print(random.uniform(1.5, 1.9))

# 2. Sélection Aléatoire

# choice(seq) - Retourne un élément aléatoire de la séquence non vide seq
noms = ['Alice', 'Bob', 'Charlie', 'Diana']
print(random.choice(noms))

# choices(population, weights=None, *, cum_weights=None, k=1) - Retourne une liste de k éléments choisis avec remplacement
print(random.choices(noms, k=2))

# sample(population, k) - Retourne une liste de k éléments choisis sans remplacement
print(random.sample(noms, 2))

# 3. Mélanger des Séquences

# shuffle(x[, random]) - Mélange la séquence x sur place
cartes = ['As', 'Roi', 'Reine', 'Valet']
random.shuffle(cartes)
print(cartes)

# 4. Contrôle de la Génération Aléatoire

# seed(a=None, version=2) - Initialise le générateur de nombres aléatoires. Peut être utilisé pour obtenir des résultats reproductibles
random.seed(42)
print(random.random())

# 5. Distribution Statistique inutile dans 99% des cas

# Les fonctions suivantes génèrent des valeurs en fonction de diverses distributions statistiques :

# gauss(mu, sigma) - Retourne un flottant aléatoire selon la distribution normale (gaussienne) avec la moyenne mu et l'écart type sigma
print(random.gauss(0, 1))

# expovariate(lambd) - Retourne un flottant aléatoire selon la distribution exponentielle avec le paramètre lambda
print(random.expovariate(1))

# gammavariate(alpha, beta) - Retourne un flottant aléatoire selon la distribution gamma avec les paramètres alpha et beta
print(random.gammavariate(1, 2))

# betavariate(alpha, beta) - Retourne un flottant aléatoire selon la distribution bêta avec les paramètres alpha et beta
print(random.betavariate(2, 5))

# paretovariate(alpha) - Retourne un flottant aléatoire selon la distribution de Pareto avec le paramètre alpha
print(random.paretovariate(1))

# 6. Exemple Pratique

# Simulons un jeu de dés où nous lançons deux dés à six faces et additionnons les résultats

def lancer_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    return de1 + de2

resultat = lancer_des()
print("Résultat du lancer de dés:", resultat)

# Noter que le module random donne des veleurs pseudo-aléatoires
# Il ne doit pas être utiliser lors d'opération cryptographique 
# ou lorsque le manque d'aléatoire peut compromettre le bon déroulement du programme