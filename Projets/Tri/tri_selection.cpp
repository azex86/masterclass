#include "tri_selection.hpp"
#include <tuple>




/// <summary>
/// Retourne la valeur minimale d'un tableau de float et son index.
/// Complexité pire cas : O(n) avec n la taille du tableau.
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
/// Le principe du tri par selection est : la méthode brut
/// On cherche l'élément le plus petit du tableau,
/// on le place en première position,
/// on cherche ensuite l'élément le plus petit du tableau restant,
/// et on itère ainsi de suite jusqu'à ce que le tableau soit trié.
/// Complexité pire cas : O(n^2) avec n la taille du tableau.
/// </summary>
/// <param name="array">tableau qui va être trié</param>
void tri_selection(std::vector<float>& array) {

	for(size_t i=0; i < array.size() - 1; ++i) {
		// On cherche l'élément le plus petit du tableau restant
		auto min_tuple = min(std::vector<float>(array.begin() + i, array.end()));
		float min_value = std::get<0>(min_tuple);
		size_t min_index = std::get<1>(min_tuple);

		// On échange l'élément le plus petit avec l'élément en position i
		std::swap(array[i], array[min_index + i]);
	}

}
