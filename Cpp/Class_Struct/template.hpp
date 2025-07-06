#pragma once
#ifndef TEMPLATE_HEADER
#define TEMPLATE_HEADER
#include <iostream>

/*
	Le but des templates en C++ est de permettre la cr�ation de fonctions et de classes g�n�riques
	qui peuvent fonctionner avec n'importe quel type de donn�es.
	Cela permet d'�crire du code r�utilisable et flexible, r�duisant ainsi la duplication de code pour diff�rents types.

	Ici, je propose une impl�mentation simple d'une liste cha�n�e g�n�rique en C++.
	� l'aide d'une structure, une classe pourrrait faire l'affaire.
*/

template <typename E>
struct List {
	E* data;
	List* next;

	List() : data(nullptr), next(nullptr)  //initialise une liste vide
	{
	}

	void append(const E& value) {
		if (this->data != nullptr)
			this->next->append(value); // si l'�l�ment actuel est vide, on appelle la m�thode append sur l'�l�ment suivant
		else
		{
			this->data = new E(value); // alloue de la m�moire pour le nouvel �l�ment
			this->next = new List<E>(); // cr�e un nouvel �l�ment suivant vide
		}

	}

	E get(size_t index) const {
		if (index == 0) {
			return *data; // retourne la valeur de l'�l�ment actuel
		}
		else if (next != nullptr) {
			return next->get(index - 1); // appelle r�cursivement pour obtenir l'�l�ment suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // g�re les erreurs d'index
		}
	}

	void set(size_t index, E value) {
		if (index == 0) {
			*data = value; // met � jour la valeur de l'�l�ment actuel
		}
		else if (next != nullptr) {
			next->set(index - 1, value); // appelle r�cursivement pour mettre � jour l'�l�ment suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // g�re les erreurs d'index
		}
	}

	//On appr�ciera en C++ l'utilisation d'op�rateurs pour simplifier l'acc�s aux �l�ments de la liste 
	// en lecture et �criture grace au '&' dans le type de retour 'E&' qui permet de retourner une r�f�rence � l'�l�ment
	E& operator[](size_t index) {
		if (index == 0) {
			return *data; // retourne une r�f�rence � la valeur de l'�l�ment actuel
		}
		else if (next != nullptr) {
			return next->operator[](index - 1); // appelle r�cursivement pour obtenir l'�l�ment suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // g�re les erreurs d'index
		}
	}

	//on se donne une fonction pour afficher la liste sous condition que E soit un type affichable
	void print(bool start = true) const {
		if (start) {
			std::cout << "["; // affiche un message d'introduction
		}
		if (data != nullptr) {
			std::cout << *data; // affiche la valeur de l'�l�ment actuel
			

			//la compilation ne fonctionnera pas si E n'est pas affichable
			// c'est � dire si on ne peut pas utiliser std::cout << E
			// c'est � dire si std::ostream& operator<<(std::ostream&, const E&) n'est pas d�fini pour E


			if (next->data != nullptr) {
				std::cout << ","; // ajoute une virgule entre les �l�ments
				next->print(false); // appelle r�cursivement pour afficher les �l�ments suivants
			}
			else
			{
				std::cout << "]"; // affiche un message de fin si c'est le dernier �l�ment
			}
		}
		
	}

};

void test_list()
{
	List<int> myList; // cr�e une liste de type int
	myList.append(10); // ajoute un �l�ment � la liste
	myList.append(20); // ajoute un autre �l�ment � la liste

	myList.print(); // affiche la liste, devrait afficher [10,20]

	myList.set(1, 30); // modifie l'�l�ment � l'index 1
	myList.print(); // affiche la liste, devrait afficher [10,30]

	std::cout << "Element at index 0: " << myList.get(0) << std::endl; // affiche l'�l�ment � l'index 0, devrait afficher 10


	std::cout << "Element at index 1: " << myList[1] << std::endl; // affiche l'�l�ment � l'index 1, devrait afficher 30

	//on peut modifier les valeurs dans la liste
	myList[0] = 40; // modifie l'�l�ment � l'index 1


	//plus pr�cis�ment il se passe : 
	int& ref = myList[1]; // on r�cup�re une r�f�rence � l'�l�ment � l'index 1
	ref += 10; // on modifie la valeur de l'�l�ment � l'index 1
	myList.print(); // affiche la liste, devrait afficher [40,50]

	//l'utilisation des r�f�rences est � privil�gier en termes de claret�/performance mais elle produit des effets de bord
	// ce qui veut dire qu'il faut avoir conscience qu'en modifiant une valeur quelque part on impacte la liste
}


#endif // !TEMPLATE_HEADER
