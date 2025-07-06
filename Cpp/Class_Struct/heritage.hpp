#pragma once
#include <iostream>
#include <string>
using namespace std;




class Joueur //dans l'ensemble de cet exemple on utilise des classes, mais des structures fonctionneraient �gelement
{
public :
	virtual int play()
		// M�thode pure virtuelle, rend la classe abstraite
		// On d�clare une classe Joueur qui n'a qu'une m�thode : play()
		// On veut que tout type de joueur impl�mente une m�thode jouer, on utilise le mot cl� 'virtual'
	{
		cout << "Le joueur par d�faut joue : " << endl;
		return 0;
	}
};


//on veut maintenant permettre � un joueur humain de jouer � travers le teminal
class JoueurHumain : public Joueur
{
	string username; // Nom d'utilisateur du joueur humain
public:

	JoueurHumain() // Constructeur qui initialise le nom d'utilisateur
	{
		cout << "Entrez votre nom d'utilisateur >>";
		cin >> username; // On demande � l'utilisateur de saisir son nom d'utilisateur
		cout << "Le joueur humain " << username << " est cr��." << endl;
	}

	int play() override
		// On red�finit la m�thode play() pour le joueur humain
	{
		cout << "Le joueur humain" <<username <<"joue >>" << endl;
		int value;
		cin >> value;
		return value;
	}
};

//on veut maintenant utiliser un bot qui va jouer des valeurs al�atoires

class Bot : public Joueur
{
	public:
	Bot() // Constructeur du bot
	{
		cout << "Le bot est cr��." << endl;
	}
	int play() override
		// On red�finit la m�thode play() pour le bot
	{
		int value = rand() % 100; // Le bot joue une valeur al�atoire entre 0 et 99
		cout << "Le bot joue : " << value << endl;
		return value;
	}
};


void test_heritage()
{
	JoueurHumain jh; // Cr�ation d'un joueur humain
	jh.play(); // Appel de la m�thode play() du joueur humain
	Bot b; // Cr�ation d'un bot
	b.play(); // Appel de la m�thode play() du bot

	// L'une des force de cette h�ritages est : 
	// de transf�rer tous les attributs et m�thodes d'une classe � l'autre et �viter la redondance de code
	// mais �galement le polymorphisme : 
		// c'est-�-dire que l'on peut utiliser un pointeur de la classe de base pour appeler des m�thodes de la classe d�riv�e
	// Exemple de polymorphisme avec un pointeur vers la classe de base Joueur


	Joueur* j = nullptr;
	int choix;
	cout << "Choisissez un type de joueur (1 pour Humain, 2 pour Bot) : ";
	cin >> choix;

	if (choix == 1) {
		j = new JoueurHumain(); // Cr�ation d'un joueur humain
	} else if (choix == 2) {
		j = new Bot(); // Cr�ation d'un bot
	} else {
		cout << "Choix invalide." << endl;
		return;
	}

	int play = j->play(); // Appel de la m�thode play() via le pointeur de la classe de base
	//� partir d'ici, que ce soit un joueur humain ou un bot, on peut appeler la m�thode play() de mani�re polymorphique
	// cela permet un gain consid�rable de claret� du code
	// c'est la force majeure  de l'h�ritage et du polymorphisme en C++
	// noter que l'on utilise le mot cl� 'override' pour indiquer que l'on red�finit une m�thode de la classe de base, ce mot cl� est optionnel et r�cent mais recommand�
	// le polymorphisme est le fondement m�me de Python et de bon nombre des langages de programmation orient�e objet modernes
}