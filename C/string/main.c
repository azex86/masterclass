

/*
        Les string en C n'existent PAS !
        ce qui s'en rapproche et qui est la base d'un string c'est une chaine de caractère
        c'est à dire un tableau de char ainsi 

        char monstring[] = "Hello World";
                            12345678901 => 11 +1 = 12 char
        monstring est un tableau de 12 char et oui une chaîne de caractère se termine conventionellement par le caractère \0 dit de fin

        donc ceci "0" = ['0','\0'] fait 2 octets alors que ceci '0' fait 1 seul octet

        comme monstring est un tableau il ne peut pas être réaffecté
        monstring[] = "Hello";
        monstring[] = "salut"; -> Erreur pas possible

        de même un tableau à une taille fixe
        monstring[] = "Hello"; le compilateur comprend monstring[12] = "Hello";
        ainsi monstring fait 12 lettres et ne pourra pas en contenir plus

        monstring[12] ="Salut la compagnie !"; -> erreur

        pour modifier le contenu d'un tableau

                1:
                        char monstring[] = "Hello";
                        monstring[0] = 's';
                        monstring[1] = 'a';
                        monstring[2] = 'l';
                        monstring[3] = 'u';
                        monstring[4] = 't';
                        monstring[5] = '\0'; ça ne change pas
                2:
                       méthode de la bibliothèque <string.h> strcpy(target,source)
                        char monstring[] = "Hello";
                        strcpy(monstring,"salut");


        L'utilisation de chaîne de caractères nous amène à utiliser la sortie(print) et n'entrée standard(input)
        pour ce faire <stdio.h> nous donne quelque fonctions dont 4 que nous verrons
        printf()
        scanf()



        %d int
        %c char
        %f float
        %s string
        %ld long int
        %i unsigned int
        %lf double = long float
        %n nothing
        %[character]
        %[^character]


        
*/


#include <string.h>
#include <stdio.h>

int main()
{
        char monstring[] = "Hello";
        printf("%s\n",monstring);

        strcpy(monstring,"salut");
        printf("%s\n",monstring);

        
        return 0;
}