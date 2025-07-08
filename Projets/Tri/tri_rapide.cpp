#include "tri_rapide.hpp"

/// <summary>
/// Le tri rapide est un algorithme de diviser pour r�gner.
/// Il choisit un �l�ment pivot et partitionne le tableau en deux sous-tableaux :
///		un contenant les �l�ments inf�rieurs au pivot et l'autre contenant les �l�ments sup�rieurs ou �gaux.
///		Ensuite, il trie r�cursivement les sous-tableaux.
/// 
///	Complexit� moyenne de O(n*log(n)).
/// Complexit� pire cas O(n^2)	
/// </summary>
/// <param name="array"></param>
void tri_rapide(std::vector<float>& array)
{
	if (array.size() < 2) return; // No need to sort if the array has less than 2 elements
	float pivot = array[array.size() / 2]; // Choose the middle element as the pivot
	std::vector<float> left, right;
	for (size_t i = 0; i < array.size(); ++i) {
		if (i == array.size() / 2) continue; // Skip the pivot itself
		if (array[i] < pivot) {
			left.push_back(array[i]);
		} else {
			right.push_back(array[i]);
		}
	}
	tri_rapide(left); // Recursively sort the left part
	tri_rapide(right); // Recursively sort the right part
	// Combine the sorted parts and the pivot
	array.clear();
	array.insert(array.end(), left.begin(), left.end());
	array.push_back(pivot);
	array.insert(array.end(), right.begin(), right.end());
}
