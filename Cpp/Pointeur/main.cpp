#include <iostream>


using namespace std;


void test();

//Les pointeurs : 
    //Ce sont des variables classiques, des entiers de 32 ou 64 bits selon le processeur
    //il se déclare comme ceci :
    //                  type * name;
    //ex : int * px;            on met généralement un p en première lettre des pointeur pour signifier qu'ils sont des pointeurs

//Le but d'un pointeur est de représenter un entier qui l'adresse mémoire de quelque chose

int main()
{
    //Utlisation d'un pointeur classiquement 
    int x = 0;
    int* px; //on veut maintenant que px pointe sur x
    //on utilise l'opérateur de référencement '&' à ne pas confondre avec le contexte de référence pour les argmuments d'une fonction
    px = &x;
    //px pointe désormais sur l'adresse mémoire de x
    //pour lire x à travers px on utilise l'opérateur de déréférencement '*'
    cout <<"adresse : " <<px <<" valeur = " <<*px <<endl;
    x = 5;
    cout <<"nouvelle valeur = " <<*px;

    //résumé
        // &variable => adresse mémoire de la variable
        // *pointeur => valeur présent à l'adresse mémoire du pointeur

    //à quoi cela sert ?
    test();//faisons un jump vers test à la fin d fichier

    return 0;
}

void f(int x)
{
    x = x+2;
}
void h(int* x)
{

    *x = *x +2;
}

void test(void)
{

    int x = 0;

    int* px = &x;

    cout <<" x = " <<x <<endl;
    f(x);
    cout <<" x = " <<x <<endl;
    h(px);
    cout <<" x = " <<x <<endl;

    //on constate qu'en transmettant une adresse mémoire en argument, celle-ci peut bien être copier, elle pointeras toujours vers la même addresse
    //On peut ainsi modifier une variable extérieur à une fonction via un argument


}