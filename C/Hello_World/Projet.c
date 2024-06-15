// Projet.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//
/*
    compilation en ligne de commande:
        Linux: 
            sudo apt-get install libsdl2-dev 
            gcc -lSDL2 main.c 
        Windows:
            gcc
                gcc main.c -o prog -I include -L lib -lmingw32 -lSDL2main -lSDL2

            MSVC(microsoft) : 
                ajouter au path Common7\Tools et VC\Tools\MSVC\14.36.32532\bin\Hostx64\x64
                taper VsDevCmd
                taper cl main.c

*/

#include <stdio.h>



int main()
{
         
    printf("Hello world !");
    

    return 0;
}

