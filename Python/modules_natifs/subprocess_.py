# Cours sur le Module subprocess en Python

# Le module subprocess en Python permet de créer de nouveaux processus, 
# de se connecter à leurs canaux d'entrée/sortie/erreur et d'obtenir leurs codes de retour. 
# Il est utilisé pour exécuter des commandes du système et interagir avec d'autres programmes.

import subprocess

# 1. Exécution de Commandes Simples

# run(args, *, capture_output=False, text=False, input=None, timeout=None, check=False, **other_popen_kwargs)
# Exécute une commande spécifiée par args. C'est la fonction la plus simple pour exécuter une commande.
# elle attend que le processus se termine avant de continuer le programme

resultat = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print("Sortie de la commande 'ls -l':")
print(resultat.stdout)

# 2. Popen pour une Communication Plus Complexe

# Popen est une classe qui permet de lancer un processus et de communiquer avec lui via ses canaux stdin, stdout et stderr.

process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
print("Sortie standard:")
print(stdout)
print("Erreur standard:")
print(stderr)

# 3. Exécution de Commandes avec Entrée Utilisateur

# On peut envoyer des données à l'entrée standard du processus en utilisant l'argument stdin de Popen.

process = subprocess.Popen(['python3'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate(input="print('Bonjour, monde!')\n")
print("Sortie standard après envoi de commande Python:")
print(stdout)

# 4. Capturer la Sortie d'Erreur

# Pour capturer l'erreur standard, utilisez stderr=subprocess.PIPE.

process = subprocess.Popen(['ls', '/chemin/invalide'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()
print("Sortie standard:")
print(stdout)
print("Erreur standard:")
print(stderr)

# 5. Timeout et Gestion des Erreurs

# run() avec l'option check=True lancera une exception CalledProcessError si la commande retourne un code d'erreur non nul.

try:
    resultat = subprocess.run(['sleep', '2'], timeout=1)
except subprocess.TimeoutExpired:
    print("La commande a expiré.")

try:
    resultat = subprocess.run(['ls', '/chemin/invalide'], check=True)
except subprocess.CalledProcessError as e:
    print(f"La commande a échoué avec le code {e.returncode} et le message d'erreur suivant:\n{e.stderr}")

# 6. Exécution de Commandes Shell

# Pour exécuter des commandes shell, définissez shell=True. Soyez prudent avec cette option pour éviter les vulnérabilités liées à l'injection de commandes.

resultat = subprocess.run('echo $HOME', shell=True, capture_output=True, text=True)
print("Sortie de la commande shell 'echo $HOME':")
print(resultat.stdout)
