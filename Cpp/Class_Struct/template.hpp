#pragma once
#ifndef TEMPLATE_HEADER
#define TEMPLATE_HEADER
#include <iostream>

/*
	Le but des templates en C++ est de permettre la création de fonctions et de classes génériques
	qui peuvent fonctionner avec n'importe quel type de données.
	Cela permet d'écrire du code réutilisable et flexible, réduisant ainsi la duplication de code pour différents types.

	Ici, je propose une implémentation simple d'une liste chaînée générique en C++.
	à l'aide d'une structure, une classe pourrrait faire l'affaire.
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
			this->next->append(value); // si l'élément actuel est vide, on appelle la méthode append sur l'élément suivant
		else
		{
			this->data = new E(value); // alloue de la mémoire pour le nouvel élément
			this->next = new List<E>(); // crée un nouvel élément suivant vide
		}

	}

	E get(size_t index) const {
		if (index == 0) {
			return *data; // retourne la valeur de l'élément actuel
		}
		else if (next != nullptr) {
			return next->get(index - 1); // appelle récursivement pour obtenir l'élément suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // gère les erreurs d'index
		}
	}

	void set(size_t index, E value) {
		if (index == 0) {
			*data = value; // met à jour la valeur de l'élément actuel
		}
		else if (next != nullptr) {
			next->set(index - 1, value); // appelle récursivement pour mettre à jour l'élément suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // gère les erreurs d'index
		}
	}

	//On appréciera en C++ l'utilisation d'opérateurs pour simplifier l'accès aux éléments de la liste 
	// en lecture et écriture grace au '&' dans le type de retour 'E&' qui permet de retourner une référence à l'élément
	E& operator[](size_t index) {
		if (index == 0) {
			return *data; // retourne une référence à la valeur de l'élément actuel
		}
		else if (next != nullptr) {
			return next->operator[](index - 1); // appelle récursivement pour obtenir l'élément suivant
		}
		else {
			throw std::out_of_range("Index out of range"); // gère les erreurs d'index
		}
	}

	//on se donne une fonction pour afficher la liste sous condition que E soit un type affichable
	void print(bool start = true) const {
		if (start) {
			std::cout << "["; // affiche un message d'introduction
		}
		if (data != nullptr) {
			std::cout << *data; // affiche la valeur de l'élément actuel
			

			//la compilation ne fonctionnera pas si E n'est pas affichable
			// c'est à dire si on ne peut pas utiliser std::cout << E
			// c'est à dire si std::ostream& operator<<(std::ostream&, const E&) n'est pas défini pour E


			if (next->data != nullptr) {
				std::cout << ","; // ajoute une virgule entre les éléments
				next->print(false); // appelle récursivement pour afficher les éléments suivants
			}
			else
			{
				std::cout << "]"; // affiche un message de fin si c'est le dernier élément
			}
		}
		
	}

};

void test_list()
{
	List<int> myList; // crée une liste de type int
	myList.append(10); // ajoute un élément à la liste
	myList.append(20); // ajoute un autre élément à la liste

	myList.print(); // affiche la liste, devrait afficher [10,20]

	myList.set(1, 30); // modifie l'élément à l'index 1
	myList.print(); // affiche la liste, devrait afficher [10,30]

	std::cout << "Element at index 0: " << myList.get(0) << std::endl; // affiche l'élément à l'index 0, devrait afficher 10


	std::cout << "Element at index 1: " << myList[1] << std::endl; // affiche l'élément à l'index 1, devrait afficher 30

	//on peut modifier les valeurs dans la liste
	myList[0] = 40; // modifie l'élément à l'index 1


	//plus précisément il se passe : 
	int& ref = myList[1]; // on récupère une référence à l'élément à l'index 1
	ref += 10; // on modifie la valeur de l'élément à l'index 1
	myList.print(); // affiche la liste, devrait afficher [40,50]

	//l'utilisation des références est à privilégier en termes de clareté/performance mais elle produit des effets de bord
	// ce qui veut dire qu'il faut avoir conscience qu'en modifiant une valeur quelque part on impacte la liste
}


#endif // !TEMPLATE_HEADER
