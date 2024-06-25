# Cours sur l'Utilisation du Module time en Python

# Le module time en Python fournit diverses fonctions liées au temps, 
# telles que la manipulation de l'heure actuelle, 
# la mesure de la durée d'exécution d'un programme et le formatage des dates et des heures. 
# Ce module est essentiel pour travailler avec des données temporelles, 
# réaliser des pauses dans les programmes et mesurer les performances.

import time

# 1. Obtenir l'Heure Actuelle

# time() - Retourne le temps actuel en secondes depuis l'époque (le 1er janvier 1970 00:00:00 UTC)
temps_actuel = time.time()
print("Temps actuel en secondes depuis l'époque:", temps_actuel)

# ctime([secs]) - Convertit un temps exprimé en secondes depuis l'époque en une chaîne de caractères représentant l'heure locale
heure_actuelle = time.ctime(temps_actuel)
print("Heure actuelle formatée:", heure_actuelle) #Heure actuelle formatée: Mon Jun 24 12:27:04 2024

# localtime([secs]) - Convertit un temps exprimé en secondes depuis l'époque en une struct_time représentant l'heure locale
heure_locale = time.localtime(temps_actuel)
print("Struct_time pour l'heure locale:", heure_locale)

# gmtime([secs]) - Convertit un temps exprimé en secondes depuis l'époque en une struct_time représentant l'heure UTC
heure_utc = time.gmtime(temps_actuel)
print("Struct_time pour l'heure UTC:", heure_utc)

# 2. Formatage des Dates et des Heures

# strftime(format[, t]) - Convertit une struct_time ou un tuple en une chaîne de caractères selon le format spécifié
format_heure = time.strftime("%Y-%m-%d %H:%M:%S", heure_locale)
print("Heure formatée (local):", format_heure)

# strptime(string, format) - Convertit une chaîne de caractères représentant une date/heure en une struct_time selon le format spécifié
date_str = "2024-06-24 14:30:00"
date_struct = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Struct_time à partir de la chaîne de caractères:", date_struct)

# 3. Mesurer le Temps

# perf_counter() - Retourne le compteur de performance le plus précis disponible, utile pour mesurer des intervalles de temps courts
debut = time.perf_counter()
# Simuler un délai
time.sleep(1)
fin = time.perf_counter()
print("Durée mesurée (en secondes):", fin - debut)

# sleep(secs) - Suspend l'exécution du programme pour le nombre de secondes spécifié
print("Attente de 2 secondes...")
time.sleep(2)
print("Fin de l'attente.")

# 4. Manipuler le Temps

# mktime(t) - Convertit une struct_time ou un tuple représentant l'heure locale en un nombre de secondes depuis l'époque
secondes = time.mktime(heure_locale)
print("Secondes depuis l'époque à partir de struct_time:", secondes)

# 5. Exemple Pratique

# Exemple de chronomètre simple
def chronometre():
    input("Appuyez sur Entrée pour commencer le chronomètre.")
    debut = time.perf_counter()
    input("Appuyez sur Entrée pour arrêter le chronomètre.")
    fin = time.perf_counter()
    print("Temps écoulé: {:.2f} secondes".format(fin - debut))

chronometre()


# Résumé des fonctions importantes
# time.time()
# time.sleep(sec)
# time.perf_counter() 