#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argcn,char** argv)
{
    char* filename = argv[1];
    printf("Ouverture de : ");
    printf(filename);
    printf("\n");
    FILE *f = fopen(filename,"rb");
    if(f==NULL)
        printf("Error fopen\n");
    
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    fseek(f,0,SEEK_SET);
    
    printf("Taille du fichier a lire : %d Octets !\n",size);

    size_t sizeBlock = 500*1000*1000;
    int nBlock = size/sizeBlock +1;
    char **data = malloc(nBlock*sizeof(char*));
    printf("%d block de %d octets\n",nBlock,sizeBlock);
    for (int i=0;i<nBlock;i++)
        {
            data[i] = malloc(sizeBlock);
            printf("Lecture de %d octets !\n",fread(data[i],1,(i!=nBlock-1)?sizeBlock:size%sizeBlock,f));
        }
    

    fclose(f);
       

    for (int i=0;i<nBlock;i++)
        {
            free(data[i]);
        }
        fclose(f);
    free(data);
    return 0;
}