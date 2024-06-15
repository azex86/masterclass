#include "struct_methode.hpp"

//En C++ uniquement
//les structures peuvent int�grer des m�thodes 



struct Vector
{
	//attributs
	float x;
	float y;

	//m�thodes
	float norme(void)
	{
		return sqrt(x * x + y * y);//on retourne la norme du vecteur  sqrt est la racine carr�
	}

	string tostring(void)
	{
		return "(" + to_string(x) + ";" + to_string(y) + ")";
	}

	//il existe des m�thodes sp�ciales 
	//Le constructeur est appel� quand un objet est construit;
	Vector()
	{
		cout << "Constructeur par d�faut de Vecor !\n";
		this->x = 0;//this est un pointeur sur l'objet actuel, il est facultatif dans la majorit� des cas
		this->y = 0;

	}

	//On peut �crire autant de constructeur diff�rent avec des arguments diff�rents afin de g�rer chaque cas de figure
	Vector(float _x, float _y)
	{
		cout << "Constructeur de Vector avec deux coordonn�es !\n";
		x = _x;
		y = _y;
	}

	Vector(Point a, Point b)
	{
		cout << "Constructeur de Vector avec deux points !\n";
		x = b.x - a.x;
		y = b.y - a.y;
	}

	//Le destucteur est appel� quand un objet est lib�r�
	~Vector()
	{
		cout << "Destucteur de vector !\n";
	}

	//Les op�rateurs suivent �galement  ce sh�ma

	
	Vector operator+(const Vector& v)
	{
		return Vector(this->x + v.x, this->y + v.y);
	}

	Vector operator*(const float k)
	{
		return Vector(x * k, y * k);
	}

	Vector operator-()
	{
		return Vector(-x, -y);
	}
};


void testVector()
{

		Vector a;
		a.x = 4;
		a.y = 3;
		float n = a.norme();//n =  sqrt(3*3+4*4) = sqrt(9+16)  = sqrt(25) = 5 

		Point A, B;
		A.x = 2; A.y = 2;
		B.x = -2; B.y = -2;

		Vector ab(A, B);

		cout << "A(" << A.x << ';' << A.y << ") B(" << B.x << ';' << B.y << ") => ab = " << ab.tostring() << endl;

		Vector u = ab * 2;
		cout << "u = " << u.tostring() << endl;

		Vector v = -u + Vector(1,1);

		cout << "v = " << v.tostring() << endl;




		//allouons maintenant un vecteur dynamiquement
		Vector* pw = new Vector;
		cout <<"w = " << pw->tostring() << endl;

		//on lib�re la m�moire
		delete pw;
}