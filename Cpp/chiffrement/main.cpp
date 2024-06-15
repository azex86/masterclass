#include <iostream>

#include <fstream>

using namespace std;


//objectif 
/*
	selon la commande : 
				cr source dest			=> crypter le fichier source dans dest
				dcr source dest			=> décrypter le fichier source dans dest

	L'algorithme de cryptage est au choix, au plus simple pour le début = code César


	fonctionnalitées nécessaire : tableau, pointeur, fichier

*/

int main(int argc, char** argv)
{
	if (argc < 4)
		cerr << "Il manque des arguments à la commandes !\n";
	string commande = argv[1];
	string source = argv[2];
	string dest = argv[3];
	

	//lecture du fichier source


	//cryptage


	//écriture du fichier dest






	return 0;
}