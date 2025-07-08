#include "tri_tas.hpp"

size_t Tas::get_index_parent(size_t index)
{
    return index/2;
}

size_t Tas::get_index_enfant_gauche(size_t index)
{
    return index*2;
}

size_t Tas::get_index_enfant_droit(size_t index)
{
    return index*2+1;
}

/// <summary>
/// Effectue une percolation ascendante à partir de l'index
/// juqu'à la racine
/// </summary>
/// <param name="index"></param>
void Tas::percolation_ascendante(size_t index)
{
    while (true)
    {
        size_t index_parent = get_index_parent(index);

        // on fait remonter la valeur data[index] si elle est plus petite que son parent
        if (data[index_parent] > data[index])
        {
            float temp = data[index_parent];
            data[index_parent] = data[index];
            data[index] = temp;
            index = index_parent;
        }
        else
        {
            // Fin de la percolation ascendante
            break;
        }
    }
}

void Tas::percolation_descendante(size_t index)
{
    while (index<this->get_size())
    {
        // on regarde quel est le plus petit enfant
        // si il est plus petit que sont data[index] on les échange
        size_t index_enfant_gauche = get_index_enfant_gauche(index);
        size_t index_enfant_droit = get_index_enfant_droit(index);

        // on regarde si l'enfant droit existe
        if (index_enfant_droit < this->get_size())
        {
            size_t index_min_enfant;
        
            // on recupère le plus petit enfant
            if (data[index_enfant_droit] < data[index_enfant_gauche])
                index_min_enfant = index_enfant_droit;
            else
                index_min_enfant = index_enfant_gauche;
            
            
            if (data[index_min_enfant] < data[index])
            {
                // si l'enfant est plus petit que son parent
                // on les échange
                float temp = data[index];
                data[index] = data[index_min_enfant];
                data[index_min_enfant] = temp;

                index = index_min_enfant;
            }
            else
            {
                // sinon la percolation descendante est finie
                break;
            }
                
            
        }
        else if (index_enfant_gauche < this->get_size())
        {
            if (data[index_enfant_gauche] < data[index])
            {
                // si l'enfant est plus petit que son parent
                // on les échange
                float temp = data[index];
                data[index] = data[index_enfant_gauche];
                data[index_enfant_gauche] = temp;

                index = index_enfant_gauche;
            }
            else
            {
                break;
            }
        }
        else
        {
            break;
        }
        
    }
}

size_t Tas::get_size()
{
    return data.size();
}

void Tas::append(float value)
{
    this->data.push_back(value);
	this->percolation_ascendante(this->get_size() - 1);
}

float Tas::pop()
{
	float min_value = data[0];
	data[0] = data[data.size() - 1];
	data.pop_back();
	this->percolation_descendante(0);

	return min_value;
}


void tri_tas(std::vector<float>& array)
{
    Tas tas;
    for (float value : array)
    {
        tas.append(value);
    }
    for(size_t i = 0; i < array.size(); i++)
    {
        array[i] = tas.pop();
	}
}
