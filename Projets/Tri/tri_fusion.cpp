#include "tri_fusion.hpp"









/// <summary>
/// Le tri fusion est un algorithme de tri bas� sur le principe du diviser pour r�gner.
/// Il s'appuie sur l'id�e que avec deux tableaux tri�s, il est facile de les combiner en un seul tableau tri�.
/// Ainsi, � partir du tableau non tri� on va le diviser en deux sous - tableaux,
/// puis trier r�cursivement ces deux sous - tableaux, et enfin les combiner pour obtenir le tableau tri� final.
/// 
/// L'algorithme diviser pour r�gner est naturellement d�crit de fa�on r�cursive.
/// 
/// Cas de base :
/// Si le tableau est vide, il est d�j� tri�
/// Si le tableau n'a qu'un �l�ment, il est d�j� tri�.
/// Cas r�cursif :
/// Diviser: s�parer le tableau en deux parties � peu pr�s �gales, de tailles n / 2 + (n % 2), n / 2 respectivement.
/// R�gner : Trier r�cursivement les deux parties avec l'algorithme du tri fusion.
/// Combiner : Interclasser les deux tableaux tri�s en un seul tableau tri�[2].
/// 
/// Compleit� pire cas : O(n log n) avec n le nombre d'�l�ments � trier.
/// </summary>
/// <param name="array"></param>
/// 
void tri_fusion(std::vector<float>& array)
{
	size_t n1 = array.size()/2 + array.size()%2;
	size_t n2 = array.size() / 2;

	if (n1 == 0 || n2 == 0) // Cas de base : tableau vide ou un seul �l�ment
		return;


	std::vector<float> left(array.begin(), array.begin() + n1); // Premier sous-tableau
	std::vector<float> right(array.begin() + n1, array.end()); // Deuxi�me sous-tableau

	tri_fusion(left); // Tri r�cursif du premier sous-tableau
	tri_fusion(right); // Tri r�cursif du deuxi�me sous-tableau

	// Combinaison des deux sous-tableaux tri�s
	size_t i = 0, j = 0, k = 0;
	while (i < n1 && j < n2) // Tant qu'il y a des �l�ments dans les deux sous-tableaux
	{
		if (left[i] <= right[j]) // Si l'�l�ment du premier sous-tableau est plus petit ou �gal
		{
			array[k++] = left[i++]; // Ajouter � l'array et avancer dans le premier sous-tableau
		}
		else // Si l'�l�ment du deuxi�me sous-tableau est plus petit
		{
			array[k++] = right[j++]; // Ajouter � l'array et avancer dans le deuxi�me sous-tableau
		}
	}
	while (i < n1) // Ajouter les �l�ments restants du premier sous-tableau
	{
		array[k++] = left[i++];
	}
	while (j < n2) // Ajouter les �l�ments restants du deuxi�me sous-tableau
	{
		array[k++] = right[j++];
	}

	// Le tableau 'array' est maintenant tri�
	// Note : Les sous-tableaux 'left' et 'right' sont temporaires et seront d�truits � la fin de la fonction

}
