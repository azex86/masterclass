# Cours sur l'Utilisation des Fichiers en Python et du Module io

# Les Opérations de Base sur les Fichiers

# Ouverture d'un Fichier
# Pour ouvrir un fichier en Python, utilisez la fonction open(). 
# Cette fonction prend deux arguments principaux : le nom du fichier et le mode d'ouverture.

# Modes d'ouverture courants :
# 'r' : Lecture (par défaut).
# 'w' : Écriture (écrase le fichier s'il existe).
# 'a' : Ajout (écriture à la fin du fichier).
# 'b' : Mode binaire (ajoutez à un autre mode, ex : 'rb' pour lecture binaire).
# 't' : Mode texte (par défaut, ajoutez à un autre mode, ex : 'rt' pour lecture en mode texte).

f = open('monfichier.txt', 'r')  # Ouvre le fichier en lecture

# Lecture d'un Fichier
# Une fois le fichier ouvert, vous pouvez lire son contenu de plusieurs manières :

# Lire tout le contenu :
contenu = f.read()
print(contenu)

# Lire une ligne à la fois :
ligne = f.readline()
print(ligne)

# Lire toutes les lignes dans une liste :
lignes = f.readlines()
print(lignes)

# Écriture dans un Fichier
# Pour écrire dans un fichier, vous pouvez utiliser les méthodes write() ou writelines() :

# Écrire une chaîne :
f = open('monfichier.txt', 'w')
f.write('Bonjour, monde!')
f.close()

# Écrire plusieurs lignes :
lignes = ['Première ligne\n', 'Deuxième ligne\n']
f = open('monfichier.txt', 'w')
f.writelines(lignes)
f.close()

# Fermeture d'un Fichier
# Il est important de fermer le fichier après avoir terminé les opérations :
f.close()

# Utilisation du Gestionnaire de Contexte
# Utilisez le gestionnaire de contexte (with statement) pour ouvrir et fermer automatiquement le fichier, même en cas d'erreur :
with open('monfichier.txt', 'r') as f:
    contenu = f.read()
    print(contenu)


# Utilisation Avancée avec le Module io

# Le module io en Python fournit les outils pour travailler avec des flux de données, permettant une gestion plus fine des entrées/sorties.

# Types de Flux dans io
# io.StringIO : Utilisé pour lire et écrire des chaînes de caractères en mémoire (utile pour les tests).
# io.BytesIO : Utilisé pour lire et écrire des données binaires en mémoire.

# Exemple avec io.StringIO
import io

# Création d'un objet StringIO
f = io.StringIO()
f.write('Bonjour, monde!\n')
f.write('Ceci est un test.')

# Revenir au début du flux pour lire son contenu
f.seek(0)
contenu = f.read()
print(contenu)

f.close()

# Exemple avec io.BytesIO
import io

# Création d'un objet BytesIO
f = io.BytesIO()
f.write(b'Hello, world!\n')
f.write(b'This is a test.')

# Revenir au début du flux pour lire son contenu
f.seek(0)
contenu = f.read()
print(contenu)

f.close()

# Exemples de Manipulations Courantes de Fichiers

# Copier un Fichier
def copier_fichier(source, destination):
    with open(source, 'rb') as fsrc:
        with open(destination, 'wb') as fdst:
            fdst.write(fsrc.read())

copier_fichier('source.txt', 'destination.txt')


# un fichier CSV est un fichier texte dont chaque ligne contient des données séparées par un caractère particulier en général ';'
# Exemple : 
#   Ville;departement;nb_habitant;superficie(en Km²)
#   Tours;37;136000;36.67
#   Limoges;87;129760;77,45

# Lire un Fichier CSV
import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  #row = ["Ville","departement","nb_habitant","superficie(en Km²)"] puis ["Tours","37","136000","36.67"] puis ["Limoges",.....] 

# Écrire dans un Fichier CSV
import csv

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nom', 'Age', 'Ville'])
    writer.writerow(['Alice', 30, 'Paris'])
    writer.writerow(['Bob', 25, 'Londres'])

