#include "tri_rapide.hpp"

/// <summary>
/// Le tri rapide est un algorithme de diviser pour régner.
/// Il choisit un élément pivot et partitionne le tableau en deux sous-tableaux :
///		un contenant les éléments inférieurs au pivot et l'autre contenant les éléments supérieurs ou égaux.
///		Ensuite, il trie récursivement les sous-tableaux.
/// 
///	Complexité moyenne de O(n*log(n)).
/// Complexité pire cas O(n^2)	
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
