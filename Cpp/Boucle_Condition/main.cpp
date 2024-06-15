#include <iostream>

using namespace std;


int main()
{
   //Les conditions : 
   // 
    //Le classique:
    // 
    // if(condition)
    //{
    //  action;
    //}

    if (10 > 5)
    {
        cout << "10>5 !\n";
        cout << "on est content !\n";
    }

    //il est possible de se passer d'accolade pour une unique instruction
    if (5 > 10)
        cout << "????";

    //pour executer du code si la condition n'es pas v�rifi�e
    //if(action)
    //  action_si_oui;
    //else
    //  action_si_non;

    if (true)
        cout << true;
    else 
        cout << false;
    //c'est l'�quivalent de 
    if (true) cout << true; else cout << false;
    //en C le retour � la ligne n'a de signification que pour les "" et pour les lignes commencant par #
    //on peut aussi �crire : 
    if (true)
    {
        cout << true;
    }
    else
    {
        cout << false;
    }

    //avec if else, la conditon doit-�tre bool�enne, un entier est �gal � true sauf 0
    if (10)
        cout << "oui";
    if (0)
        cout << "non";

    //une autre forme de condition : switch
    /*
        switch(var)
        {
        case value1:
            code;
            break;
        case value2;
            code;
            break;
        case value....
        ...


        default:
            code;
            break;
    */
    int x = 10;
    switch (x)
    {
    case 5:
        cout << "x = 5\n";
        break;
    case 8:
        cout << "x = 8\n";
        break;
    default:
        cout << "ce cas n'est pas g�r� !\n";
        break;
    }
    //l'instruction break est IMPORTANTE sinon le code continue et passe � la case suivante(�a peut �tre utile des fois)
    //les valeur test� dans les case DOIVENT-�tre des CONSTANTES et var doit-�tre une "lvalue" = un type primitif :
    /*
    *   switch(x)
    * {
    *   case y:
    *       x = y;
    *       break;
    * }
    * ceci ne marche pas
    * 
    * cette deuxi�me contrainte fait que l'on prefereras l'usage de if else
    */



    //Les boucles

    //une boucle d�pent obligatoirement d'une condition
    //la premi�re boucle qui vient de l'assembleur : 

    x = 0;

 debutBoucle:
    x++;
    cout << x << endl;
    if (x < 10)
        goto debutBoucle;

    //on n'utiliseras JAMAIS cette solution mais il est bon de savoir que cette "chose" est l'unque repr�sentation d'une boucle pour un ordinateur


    //la boucle while
    /*
        while(condition)
        {
            action tant que la condition est v�rifi�e;
        }
    */
    x = 0;
    while (x<10)
    {
        x++;
        cout << x << endl;
    }

    //pour tester la condition � la fin de la boucle            => si on veut que la boucle soit parcourue au moins une fois
    x = 0;
    do
    {
        x++;
        cout << x << endl;
    }
    while(x<10);
    //Attention il y a un ';'


    //La boucle it�ratitve par excellence
    /*
        for(declaration ; condition ; incrementation)
        {
            action tant que contion est v�rifi�e;
        }
    */
    x = 0;
    for (; x < 10; )
    {
        cout << x << endl;
        x++;
    }
    //cela ressemble � une boucle while mais affinons un peu
    x = 0;
    for (; x < 10; x++ )
    {
        cout << x << endl;
    }
    //le x++ � �t� d�plac� dans l'incr�mentations
    //l'utilisation classique

    for (int i = 0; i < 10; i++)
        cout <<"i = " << i << endl;


    /*
    Conclusion
            if else
            switch
            while
            for
    */

    return 0;
}