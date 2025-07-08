#include "tri_bulles.hpp"



/// <summary>
/// Le pricipe du tri par bulles est de parcourir le tableau à plusieurs reprises, 
/// en comparant les éléments adjacents et en les échangeant s'ils sont dans le mauvais ordre.
/// à chaque passage, le plus grand élément "remonte" vers la fin du tableau comme une bulle dans l'eau, d'où le nom "tri à bulles".
/// Complexité pire cas : O(n^2)
/// </summary>
/// <param name="array"></param>
/// 
/// 
void tri_bulles(std::vector<float>& array)
{
	size_t n = array.size();
	for (; n > 1; --n)
	{
		for(size_t i=0; i < n-1; ++i)
		{
			if (array[i] > array[i + 1])
			{
				std::swap(array[i], array[i+1]);
			}
		}
	}

}
