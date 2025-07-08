#include "tri_selection.hpp"
#include <tuple>




/// <summary>
/// Retourne la valeur minimale d'un tableau de float et son index.
/// Complexit� pire cas : O(n) avec n la taille du tableau.
/// </summary>
/// <param name="array"></param>
/// <returns></returns>
std::tuple<float,size_t> min(const std::vector<float>& array) {
	float min_value = array[0];
	size_t min_index = 0;

	for(size_t i=0; i < array.size(); ++i) {
		if(array[i] < min_value) {
			min_value = array[i];
			min_index = i;
		}
	}

	return std::tuple<float,rsize_t>(min_value,min_index);
}




/// <summary>
/// Le principe du tri par selection est : la m�thode brut
/// On cherche l'�l�ment le plus petit du tableau,
/// on le place en premi�re position,
/// on cherche ensuite l'�l�ment le plus petit du tableau restant,
/// et on it�re ainsi de suite jusqu'� ce que le tableau soit tri�.
/// Complexit� pire cas : O(n^2) avec n la taille du tableau.
/// </summary>
/// <param name="array">tableau qui va �tre tri�</param>
void tri_selection(std::vector<float>& array) {

	for(size_t i=0; i < array.size() - 1; ++i) {
		// On cherche l'�l�ment le plus petit du tableau restant
		auto min_tuple = min(std::vector<float>(array.begin() + i, array.end()));
		float min_value = std::get<0>(min_tuple);
		size_t min_index = std::get<1>(min_tuple);

		// On �change l'�l�ment le plus petit avec l'�l�ment en position i
		std::swap(array[i], array[min_index + i]);
	}

}
