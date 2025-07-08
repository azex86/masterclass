#pragma once
#include <vector>
using namespace std;


class Tas
{
	/// <summary>
	/// on va repr�senter le tas binaire par un tableau
	/// pour cela on va s'appuyer sur le fait qu'un tas binaire est un arbre binaire presque complet � gauche
	/// ainsi la racine sera � l'inde 0
	/// chaque enfant gauche d'un noeud sera � l'index : index du parent*2
	/// chaque enfant droit sera � l'index : index du parent*2 + 1
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
	
	// ins�re un �l�ment dans le tas binaire
	// complexit� en O(log(n)) avec n le nombre d'�l�ment dans le tas
	void append(float value);
	
	// extrait l'�l�ment minimal du tas
	// complexit� O(log(n)) avec n le nombre d'�l�ment dans le tas
	float pop();
};

/// <summary>
/// Complexit� pire cas : O(n*log(n))
/// </summary>
/// <param name="array"></param>
void tri_tas(std::vector<float>& array);

