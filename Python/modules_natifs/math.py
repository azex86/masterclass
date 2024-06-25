# Cours sur le Module math en Python

# Le module math en Python fournit des fonctions pour effectuer des opérations mathématiques courantes et avancées. 
# Ce module est essentiel pour les calculs numériques, la manipulation des nombres, et les opérations mathématiques spécialisées.

# Sans le module  math

# valeur absolue abs(x)
print(f"|-5| = {abs(-5)}") 

# x puissance y : x**y
print(f"3*3*3*3 = {3**4}")

# racine carré = puissance 0.5
print(f"squrt(25) = {25**0.5}")

import math

# 1. Fonctions Mathématiques de Base

# sqrt(x) - Retourne la racine carrée de x
print("Racine carrée de 16:", math.sqrt(16))

# ceil(x) - Retourne le plus petit entier supérieur ou égal à x
print("Plafond de 4.2:", math.ceil(4.2))

# floor(x) - Retourne le plus grand entier inférieur ou égal à x
print("Plancher de 4.8:", math.floor(4.8))

# fabs(x) - Retourne la valeur absolue de x
print("Valeur absolue de -5:", math.fabs(-5))

# factorial(x) - Retourne la factorielle de x
print("Factorielle de 5:", math.factorial(5))

# 2. Fonctions Trigonométriques

# sin(x) - Retourne le sinus de x (en radians)
print("Sinus de π/2:", math.sin(math.pi / 2))

# cos(x) - Retourne le cosinus de x (en radians)
print("Cosinus de π:", math.cos(math.pi))

# tan(x) - Retourne la tangente de x (en radians)
print("Tangente de π/4:", math.tan(math.pi / 4))

# asin(x) - Retourne l'arc sinus de x, résultat en radians
print("Arc sinus de 1:", math.asin(1))

# acos(x) - Retourne l'arc cosinus de x, résultat en radians
print("Arc cosinus de 0:", math.acos(0))

# atan(x) - Retourne l'arc tangente de x, résultat en radians
print("Arc tangente de 1:", math.atan(1))

# hypot(x, y) - Retourne la longueur de l'hypoténuse de l'angle droit avec les côtés de longueur x et y
print("Hypoténuse pour les côtés de longueur 3 et 4:", math.hypot(3, 4))

# 3. Fonctions Exponentielles et Logarithmiques

# exp(x) - Retourne e élevé à la puissance x
print("e^3:", math.exp(3))

# log(x[, base]) - Retourne le logarithme de x à la base spécifiée. Si la base n'est pas spécifiée, retourne le logarithme naturel (base e)
print("Logarithme naturel de 20:", math.log(20))
print("Logarithme base 10 de 1000:", math.log(1000, 10))

# log10(x) - Retourne le logarithme base 10 de x
print("Logarithme base 10 de 1000:", math.log10(1000))

# 4. Constantes Mathématiques

# pi - La constante pi (approximativement 3.14159)
print("La constante pi:", math.pi)

# e - La constante e (approximativement 2.71828)
print("La constante e:", math.e)

# tau - La constante tau, égale à 2 * pi (approximativement 6.28318)
print("La constante tau:", math.tau)

# inf - L'infini positif
print("L'infini positif:", math.inf)

# nan - Not-a-Number (NaN)
print("Not-a-Number:", math.nan)

# 5. Fonctions Hyperboliques

# sinh(x) - Retourne le sinus hyperbolique de x
print("Sinus hyperbolique de 1:", math.sinh(1))

# cosh(x) - Retourne le cosinus hyperbolique de x
print("Cosinus hyperbolique de 1:", math.cosh(1))

# tanh(x) - Retourne la tangente hyperbolique de x
print("Tangente hyperbolique de 1:", math.tanh(1))

# asinh(x) - Retourne l'arc sinus hyperbolique de x
print("Arc sinus hyperbolique de 1:", math.asinh(1))

# acosh(x) - Retourne l'arc cosinus hyperbolique de x
print("Arc cosinus hyperbolique de 1:", math.acosh(1))

# atanh(x) - Retourne l'arc tangente hyperbolique de x
print("Arc tangente hyperbolique de 0.5:", math.atanh(0.5))

# 6. Fonctions de Conversion d'Angle

# degrees(x) - Convertit l'angle x de radians en degrés
print("180 radians en degrés:", math.degrees(math.pi))

# radians(x) - Convertit l'angle x de degrés en radians
print("180 degrés en radians:", math.radians(180))

# 7. Exemple Pratique

# Exemple de calcul de l'hypoténuse d'un triangle rectangle avec les côtés de longueur 5 et 12
def calculer_hypotenuse(a, b):
    return math.hypot(a, b)

hypotenuse = calculer_hypotenuse(5, 12)
print("Hypoténuse pour les côtés 5 et 12:", hypotenuse)

# Conclusion

# Le module math est un outil essentiel pour toute application nécessitant des calculs mathématiques en Python. Il offre une vaste gamme de fonctions pour les opérations de base, les fonctions trigonométriques, exponentielles, logarithmiques, et bien plus encore. Comprendre et utiliser ces fonctions peut grandement améliorer l'efficacité et la précision de vos calculs.
