# Cours sur la Programmation Asynchrone en Python

# La programmation asynchrone permet d'écrire du code concurrent sans utiliser les threads ou les processus multiples. 
# En Python, cela se fait principalement à l'aide du module asyncio, introduit dans Python 3.4.

import asyncio

# 1. Introduction à asyncio

# asyncio est une bibliothèque qui fournit un cadre pour l'écriture de code asynchrone en Python. Elle utilise le concept de boucle d'événements (event loop) pour gérer la concurrence.

# 2. Création de Coroutines

# Les coroutines sont des fonctions spéciales qui peuvent suspendre leur exécution pour permettre à d'autres coroutines de s'exécuter. Elles sont définies avec `async def` et sont exécutées avec `await`.

async def saluer():
    print("Bonjour!")
    await asyncio.sleep(1)
    print("Au revoir!")

# 3. Exécution de Coroutines

# Pour exécuter une coroutine, utilisez `asyncio.run()`. Cela démarre la boucle d'événements, exécute la coroutine et ferme la boucle.

asyncio.run(saluer())

# 4. Utilisation de `await`

# L'opérateur `await` est utilisé pour attendre la fin d'une coroutine ou d'une autre opération asynchrone.

async def exemple_await():
    print("Attente de 2 secondes...")
    await asyncio.sleep(2)
    print("Attente terminée.")

asyncio.run(exemple_await())

# 5. Gestion de Plusieurs Coroutines avec `asyncio.gather()`

# `asyncio.gather()` permet de lancer plusieurs coroutines en parallèle et d'attendre leur achèvement.

async def tache_1():
    await asyncio.sleep(1)
    print("Tâche 1 terminée.")

async def tache_2():
    await asyncio.sleep(2)
    print("Tâche 2 terminée.")

async def main():
    await asyncio.gather(tache_1(), tache_2())

asyncio.run(main())

# 6. Utilisation de `asyncio.create_task()`

# `asyncio.create_task()` permet de planifier l'exécution d'une coroutine et de continuer immédiatement sans attendre son achèvement.

async def tache():
    await asyncio.sleep(1)
    print("Tâche terminée.")

async def main():
    tache1 = asyncio.create_task(tache())
    tache2 = asyncio.create_task(tache())
    await tache1
    await tache2

asyncio.run(main())

# 7. Communication Asynchrone avec les Files d'Attente

# `asyncio.Queue` permet une communication sûre entre coroutines.

async def producteur(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produit {i}")
        await asyncio.sleep(1)

async def consommateur(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consommé {item}")
        await asyncio.sleep(2)

async def main():
    queue = asyncio.Queue()
    producer = asyncio.create_task(producteur(queue))
    consumer = asyncio.create_task(consommateur(queue))
    await producer
    await queue.put(None)
    await consumer

asyncio.run(main())

# 8. Gestion des Exceptions

# Les exceptions dans les coroutines doivent être gérées de manière asynchrone.

async def coroutine_avec_exception():
    raise ValueError("Une erreur est survenue")

async def gestion_exceptions():
    try:
        await coroutine_avec_exception()
    except ValueError as e:
        print(f"Exception capturée: {e}")

asyncio.run(gestion_exceptions())

# 9. Exemple Complet: Téléchargement Asynchrone de Fichiers

import aiohttp #module externe

async def telecharger(url, session):
    async with session.get(url) as response:
        contenu = await response.read()
        print(f"Téléchargé {len(contenu)} octets depuis {url}")

async def telechargements(urls):
    async with aiohttp.ClientSession() as session:
        taches = [asyncio.create_task(telecharger(url, session)) for url in urls]
        await asyncio.gather(*taches)

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

asyncio.run(telechargements(urls))

