#include <stdio.h>
int i;

int main()
{


    int n = 10;
    while (n>1)
    {
        n = n-1;
        printf("n = %d\n",n);
    }
    /*
        Boucle while
        répete les instructions tant que la  condition est vérifié
        typiquement une boucle 
        while(1==1)
            ;
        est infini

    */

  
    for(int i=0;i<10;i++)
        printf("i = %d\n",i);

    /*
        boucle for
        for(declaration/initialisation de variable ; condition ; iteration)
            actions;
        au début de la boucle => initialisation 
        à chaque début de boucle la condition est vérifié si elle ne l'est pas la boucle se termine
        à la fin de chaque boucle => iteration 
    */


    n = 0;

BALISE:
    printf("n = %d\n",n);
    n = n+1;
    if(n<10)
        goto BALISE;

    /*
        ce n'est pas une boucle à proprement parler
        mais cela permet d'en faire une, c'est ce qui se rapproche le plus de l'assembleur et donc du processeur
        peut-être assez pratique pour gérer les erreurs
    */

    return 0;
}