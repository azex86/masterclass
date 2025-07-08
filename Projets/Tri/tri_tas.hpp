#pragma once
#include <vector>
using namespace std;


class Tas
{
	/// <summary>
	/// on va représenter le tas binaire par un tableau
	/// pour cela on va s'appuyer sur le fait qu'un tas binaire est un arbre binaire presque complet à gauche
	/// ainsi la racine sera à l'inde 0
	/// chaque enfant gauche d'un noeud sera à l'index : index du parent*2
	/// chaque enfant droit sera à l'index : index du parent*2 + 1
	/// </summary>
	vector<float> data;
    size_t get_index_parent(size_t index);
	size_t get_index_enfant_gauche(size_t index);
	size_t get_index_enfant_droit(size_t index);

	void percolation_ascendante(size_t index);
	void percolation_descendante(size_t index);

public:
	Tas() = default;
	size_t get_size();
	
	// insère un élément dans le tas binaire
	// complexité en O(log(n)) avec n le nombre d'élément dans le tas
	void append(float value);
	
	// extrait l'élément minimal du tas
	// complexité O(log(n)) avec n le nombre d'élément dans le tas
	float pop();
};

/// <summary>
/// Complexité pire cas : O(n*log(n))
/// </summary>
/// <param name="array"></param>
void tri_tas(std::vector<float>& array);

