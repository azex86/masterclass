#include "tri_fusion.hpp"









/// <summary>
/// Le tri fusion est un algorithme de tri basé sur le principe du diviser pour régner.
/// Il s'appuie sur l'idée que avec deux tableaux triés, il est facile de les combiner en un seul tableau trié.
/// Ainsi, à partir du tableau non trié on va le diviser en deux sous - tableaux,
/// puis trier récursivement ces deux sous - tableaux, et enfin les combiner pour obtenir le tableau trié final.
/// 
/// L'algorithme diviser pour régner est naturellement décrit de façon récursive.
/// 
/// Cas de base :
/// Si le tableau est vide, il est déjà trié
/// Si le tableau n'a qu'un élément, il est déjà trié.
/// Cas récursif :
/// Diviser: séparer le tableau en deux parties à peu près égales, de tailles n / 2 + (n % 2), n / 2 respectivement.
/// Régner : Trier récursivement les deux parties avec l'algorithme du tri fusion.
/// Combiner : Interclasser les deux tableaux triés en un seul tableau trié[2].
/// 
/// Compleité pire cas : O(n log n) avec n le nombre d'éléments à trier.
/// </summary>
/// <param name="array"></param>
/// 
void tri_fusion(std::vector<float>& array)
{
	size_t n1 = array.size()/2 + array.size()%2;
	size_t n2 = array.size() / 2;

	if (n1 == 0 || n2 == 0) // Cas de base : tableau vide ou un seul élément
		return;


	std::vector<float> left(array.begin(), array.begin() + n1); // Premier sous-tableau
	std::vector<float> right(array.begin() + n1, array.end()); // Deuxième sous-tableau

	tri_fusion(left); // Tri récursif du premier sous-tableau
	tri_fusion(right); // Tri récursif du deuxième sous-tableau

	// Combinaison des deux sous-tableaux triés
	size_t i = 0, j = 0, k = 0;
	while (i < n1 && j < n2) // Tant qu'il y a des éléments dans les deux sous-tableaux
	{
		if (left[i] <= right[j]) // Si l'élément du premier sous-tableau est plus petit ou égal
		{
			array[k++] = left[i++]; // Ajouter à l'array et avancer dans le premier sous-tableau
		}
		else // Si l'élément du deuxième sous-tableau est plus petit
		{
			array[k++] = right[j++]; // Ajouter à l'array et avancer dans le deuxième sous-tableau
		}
	}
	while (i < n1) // Ajouter les éléments restants du premier sous-tableau
	{
		array[k++] = left[i++];
	}
	while (j < n2) // Ajouter les éléments restants du deuxième sous-tableau
	{
		array[k++] = right[j++];
	}

	// Le tableau 'array' est maintenant trié
	// Note : Les sous-tableaux 'left' et 'right' sont temporaires et seront détruits à la fin de la fonction

}
