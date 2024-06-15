
#include "struct_de_base.hpp"

//utilisation la plus basique d'une structure, cette utilisation est vraie en C


//déclaration d'un structure
//struct name
//{
//
//	type_attribut name_attribut  = value ;
// 
//}
#ifndef POINT
				struct Point
				{
					float x;
					float y;
				};
#endif // POINT



/*
	Une stucture est donc un nouveau type de variable personnalisée, contenant d'autre variable , une sorte de groupe de variable que l'on regroupe dans une seul variable
	chaque sous variable (x et y) sont nommés des attributs. 

	on accède à un attribut avec struct_var.attribut l'opérateur "." sert à accéder à un attribut d'un objet struct  ou class.
*/



void testPoint()
{
	Point a ;
	a.x = 5;
	a.y = -5;


	Point* pa = &a;
	pa->x;
	(*pa).x;


}