#include <stdio.h> //Inclure les fonction pour print IO = Input/Output std == standard
//#include <stdlib.h>//Inclure les fonctions pour malloc et free
#include <string.h>


int main()
{
    char filename[] = "test.txt";
    char mode[] = "w"; //r w a rb wb ab pour  read write or append par défaut en texte b pour binaire
    //Ouvrir un fichier
    FILE *f = fopen(filename,mode);

    printf("Position = %d\n",ftell(f));//Notre position dans le fichier

    fprintf(f,"Salut beauté !\n");//On écrit quelque chose
                                                                                                    //printf("Position = %d\n",ftell(f));

                                                                                                    //fseek(f,-11,SEEK_CUR);//On se déplace dans le fichier de "-11" depuis la SEEK_CUR = position actuel donc la fin
                                                                                                    //printf("Position = %d\n",ftell(f));
                                                                                                    //fprintf(f,"personne de sexe opposé !");
                                                                                                    //printf("Position = %d\n",ftell(f));

    
    fclose(f);//On ferme le fichier



  //  ecrire
        f = fopen(filename,mode);
        fprintf(f,"Adrien\n13\n14\nLysandre\n13\n13\n");
        fclose(f);

    mode[0] = 'r';
    f = fopen(filename,mode);
    if(f!=NULL)
    printf("Ouverture en lecture !\n");
    for(int i = 0;i<2;i++)
    {
        char name[100];
        int firstNote, lastNote;
        fscanf(f,"%s%d%d",name,&firstNote,&lastNote);
        printf("L'eleve %s a eu %d puis %d\n",name,firstNote,lastNote);
    }
    fclose(f);





    return 0;
}