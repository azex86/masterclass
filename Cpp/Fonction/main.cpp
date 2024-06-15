#include <iostream>

using namespace std;


//déclaration d'une fonction
//type_de_retour nom (type1 arg1, type2 arg2,.......)
//{
//  du code
//  return valeur_de_retour;
//}
//ex:

int f ( int x)
{
    return x*x;
}

//Cas particulier, une fonction ne prend pas d'argument
int h(void)
{
    return 10;
}

//cas particulier, une fonction qui ne retourne pas de valeur : une procédure
void g(int x)
{
    cout <<"x = " <<x <<endl;
}

//on observe que le mot clé void est utilisé pour signifier l'absence de valeur
//noté que l'on ne peut PAS  déclarer une variable comme void car c'est un type incomplet


int main()
{

    //pour appeler une fonction : 
    // nom_de_la_fonction(arg1,arg2,....);
    g(5);

    g(h());

    g(f(5));


    return 0;
}