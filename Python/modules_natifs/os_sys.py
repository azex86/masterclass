# Cours sur les Modules os et sys en Python

# Les modules os et sys en Python offrent des interfaces pour interagir avec le système d'exploitation et gérer les paramètres du système.
# Ces modules sont essentiels pour les tâches liées à la gestion des fichiers, des répertoires, des variables d'environnement, et pour interagir avec l'interpréteur Python lui-même.

import os
import sys

# 1. Le Module os

# Le module os fournit une manière portable d'utiliser les fonctionnalités dépendantes du système d'exploitation.

# 1.1 Gestion des Fichiers et Répertoires

# getcwd() - Retourne le répertoire de travail actuel
repertoire_actuel = os.getcwd()
print("Répertoire de travail actuel:", repertoire_actuel)

# chdir(path) - Change le répertoire de travail actuel
os.chdir('/tmp')
print("Nouveau répertoire de travail:", os.getcwd())

# listdir(path='.') - Liste les fichiers et répertoires dans le répertoire spécifié
fichiers = os.listdir('.')
print("Liste des fichiers dans le répertoire courant:", fichiers)

# mkdir(path) - Crée un nouveau répertoire
os.mkdir('nouveau_repertoire')

# rmdir(path) - Supprime un répertoire (doit être vide)
os.rmdir('nouveau_repertoire')

# remove(path) - Supprime un fichier
# os.remove('fichier_a_supprimer.txt')

# 1.2 Gestion des Chemins de Fichiers

# path.join(path, *paths) - Combine un ou plusieurs composants de chemin
chemin_complet = os.path.join('/tmp', 'nouveau_repertoire', 'fichier.txt')
print("Chemin complet:", chemin_complet)

# path.exists(path) - Vérifie si un chemin existe
existe = os.path.exists(chemin_complet)
print("Le chemin existe-t-il?", existe)

# path.isdir(path) - Vérifie si un chemin est un répertoire
est_repertoire = os.path.isdir('/tmp')
print("Est-ce un répertoire?", est_repertoire)

# path.isfile(path) - Vérifie si un chemin est un fichier
est_fichier = os.path.isfile('/tmp/fichier.txt')
print("Est-ce un fichier?", est_fichier)

# 1.3 Variables d'Environnement

# getenv(key, default=None) - Retourne la valeur d'une variable d'environnement
python_path = os.getenv('PYTHONPATH', 'Non défini')
print("PYTHONPATH:", python_path)

# environ - Un dictionnaire contenant les variables d'environnement
variables_environnement = os.environ
print("Variables d'environnement:", variables_environnement)

# 2. Le Module sys

# Le module sys fournit des fonctions et des variables pour interagir avec l'interpréteur Python.

# 2.1 Arguments de la Ligne de Commande

# argv - Une liste contenant les arguments de la ligne de commande
print("Arguments de la ligne de commande:", sys.argv)

# 2.2 Sortie et Erreur Standard

# stdout - Flux de sortie standard
sys.stdout.write("Ceci est une sortie standard.\n")

# stderr - Flux d'erreur standard
sys.stderr.write("Ceci est une erreur standard.\n")

# 2.3 Gestion de l'Interpréteur

# exit([arg]) - Termine l'interpréteur Python
# sys.exit("Arrêt du programme.")

# version - Version de l'interpréteur Python
print("Version de Python:", sys.version)

# path - Une liste des chemins où Python recherche les modules
print("Chemins de recherche des modules:", sys.path)

# 3. Exemple Pratique

# Un script qui affiche des informations sur le système

def afficher_infos_systeme():
    print("Répertoire de travail actuel:", os.getcwd())
    print("Liste des fichiers dans le répertoire courant:", os.listdir('.'))
    print("Version de Python:", sys.version)
    print("Arguments de la ligne de commande:", sys.argv)

afficher_infos_systeme()

