#include "class.hpp"

//Une class est tr�s proche d'une structure, tout ce qui est vrai pour une structure l'est aussi pour une classe
// la différence se résume à l'accessibilité par défaut des attributs/méthode
// pour une classe les attributs sont 'private' par défaut
// cela veut dire que seul les méthodes de la classe peuvent y accéder
//
class Rectangle
{
private:
	float x;
	float y;
	float l;
	float L;
public:	
	Rectangle(float _x, float _y, float _l, float _L)
	{
		x = _x;
		y = _y;
		l = _l;
		L = _L;
	}

	float get_x()const {
		std::cout <<"lecture de la valeur x : " <<this->x <<std::endl;
		return this->x;//ici on peut acceder à x
	};

	void set_x(float new_x)
	{
		std::cout <<"Il est possible de reagir en consequence quand un des attributs est modifie" <<std::endl
		<< "Par exemple en recalculant la norme ou autre\n";
		this->x = new_x;//ici on peut acceder à x
	}

};


/*
	L
*/


void testClass()
{
	Rectangle a = Rectangle(1,1,2,2);

	a.x = 3;//erreur
	a.set_x(3);//correct

}