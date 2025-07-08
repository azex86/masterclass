/*
	Recherche du tri le plus rapide : 
	On a un tableau de N �l�ments � trier.


	On se propose de faire une �num�ration des m�thodes efficace pour trier ce tableau.


	Tri par tas, tri par s�lection, tri � bulles, tri rapide, tri fusion, etc.
	Voir les fichiers associ�s

*/


#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include "tri.hpp"


using namespace std;

void afficherTableau(const std::vector<float>& tableau) {
	if (tableau.size() > 50)
		return; // Si le tableau est trop grand, on ne l'affiche pas pour �viter une surcharge de sortie

	cout << "[";
	for (const auto& element : tableau) {
		std::cout << element << ",";
	}
	std::cout  <<"]" << std::endl;
}


double test_tri(std::vector<float>& tableau, void (*tri)(std::vector<float>&)) {
	// D�marrage du chronom�tre
	auto start = std::chrono::high_resolution_clock::now();
	// Appel de la fonction de tri
	tri(tableau);
	// Arr�t du chronom�tre
	auto end = std::chrono::high_resolution_clock::now();
	// Calcul du temps �coul�
	std::chrono::duration<double> elapsed = end - start;
	return elapsed.count();
}


int main(int argc,char** argv) {
	

	//on demande � l'utilisateur la taille du tableau � trier
	size_t N;
	std::cout << "Entrez la taille du tableau a trier >>";
	std::cin >> N;


	//on g�n�re un tableau de N �l�ments al�atoires
	std::vector<float> tableau(N);
	std::random_device rd;  // Obtention d'un g�n�rateur de nombres al�atoires
	std::mt19937 gen(rd()); // Initialisation du g�n�rateur avec une graine al�atoire
	std::uniform_real_distribution<float> dis(0.0, 100.0); // Distribution uniforme entre 0 et 100

	for (size_t i = 0; i < N; ++i) {
		tableau[i] = dis(gen); // Remplissage du tableau avec des nombres al�atoires
	}


	//on affiche le tableau avant le tri
	std::cout << "Tableau avant le tri : ";
	afficherTableau(tableau);


	//on effectue les tri sur des copie du tableau pour ne pas alt�rer les donn�es originales
	auto temp = tableau; // Copie du tableau original pour le tri par s�lection

	auto duration_tri_selection = test_tri(temp, tri_selection);
	std::cout << "Tri par selection : temps ecoule : " << duration_tri_selection << " secondes" << std::endl;
	afficherTableau(temp);
	
	
	
	temp = tableau; // Copie du tableau original pour le tri � bulles
	auto duration_tri_bulles = test_tri(temp, tri_bulles);
	std::cout << "Tri a bulles : temps ecoule : " << duration_tri_bulles << " secondes" << std::endl;
	afficherTableau(temp);

	temp = tableau; // Copie du tableau original pour le tri par tas
	auto duration_tri_tas = test_tri(temp, tri_tas);
	std::cout << "Tri par tas : temps ecoule : " << duration_tri_tas << " secondes" << std::endl;
	afficherTableau(temp);

	
	temp = tableau; // Copie du tableau original pour le tri rapide
	auto duration_tri_rapide = test_tri(temp, tri_rapide);
	std::cout << "Tri rapide : temps ecoule : " << duration_tri_rapide << " secondes" << std::endl;
	afficherTableau(temp);
	

	temp = tableau; // Copie du tableau original pour le tri rapide
	auto duration_tri_fusion = test_tri(temp, tri_fusion);
	std::cout << "Tri fusion : temps ecoule : " << duration_tri_fusion << " secondes" << std::endl;
	afficherTableau(temp);
	
}


