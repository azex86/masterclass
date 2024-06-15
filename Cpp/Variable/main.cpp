#include <iostream>

using namespace std;

int global = 2023;





int main()
{
    //declaration d'une variable :
    //type nom ( = valeur  )  ;
    //          facultatif
    int x = 0;
    int y;

    //manipulation de variable de type primitif
    x = 5;
    y = 4;
    y++;
    x = x*y;
    //x = 5 * (4 + 1) = 25
    //les variables sont avant tout des espaces mémoires et on manipule ces espaces mémoires
    
    x = 0;
    
    //on constate le même résultat
    //les variables n'existent qu'entre leurs accolades
    /*
        {
            //b est initialisé
            ...
            {
            //a est initialisé
                ...
                int a;
                ...
            //a n'existe plus
            }
            int b;
            ...
            //b est libéré
        }    
    */
   //Ceci est valable pour les boucles, les conditions, les fonctions , les classes , ....


    //observons la variable global au début du code
    //celle ci n'est pas dans des accolades
    //elle est accessible depuis tout endroit du code qui l'import
    //en d'autre terme dans tout le fichier main.cpp
    cout <<global <<endl;
    x = global;
    cout <<"x = " <<x <<endl;


    /*
        Les types de variables primitifs sont : 

                                      1   |    2    |   4   |     8   |     taille de la variable en octet
                                    -----------------------------------
                                    char  |  short  | int   |  long         type de variable entière ex : 1 ; 10 ; -5 ; 0xAFF ; 0b0110110 ;.....
                                    ----------------------------------- 
                                                    | float |  double |     type de variable à virgule ex: 2.5 ; -10.456 ; .....
                                    -----------------------------------
                                    bool  |
        Plus un variable est "grosse" plus les valeurs qu'elle peut stocker sont grandes et inversement
        ainsi une variable de type "char" de 1 octets soit 8 bits peut stocker 2^8 = 256 valeurs différentes donc de -128 à +127
        
        on peut indiquer que la variable est forcément positive (on enlève le signe) avec le mot clé "unsigned" donc : unsigned char x = 0; x peut ici prendre des valeurs allant de 0 à 255
        */


    return 0;
}