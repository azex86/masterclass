
#include "struct_de_base.hpp"

//utilisation la plus basique d'une structure, cette utilisation est vraie en C


//d�claration d'un structure
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
	Une stucture est donc un nouveau type de variable personnalis�e, contenant d'autre variable , une sorte de groupe de variable que l'on regroupe dans une seul variable
	chaque sous variable (x et y) sont nomm�s des attributs. 

	on acc�de � un attribut avec struct_var.attribut l'op�rateur "." sert � acc�der � un attribut d'un objet struct  ou class.
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