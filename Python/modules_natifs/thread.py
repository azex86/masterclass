# Cours sur le Module threading et les Threads en Python

# Le multithreading permet à un programme Python d'exécuter plusieurs threads (légers sous-processus) en parallèle. 
# Le module threading fournit une interface pour travailler avec les threads, offrant des outils pour créer, gérer et synchroniser les threads.

import threading
import time

# 1. Concepts de Base du Multithreading

# Un thread est une séquence d'exécution distincte. En Python, le module threading permet de créer et de gérer des threads.

# 2. Création et Démarrage de Threads

# Pour créer un thread, utilisez la classe Thread du module threading. Le thread peut exécuter une fonction cible ou une méthode d'un objet.

def fonction_de_thread():
    print("Thread démarré.")
    time.sleep(2)
    print("Thread terminé.")

# Création d'un thread
thread = threading.Thread(target=fonction_de_thread)

# Démarrage du thread
thread.start()

# Attente de la fin du thread
thread.join()
print("Thread principal terminé.")

# 3. Utilisation de Classes pour les Threads

# Vous pouvez également créer des threads en sous-classant la classe Thread et en redéfinissant la méthode run().

class MonThread(threading.Thread):
    def __init__(self, nom):
        threading.Thread.__init__(self)
        self.nom = nom

    def run(self):
        print(f"Thread {self.nom} démarré.")
        time.sleep(2)
        print(f"Thread {self.nom} terminé.")

# Création et démarrage d'un thread en utilisant une classe
thread1 = MonThread("A")
thread2 = MonThread("B")
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# 4. Synchronisation des Threads

# La synchronisation est nécessaire pour éviter les conditions de course (race conditions) où plusieurs threads accèdent aux mêmes ressources simultanément. 
# Les verrous (locks) sont utilisés pour garantir que seul un thread peut accéder à une ressource à la fois.

# Utilisation d'un verrou pour protéger une ressource partagée

verrou = threading.Lock()
compteur = 0

def incrementer():
    global compteur
    with verrou:
        local_compteur = compteur
        local_compteur += 1
        time.sleep(0.1)
        compteur = local_compteur

threads = []
for _ in range(10):
    thread = threading.Thread(target=incrementer)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Valeur finale du compteur:", compteur)

# 5. Autres Outils de Synchronisation

# Le module threading fournit d'autres outils de synchronisation comme les événements (events), les sémaphores (semaphores) et les barrières (barriers).

# 5.1 Utilisation d'un Événement

# Un événement permet de signaler à un ou plusieurs threads qu'un certain événement s'est produit.

event = threading.Event()

def attendre_evenement():
    print("Attente de l'événement...")
    event.wait()
    print("Événement reçu!")

thread = threading.Thread(target=attendre_evenement)
thread.start()

print("Déclenchement de l'événement après 2 secondes.")
time.sleep(2)
event.set()
thread.join()

# 5.2 Utilisation d'un Sémaphore

# Un sémaphore contrôle l'accès à une ressource partagée avec un compteur, permettant à un nombre limité de threads d'accéder à la ressource en même temps.

semaphore = threading.Semaphore(3)

def tache():
    with semaphore:
        print(f"Thread {threading.current_thread().name} commence.")
        time.sleep(2)
        print(f"Thread {threading.current_thread().name} termine.")

threads = [threading.Thread(target=tache, name=f"T-{i}") for i in range(6)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# 5.3 Utilisation d'une Barrière

# Une barrière synchronise un ensemble de threads à un point particulier, assurant qu'aucun thread ne continue avant que tous les threads aient atteint ce point.

barrier = threading.Barrier(3)

def tache_avec_barriere():
    print(f"Thread {threading.current_thread().name} atteint la barrière.")
    barrier.wait()
    print(f"Thread {threading.current_thread().name} franchit la barrière.")

threads = [threading.Thread(target=tache_avec_barriere, name=f"T-{i}") for i in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# 6. Communication Entre Threads

# Utilisation des files de messages (queues) pour la communication sécurisée entre les threads.

from queue import Queue

def producteur(queue):
    for i in range(5):
        item = f"item-{i}"
        queue.put(item)
        print(f"Produit {item}")
        time.sleep(1)

def consommateur(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consommé {item}")
        time.sleep(2)

queue = Queue()
thread_producer = threading.Thread(target=producteur, args=(queue,))
thread_consumer = threading.Thread(target=consommateur, args=(queue,))
thread_producer.start()
thread_consumer.start()
thread_producer.join()
queue.put(None)
thread_consumer.join()

# 7. Gestion des Exceptions dans les Threads

# Les exceptions dans les threads peuvent être difficiles à gérer. Il est souvent nécessaire de capturer les exceptions dans le thread et de les remonter au thread principal.

def thread_avec_exception():
    try:
        raise ValueError("Une erreur s'est produite dans le thread.")
    except Exception as e:
        print(f"Exception capturée dans le thread: {e}")

thread = threading.Thread(target=thread_avec_exception)
thread.start()
thread.join()

# 8. Performance et Limites du Multithreading en Python

# En raison du Global Interpreter Lock (GIL) de Python, les threads ne peuvent pas véritablement s'exécuter en parallèle sur plusieurs cœurs de CPU. 
# Pour les tâches liées au CPU, le multiprocessing peut être une meilleure alternative.
