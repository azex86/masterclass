#pragma once
#include <iostream>
#include <string>
using namespace std;




class Joueur //dans l'ensemble de cet exemple on utilise des classes, mais des structures fonctionneraient égelement
{
public :
	virtual int play()
		// Méthode pure virtuelle, rend la classe abstraite
		// On déclare une classe Joueur qui n'a qu'une méthode : play()
		// On veut que tout type de joueur implémente une méthode jouer, on utilise le mot clé 'virtual'
	{
		cout << "Le joueur par défaut joue : " << endl;
		return 0;
	}
};


//on veut maintenant permettre à un joueur humain de jouer à travers le teminal
class JoueurHumain : public Joueur
{
	string username; // Nom d'utilisateur du joueur humain
public:

	JoueurHumain() // Constructeur qui initialise le nom d'utilisateur
	{
		cout << "Entrez votre nom d'utilisateur >>";
		cin >> username; // On demande à l'utilisateur de saisir son nom d'utilisateur
		cout << "Le joueur humain " << username << " est créé." << endl;
	}

	int play() override
		// On redéfinit la méthode play() pour le joueur humain
	{
		cout << "Le joueur humain" <<username <<"joue >>" << endl;
		int value;
		cin >> value;
		return value;
	}
};

//on veut maintenant utiliser un bot qui va jouer des valeurs aléatoires

class Bot : public Joueur
{
	public:
	Bot() // Constructeur du bot
	{
		cout << "Le bot est créé." << endl;
	}
	int play() override
		// On redéfinit la méthode play() pour le bot
	{
		int value = rand() % 100; // Le bot joue une valeur aléatoire entre 0 et 99
		cout << "Le bot joue : " << value << endl;
		return value;
	}
};


void test_heritage()
{
	JoueurHumain jh; // Création d'un joueur humain
	jh.play(); // Appel de la méthode play() du joueur humain
	Bot b; // Création d'un bot
	b.play(); // Appel de la méthode play() du bot

	// L'une des force de cette héritages est : 
	// de transférer tous les attributs et méthodes d'une classe à l'autre et éviter la redondance de code
	// mais également le polymorphisme : 
		// c'est-à-dire que l'on peut utiliser un pointeur de la classe de base pour appeler des méthodes de la classe dérivée
	// Exemple de polymorphisme avec un pointeur vers la classe de base Joueur


	Joueur* j = nullptr;
	int choix;
	cout << "Choisissez un type de joueur (1 pour Humain, 2 pour Bot) : ";
	cin >> choix;

	if (choix == 1) {
		j = new JoueurHumain(); // Création d'un joueur humain
	} else if (choix == 2) {
		j = new Bot(); // Création d'un bot
	} else {
		cout << "Choix invalide." << endl;
		return;
	}

	int play = j->play(); // Appel de la méthode play() via le pointeur de la classe de base
	//à partir d'ici, que ce soit un joueur humain ou un bot, on peut appeler la méthode play() de manière polymorphique
	// cela permet un gain considérable de clareté du code
	// c'est la force majeure  de l'héritage et du polymorphisme en C++
	// noter que l'on utilise le mot clé 'override' pour indiquer que l'on redéfinit une méthode de la classe de base, ce mot clé est optionnel et récent mais recommandé
	// le polymorphisme est le fondement même de Python et de bon nombre des langages de programmation orientée objet modernes
}