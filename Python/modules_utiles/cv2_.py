# -*- coding: utf-8 -*-
"""
Cours sur l'utilisation du module cv2 (OpenCV)
Pour le traitement d'image et de vidéo
"""

# Importation du module cv2
import cv2

# Chargement et affichage d'une image
# Utilisation de la fonction cv2.imread() pour charger une image depuis un fichier
image = cv2.imread('chemin/vers/votre/image.jpg')

# Vérification si l'image est chargée correctement
if image is None:
    print('Impossible de charger l\'image.')
else:
    # Affichage de l'image dans une fenêtre
    cv2.imshow('Image originale', image)
    cv2.waitKey(0)  # Attente indéfinie jusqu'à ce qu'une touche soit pressée
    cv2.destroyAllWindows()  # Fermeture de toutes les fenêtres ouvertes

# Conversion de l'image en niveaux de gris
image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Affichage de l'image en niveaux de gris
cv2.imshow('Image en niveaux de gris', image_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Redimensionnement de l'image
largeur = 300
hauteur = 200
image_redimensionnee = cv2.resize(image, (largeur, hauteur))

# Affichage de l'image redimensionnée
cv2.imshow('Image redimensionnée', image_redimensionnee)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Enregistrement d'une nouvelle image
cv2.imwrite('nouvelle_image.jpg', image_redimensionnee)
print('Nouvelle image enregistrée.')

# Exemple d'utilisation d'une vidéo en direct depuis la webcam
capture = cv2.VideoCapture(0)  # Ouvre la webcam par défaut (index 0)
#capture = cv2.VideoCapture("file.mp4") #ouvre une vidéo depuis le disque


while capture.isOpened():
    ret, frame = capture.read()  # Lecture d'une frame depuis la webcam

    cv2.imshow('Video depuis la webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Attend la touche 'q' pour quitter la boucle
        break

capture.release()  # Libération de la ressource de la webcam
cv2.destroyAllWindows()

# Exemple de dessin sur une image
image_dessin = image.copy()  # Crée une copie de l'image originale pour le dessin

# Dessine un rectangle
cv2.rectangle(image_dessin, (100, 50), (300, 200), (0, 255, 0), 2)  # Coordonnées, couleur, épaisseur

# Dessine un cercle
cv2.circle(image_dessin, (400, 200), 50, (255, 0, 0), -1)  # Centre, rayon, couleur, rempli (-1)

# Dessine un texte
cv2.putText(image_dessin, 'Exemple de dessin', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Affichage de l'image avec dessins
cv2.imshow('Image avec dessins', image_dessin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exemple de détection de visage avec un classifieur pré-entraîné
cascade_visage = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Convertir l'image en niveaux de gris pour la détection
image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détection des visages
visages = cascade_visage.detectMultiScale(image_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dessiner des rectangles autour des visages détectés
for (x, y, w, h) in visages:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Affichage de l'image avec les visages détectés
cv2.imshow('Visages détectés', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
