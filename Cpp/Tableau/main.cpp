#include <iostream>
using namespace std;


int main()
{

    //tableau statique
    int a[50]; //a est un tableau de 50 éléments de type int
    //pour accéder à un des élément de a 
    a[10] = 10;

    //le premier élément est toujour à l'index 0
    a[0] = 0;
    a[50-1] = 49;//dernier élément
    //attention lire en dehors du tableau peut conduire à de graves erreurs : crash du programme

    cout <<"a[25] = " <<a[25] <<endl;

    //un tableau déclaré de la sorte à un certains nombre de défauts :
        //il ne peut pas changer de taille il fait 50 pas plus pas moins
        //la taille d'un tableau statique doit être une constante, le compilateur doit savoir quelle taille il fait
        /*
        ceci n'est pas autorisé

        cout <<"nombre d'éléments ? ";
        int n = 0;
        cin >> n;
        int a[n]; 
        */
    //allouer un tableau trop grand consomme de la mémoire pour rien
    //allouer un tableau trop petit est encore plus génant


    //Le language C n'offre rien qui nativement règle le problème
    //Pour avoir un tableau de taille dynamique on doit demander à l'OS de nous fournir un espace libre en ram
    //Le C++ possède un mot clé natif pour cela
    //  new
    //ex : int* a = new int[10]; new demande à l'os un espace mémoire de 10*sizeof(int) avant de renvoier l'adresse de cet espace
    //lorsque l'on ne l'utilise plus, il faut indiquer à l'OS que l'espace mémoire est libre
    //delete[] a;

    int n = 0;
    cout <<"nombre d'éléments >>";
    cin >>n;
    int *L = new int[n];
    for(int i=0;i<n;i++)
        {
            L[i] = i;
        }
    for(int i=0;i<n;i++)
        {
            cout <<"L["<<i <<"] = "<<L[i] <<endl;
        }

        //On observe que les "[]" sont utilisable sur un pointeur
        //en réalité   a[2] <=> *(a + 2*sizeof(int))
        //donc *a et a[0] reviennent au même

    delete [] a;

}