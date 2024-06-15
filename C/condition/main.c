#include <stdio.h>


int main()
{

    /*
        Une condition est une une expression retournant une valeur booléenne 0(false) ou 1(true)
        le C considère toute valeur entière non nulle comme true
        le cast implicite renvoie vers de l'entier 

        ainsi l'expression     3.4 vaut true

        les opérateurs disponible dans les expression sont
        égal à :  a==b => true si a=b false sinon
        différent de   a!=b => l'inverse
        supérieur inférieur à : a>b a<b
        supérieur ou égale : a>=b a<=b
        inversion : !a => false si a vaut true sinon true  ex: !true => false   !false=>true
        et logique : a&&b => true si a et b sont true
        ou logique : a||b => false si a et b sont false

        exemple d'expression:
        int vrai_ou_faux = 2>1;           //1
        vrai_ou_faux = 2==2 && 1==1; //1
        vrai_ou_faux = 1>2 || 2>1;//1
        vrai_ou_faux = !(1>2 || 2>1);//0
        
    */

    int a = 0;

    if(a==0 && a!=1 || a>1)
        {
            printf("Salut\n");
        }
    else
        {
            printf("Bonjour\n");
        }

    switch (a)
    {
    case 0:
        printf("a = 0\n");
        break;
    case 1:
        printf("a = 1\n");
        break;
    default:
        printf("a != 0 et a!=1\n");
        break;
    }

    int b = (a==1)?1:2;

    /*
        trois type d'utilisation des conditions
        if(condition){actions;} else {actions;}
        les () sont obligatoire
        les if peuvent être imbriqués
            if(0==0)
                ;
            else if(1==1)
                ;
                else
                ;

        switch(variable)
        {
            case value_constante:
                actions;
                break;
            case value_constante:
                actions;
                break;
            default:
                code à éxecuter sinon
                break;
            
        }



        opérateur ternaire  
        (condition)?value_1:value_2
        renvoie value_1 si condition sinon retourne value_2
    */


}