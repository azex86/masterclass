#include <stdio.h>

enum Piece
{
    PION,
    CAVALIER,
    FOU,
    TOUR,
    ROI,
    DAME
};
int main()
{
    printf("Salut\n");
    enum Piece mapiece = PION;

    if(mapiece==PION)
        printf("Ma piece est un pion !\n");

    return 0;
}