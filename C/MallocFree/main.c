#include <stdlib.h>
#include <stdio.h>
int main()
{
    size_t size = 500000000;
    char* a = malloc(size);
    if(a==NULL)printf("Erreur\n");
    char* b = malloc(size);
    if(b==NULL)printf("Erreur\n");

    free(a);
    free(b);
    return 0;
}