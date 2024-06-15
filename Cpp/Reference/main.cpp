#include <iostream>


using namespace std;


void f(int x)
{
    x = x +2;
}
void h(int& x)
{
    x = x+2;
}

int main()
{

    int y = 0;
    cout <<y <<endl;
    f(y);
    cout <<y <<endl;
    h(y);
    cout <<y <<endl;

    //on constate que la fonction h modifie y contrairement à la fonction f
    //nous avons dit que les argmuments sont passés par copie par défaut comme dans la fonction f

    //il est possible de transmettre des arguments par référence avec l'ajout du '&'
    //type_retour name ( type_arg1 '&' arg1,....)

    //3 avantages de la référence : 
            //on peut modifier la variable
            //il n'y a pas de copie, si l'objet et volumineux on gagne de la vitesse
            //plus lisible qu'un pointeur
    //danger
        //toute modification à l'intérieur de la fonction modifie la variable

    return 0;
}