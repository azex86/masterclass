/*
	Recherche du tri le plus rapide : 
	On a un tableau de N éléments à trier.


	On se propose de faire une énumération des méthodes efficace pour trier ce tableau.


	Tri par tas, tri par sélection, tri à bulles, tri rapide, tri fusion, etc.
	Voir les fichiers associés

*/


#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include "tri.hpp"


using namespace std;

void afficherTableau(const std::vector<float>& tableau) {
	if (tableau.size() > 50)
		return; // Si le tableau est trop grand, on ne l'affiche pas pour éviter une surcharge de sortie

	cout << "[";
	for (const auto& element : tableau) {
		std::cout << element << ",";
	}
	std::cout  <<"]" << std::endl;
}


double test_tri(std::vector<float>& tableau, void (*tri)(std::vector<float>&)) {
	// Démarrage du chronomètre
	auto start = std::chrono::high_resolution_clock::now();
	// Appel de la fonction de tri
	tri(tableau);
	// Arrêt du chronomètre
	auto end = std::chrono::high_resolution_clock::now();
	// Calcul du temps écoulé
	std::chrono::duration<double> elapsed = end - start;
	return elapsed.count();
}


int main(int argc,char** argv) {
	

	//on demande à l'utilisateur la taille du tableau à trier
	size_t N;
	std::cout << "Entrez la taille du tableau a trier >>";
	std::cin >> N;


	//on génère un tableau de N éléments aléatoires
	std::vector<float> tableau(N);
	std::random_device rd;  // Obtention d'un générateur de nombres aléatoires
	std::mt19937 gen(rd()); // Initialisation du générateur avec une graine aléatoire
	std::uniform_real_distribution<float> dis(0.0, 100.0); // Distribution uniforme entre 0 et 100

	for (size_t i = 0; i < N; ++i) {
		tableau[i] = dis(gen); // Remplissage du tableau avec des nombres aléatoires
	}


	//on affiche le tableau avant le tri
	std::cout << "Tableau avant le tri : ";
	afficherTableau(tableau);


	//on effectue les tri sur des copie du tableau pour ne pas altérer les données originales
	auto temp = tableau; // Copie du tableau original pour le tri par sélection

	auto duration_tri_selection = test_tri(temp, tri_selection);
	std::cout << "Tri par selection : temps ecoule : " << duration_tri_selection << " secondes" << std::endl;
	afficherTableau(temp);
	
	
	
	temp = tableau; // Copie du tableau original pour le tri à bulles
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


