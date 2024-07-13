"""
NumPy (Numerical Python) est une bibliothèque fondamentale pour la programmation scientifique en Python. Voici les principaux usages et intérêts de NumPy :
Usages de NumPy :

    Manipulation de tableaux multidimensionnels (ndarrays) :
        NumPy permet de créer et de manipuler des tableaux (arrays) de données multidimensionnels, qui sont plus efficaces et flexibles que les listes Python natives.

    Opérations mathématiques et algébriques :
        NumPy propose une large gamme de fonctions mathématiques, notamment pour les opérations élémentaires (addition, soustraction, multiplication, division) ainsi que pour des opérations plus complexes (exponentiation, logarithmes, fonctions trigonométriques).

    Traitement de données :
        Les capacités de manipulation de données de NumPy permettent de nettoyer, transformer et analyser des ensembles de données de grande taille de manière efficace.

    Génération de données aléatoires :
        NumPy inclut un sous-module, numpy.random, qui permet de générer des nombres aléatoires pour la simulation et les tests statistiques.

    Algèbre linéaire :
        NumPy inclut des fonctions pour effectuer des opérations d'algèbre linéaire telles que la multiplication de matrices, la décomposition en valeurs singulières (SVD), la résolution de systèmes linéaires, etc.

    Intégration avec d'autres bibliothèques :
        NumPy est souvent utilisé conjointement avec d'autres bibliothèques scientifiques en Python telles que SciPy, pandas, Matplotlib, et scikit-learn, facilitant l’analyse de données, le machine learning, et la visualisation de données.

Intérêts de NumPy :

    Performance :
        Les tableaux NumPy sont plus compacts que les listes Python natives. Les opérations sur ces tableaux sont également beaucoup plus rapides grâce à leur implémentation en C, ce qui réduit l'overhead du langage Python.

    Facilité d’utilisation :
        NumPy fournit une syntaxe simple et claire pour effectuer des opérations complexes sur des tableaux de données.

    Interopérabilité :
        Les tableaux NumPy peuvent être utilisés avec des programmes écrits dans d'autres langages tels que C, C++, et Fortran. Ils peuvent aussi être utilisés comme des objets tampon (buffer objects) en Python.

    Ecosystème riche :
        NumPy est au cœur de l'écosystème scientifique et analytique en Python. De nombreuses autres bibliothèques se basent sur NumPy pour leurs propres structures de données et algorithmes.

    Communauté et documentation :
        NumPy bénéficie d'une vaste communauté d'utilisateurs et de développeurs, ainsi que d'une documentation exhaustive et de nombreux tutoriels disponibles en ligne.
"""



"""     
Qu'est-ce qu'un tableau NumPy ?

Un tableau NumPy, également appelé ndarray (N-dimensional array), est une structure de données centrale dans la bibliothèque NumPy.
Très similaire au liste python, les tableaux numpy sont cependant de taille fixe et continennent des valeurs numériques uniquement. 
Contrairement aux listes Python natives, les tableaux NumPy sont optimisés pour effectuer des opérations mathématiques et statistiques sur des grandes quantités de données de manière efficace.

Attributs des tableaux NumPy

Les tableaux NumPy possèdent plusieurs attributs importants qui facilitent leur manipulation :

    Shape (forme) :
        L'attribut shape d'un tableau NumPy retourne une tuple représentant les dimensions du tableau. Par exemple, un tableau de 2 lignes et 3 colonnes aura une forme de (2, 3).
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # (2, 3)

#Size (taille) :

#    L'attribut size donne le nombre total d'éléments dans le tableau.
print(arr.size)  # 6

#dtype (type de données) :

#    L'attribut dtype indique le type de données des éléments dans le tableau (par exemple, int32, float64, etc.).
print(arr.dtype)  # int64

#ndim (nombre de dimensions) :

#    L'attribut ndim donne le nombre de dimensions (ou d'axes) du tableau.
print(arr.ndim)  # 2

"""
Vitesse des tableaux NumPy

Les tableaux NumPy sont beaucoup plus rapides et plus économes en mémoire que les listes Python pour plusieurs raisons :

    Allocation contiguë de mémoire :
        Les éléments des tableaux NumPy sont stockés dans des blocs de mémoire contigus, ce qui permet un accès plus rapide aux éléments et une utilisation plus efficace de la mémoire cache du processeur.

    Typage homogène :
        Contrairement aux listes Python qui peuvent contenir des éléments de différents types, tous les éléments d'un tableau NumPy sont du même type. Cela permet d'optimiser les opérations mathématiques et d'éviter les vérifications de type coûteuses.

    Opérations vectorisées :
        NumPy permet d'effectuer des opérations mathématiques sur des tableaux entiers sans boucles explicites en Python, grâce à la vectorisation. Cela tire parti des optimisations au niveau bas, souvent implémentées en C, pour améliorer les performances.
"""


#Initialisation des tableaux NumPy

#Il existe plusieurs façons d'initialiser des tableaux NumPy, selon les besoins :

#    À partir de listes Python :
arr = np.array([1, 2, 3, 4, 5])

#Tableaux de zéros :
zeros = np.zeros((2, 3))

#Tableaux de uns :
ones = np.ones((3, 4))

#Tableaux vides (sans initialisation spécifique) :
empty = np.empty((2, 2))

#Tableaux avec une séquence de nombres :
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

#Tableaux de nombres également espacés :
linspace = np.linspace(0, 1, 5)  # [0. , 0.25, 0.5 , 0.75, 1. ]

#Tableaux d'identité :
identity = np.eye(3)  # Matrice identité 3x3

#Tableaux aléatoires :
random_array = np.random.rand(3, 3)  # Matrice 3x3 avec des valeurs
        
"""        
Accès aux données des tableaux NumPy

Accéder aux données dans les tableaux NumPy est une opération courante et essentielle pour manipuler et analyser des données. NumPy offre plusieurs moyens efficaces pour accéder aux éléments des tableaux, y compris l'indexation, le slicing, l'indexation avancée et le masquage.
Indexation des tableaux NumPy

L'indexation permet d'accéder à un élément spécifique dans un tableau NumPy en utilisant des indices. L'indexation commence toujours à 0 en NumPy, comme en Python.
"""
#Exemple de base :
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # Accès au premier élément: 1
print(arr[4])  # Accès au dernier élément: 5

#Pour les tableaux multidimensionnels, plusieurs indices sont nécessaires :
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat[0, 0])  # Accès à l'élément en première ligne, première colonne: 1
print(mat[1, 2])  # Accès à l'élément en deuxième ligne, troisième colonne: 6

#Slicing (Tranche)

#Le slicing permet de sélectionner des sous-ensembles de tableaux en utilisant des intervalles. La syntaxe est start:stop:step.
#Exemple de slicing :
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # [2 3 4]
print(arr[:3])   # [1 2 3]
print(arr[::2])  # [1 3 5]

#Pour les tableaux multidimensionnels, le slicing peut être appliqué à chaque dimension :
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat[:2, 1:3])  # Sélectionne un sous-tableau
# [[2 3]
#  [5 6]]

#Indexation avancée

#L'indexation avancée permet de sélectionner des éléments spécifiques à l'aide de tableaux d'indices.
#Exemple d'indexation par tableaux d'indices :
arr = np.array([10, 20, 30, 40, 50])
indices = np.array([0, 2, 4])
print(arr[indices])  # [10 30 50]

#Pour les tableaux multidimensionnels, l'indexation avancée peut être utilisée de manière similaire :
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([2, 1, 0])
print(mat[row_indices, col_indices])  # [3 5 7]

#Masquage (Indexation booléenne)

#Le masquage permet de sélectionner des éléments d'un tableau en utilisant une condition logique.
#Exemple de masquage :
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
print(arr[mask])  # [4 5]

#Pour les tableaux multidimensionnels :
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = mat > 5
print(mat[mask])  # [6 7 8 9]

#Modification des éléments via l'indexation

#Les éléments des tableaux NumPy peuvent être modifiés en utilisant les mêmes techniques d'indexation.
#Exemple de modification :
arr = np.array([1, 2, 3, 4, 5])
arr[0] = 10
print(arr)  # [10  2  3  4  5]

mat = np.array([[1, 2, 3], [4, 5, 6]])
mat[1, 2] = 10
print(mat)
# [[ 1  2  3]
#  [ 4  5 10]]




"""
Opérations sur les tableaux NumPy

NumPy est spécialement conçu pour effectuer des opérations mathématiques et logiques sur des tableaux de manière efficace. Il permet d'effectuer des opérations élémentaires, de l'algèbre linéaire, des transformations de tableaux et bien plus encore.
Opérations élémentaires

Les opérations élémentaires peuvent être effectuées de manière vectorisée sur des tableaux NumPy, ce qui est à la fois rapide et concis.
Addition, soustraction, multiplication, division :
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # [5 7 9]
print(arr1 - arr2)  # [-3 -3 -3]
print(arr1 * arr2)  # [4 10 18]
print(arr1 / arr2)  # [0.25 0.4  0.5 ]

#Opérations scalaires

#Les opérations peuvent également être effectuées entre un tableau et un scalaire.
print(arr1 + 10)  # [11 12 13]
print(arr1 * 2)   # [2 4 6]

#Fonctions universelles (ufuncs)

#NumPy fournit des fonctions mathématiques universelles qui opèrent sur des tableaux élément par élément.
#Exemples de fonctions universelles :
print(np.sqrt(arr1))     # [1.         1.41421356 1.73205081]
print(np.exp(arr1))      # [ 2.71828183  7.3890561  20.08553692]
print(np.sin(arr1))      # [0.84147098 0.90929743 0.14112001]

#Agrégation

#Les fonctions d'agrégation permettent de résumer les données dans un tableau.
#Exemples de fonctions d'agrégation :
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(np.sum(arr))       # 21
print(np.mean(arr))      # 3.5
print(np.max(arr))       # 6
print(np.min(arr))       # 1
print(np.std(arr))       # 1.707825127659933

#Opérations le long des axes

#Les opérations d'agrégation peuvent être effectuées le long de dimensions spécifiques (axes).
print(np.sum(arr, axis=0))  # [5 7 9] (somme de chaque colonne)
print(np.sum(arr, axis=1))  # [ 6 15] (somme de chaque ligne)

#Algèbre linéaire

#NumPy inclut un module pour les opérations d'algèbre linéaire (numpy.linalg).
#Produit matriciel :
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

print(np.dot(mat1, mat2))
# [[19 22]
#  [43 50]]

#Déterminant et inverse de matrice :
print(np.linalg.det(mat1))   # -2.0000000000000004
print(np.linalg.inv(mat1))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

#Opérations logiques

#Les opérations logiques permettent de comparer des tableaux et de créer des masques booléens.
#Exemples d'opérations logiques :
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 2, 1])

print(arr1 > arr2)   # [False False  True]
print(arr1 == arr2)  # [False  True False]

#Utilisation de masques booléens :
mask = arr1 > 2
print(arr1[mask])  # [3]

#Broadcasting

#Le broadcasting est une technique qui permet à NumPy d'effectuer des opérations sur des tableaux de formes différentes.
#Exemple de broadcasting :
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print(arr + scalar)
# [[11 12 13]
#  [14 15 16]]

#Broadcasting avec tableaux de différentes dimensions :
arr1 = np.array([1, 2, 3])
arr2 = np.array([[0], [1], [2]])

print(arr1 + arr2)
# [[1 2 3]
#  [2 3 4]
#  [3 4 5]]

#Manipulation de tableaux

#NumPy offre plusieurs fonctions pour modifier la forme et la structure des tableaux.
#Transposition :
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]

#Changement de forme :
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape((2, 3)))
# [[1 2 3]
#  [4 5 6]]

#Concaténation et empilement :
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(np.concatenate((arr1, arr2), axis=0))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(np.vstack((arr1, arr2)))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(np.hstack((arr1, arr2)))
# [[1 2 5 6]
#  [3 4 7 8]]




# Copy vs. View

# Lorsqu'on manipule des tableaux, il est important de comprendre la différence entre une copie et une vue. 
# Une vue est un tableau qui partage les mêmes données que l'original, tandis qu'une copie est un tableau distinct avec ses propres données.
# Exemple de vue :
arr = np.array([1, 2, 3, 4, 5])
view = arr[1:3]
view[0] = 10
print(arr)  # [ 1 10  3  4  5]

#Exemple de copie :
arr = np.array([1, 2, 3, 4, 5])
copy = arr[1:3].copy()
copy[0] = 10
print(arr)  # [1 2 3 4 5]