#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
    FILE *fptr = fopen(filename,mode);
    fprintf(fptr,text,....var);/fscanf(fptr,&var)
    fwrite();fread();
    fclose(fptr);
*/


int main()
{

    const unsigned long size = 500*1000*1000;
    const unsigned long size_per_unit = 1;
    unsigned long trace = 0;
    FILE *fptr;
    const char filename[] = "temp.log";
    char* dataRead = NULL;
    char* dataWrite = NULL;

    printf("Generation des buffers...\n");

    dataWrite = malloc(size*size_per_unit); 
    if(dataWrite==NULL)
        printf("Erreur d'allocation de la memoire !\n");
    for (int i=0;i<size;i++)
        dataWrite[i] = i;
    

    dataRead = malloc(size*size_per_unit); 
    if(dataRead==NULL)
        printf("Erreur d'allocation de la memoire !\n");



    printf("Lancement de la boucle d'ecriture lecture !\n");
    for(;;)
    {
        //Phase d'ecriture
        fptr = (fopen(filename, "wb"));
        if(fptr == NULL)
        {
        printf("Error!");
        exit(1);
        }
         printf("Ecriture de ");
        trace = fwrite(dataWrite,size_per_unit,size,fptr);
        printf("%d octets\n",trace);

        fclose(fptr);

       

        //Phase de lecture
        fptr = fopen(filename,"rb");
        if(fptr == NULL)
        {
            printf("Error!");
            exit(1);
        }
        printf("Lecture de ");
        trace = fread(dataRead,size_per_unit,size,fptr);
        printf("%d octets\n",trace);
        fclose(fptr);
        

        //Phase de Verification
        printf("Recherche d'erreur !\n");
        //Comparaison  de dataRead avec dataWrite
        //Methode 1
        int nError = 0;
        for (int i=0;i<size*size_per_unit;i++)
            if(dataRead[i] != dataWrite[i])
                nError++;
        printf("%d Erreurs !\n",nError);

        //Methode 2
       // nError=memcmp(dataRead,dataWrite,size*size_per_unit);
        //if (nError!=0)
        //    printf("Erreur !\n");
    }
    

   




   return 0;
}
