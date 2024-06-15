#include <stdio.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 8080
#define MAX_BUFFER_SIZE 1024

int main() {
    WSADATA wsaData;
    SOCKET serverSocket, clientSocket;
    struct sockaddr_in serverAddress, clientAddress;
    int clientAddressLength = sizeof(clientAddress);
    char buffer[MAX_BUFFER_SIZE];

    // Initialisation de Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("Erreur lors de l'initialisation de Winsock.\n");
        return 1;
    }

    // Création du socket
    if ((serverSocket = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Erreur lors de la création du socket.\n");
        WSACleanup();
        return 1;
    }

    // Configuration de l'adresse du serveur
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = INADDR_ANY;
    serverAddress.sin_port = htons(PORT);

    // Liaison du socket à l'adresse du serveur
    if (bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == SOCKET_ERROR) {
        printf("Erreur lors de la liaison du socket.\n");
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    // Mise en écoute du socket
    if (listen(serverSocket, SOMAXCONN) == SOCKET_ERROR) {
        printf("Erreur lors de la mise en écoute du socket.\n");
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    printf("Serveur en écoute sur le port %d...\n", PORT);

    // Attente de la connexion d'un client
    if ((clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddress, &clientAddressLength)) == INVALID_SOCKET) {
        printf("Erreur lors de l'acceptation de la connexion.\n");
        closesocket(serverSocket);
        WSACleanup();
        return 1;
    }

    printf("Client connecté.\n");

    // Réception et affichage des messages du client
    while (1) {
        int bytesRead = recv(clientSocket, buffer, MAX_BUFFER_SIZE, 0);
        if (bytesRead > 0) {
            buffer[bytesRead] = '\0';
            printf("Message reçu : %s\n", buffer);
        }
    }

    // Fermeture du socket et nettoyage de Winsock
    closesocket(clientSocket);
    closesocket(serverSocket);
    WSACleanup();

    return 0;
}
