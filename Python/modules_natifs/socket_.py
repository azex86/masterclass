# Cours sur les Sockets en Python

# Les sockets sont un moyen de communication entre deux machines connectées via un réseau. 
# Le module socket en Python fournit une interface pour les sockets de bas niveau, 
# permettant de créer des applications réseau comme des clients et des serveurs.

import socket

# 1. Concepts de Base des Sockets

# Une socket est une extrémité de communication permettant l'envoi et la réception de données. 
# Les sockets peuvent être utilisées pour créer des connexions TCP (orientées connexion) ou UDP (sans connexion).

# 2. Création d'un Serveur TCP

# Exemple de création d'un serveur TCP qui écoute les connexions entrantes et envoie une réponse.

def serveur_tcp():
    # Création de la socket
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Liaison de la socket à une adresse et un port
    serveur_socket.bind(('localhost', 12345))
    
    # Écoute des connexions entrantes
    serveur_socket.listen(5)
    print("Serveur en écoute sur le port 12345...")
    
    # Acceptation des connexions entrantes
    while True:
        client_socket, adresse_client = serveur_socket.accept()
        print(f"Connexion établie avec {adresse_client}")
        
        # Réception et envoi de données
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Données reçues: {data}")
        client_socket.send("Bonjour, client!".encode('utf-8'))
        
        # Fermeture de la connexion
        client_socket.close()

# 3. Création d'un Client TCP

# Exemple de création d'un client TCP qui se connecte à un serveur, envoie des données et reçoit une réponse.

def client_tcp():
    # Création de la socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connexion au serveur
    client_socket.connect(('localhost', 12345))
    
    # Envoi de données
    client_socket.send("Bonjour, serveur!".encode('utf-8'))
    
    # Réception de la réponse
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Réponse du serveur: {data}")
    
    # Fermeture de la connexion
    client_socket.close()

# 4. Création d'un Serveur UDP

# Exemple de création d'un serveur UDP qui écoute les paquets entrants et envoie une réponse.

def serveur_udp():
    # Création de la socket
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Liaison de la socket à une adresse et un port
    serveur_socket.bind(('localhost', 12345))
    print("Serveur UDP en écoute sur le port 12345...")
    
    # Réception des paquets
    while True:
        data, adresse_client = serveur_socket.recvfrom(1024)
        print(f"Données reçues de {adresse_client}: {data.decode('utf-8')}")
        serveur_socket.sendto("Bonjour, client!".encode('utf-8'), adresse_client)

# 5. Création d'un Client UDP

# Exemple de création d'un client UDP qui envoie des données à un serveur et reçoit une réponse.

def client_udp():
    # Création de la socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Envoi de données
    client_socket.sendto("Bonjour, serveur!".encode('utf-8'), ('localhost', 12345))
    
    # Réception de la réponse
    data, serveur = client_socket.recvfrom(1024)
    print(f"Réponse du serveur: {data.decode('utf-8')}")
    
    # Fermeture de la socket
    client_socket.close()

# 6. Utilisation des Sockets Non-Bloquantes

# Les sockets peuvent être mises en mode non-bloquant pour permettre des opérations d'E/S sans attendre la disponibilité des données.

def socket_non_bloquante():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setblocking(False)
    try:
        client_socket.connect(('localhost', 12345))
    except BlockingIOError:
        pass
    
    # Utilisation de la boucle de vérification
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(f"Données reçues: {data.decode('utf-8')}")
                break
        except BlockingIOError:
            pass
        # Faire d'autres tâches pendant l'attente
        print("En attente de données...")

# 7. Sécurisation des Sockets avec SSL

# Le module ssl permet de sécuriser les connexions socket avec SSL/TLS.

import ssl

def serveur_tcp_ssl():
    # Création de la socket
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur_socket.bind(('localhost', 12345))
    serveur_socket.listen(5)
    
    # Wrapping de la socket avec SSL
    contexte = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    serveur_socket_ssl = contexte.wrap_socket(serveur_socket, server_side=True)
    
    print("Serveur SSL en écoute sur le port 12345...")
    while True:
        client_socket, adresse_client = serveur_socket_ssl.accept()
        print(f"Connexion SSL établie avec {adresse_client}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Données reçues: {data}")
        client_socket.send("Bonjour, client SSL!".encode('utf-8'))
        client_socket.close()

def client_tcp_ssl():
    # Création de la socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrapping de la socket avec SSL
    contexte = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    client_socket_ssl = contexte.wrap_socket(client_socket, server_hostname='localhost')
    
    # Connexion au serveur
    client_socket_ssl.connect(('localhost', 12345))
    client_socket_ssl.send("Bonjour, serveur SSL!".encode('utf-8'))
    data = client_socket_ssl.recv(1024).decode('utf-8')
    print(f"Réponse du serveur SSL: {data}")
    client_socket_ssl.close()

# 8. Gestion des Exceptions

# Il est important de gérer les exceptions lors de l'utilisation des sockets pour gérer les erreurs réseau et autres problèmes.

def gestion_exceptions_socket():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))
        client_socket.send("Bonjour, serveur!".encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Réponse du serveur: {data}")
        client_socket.close()
    except socket.error as e:
        print(f"Erreur de socket: {e}")
    except Exception as e:
        print(f"Erreur générale: {e}")

