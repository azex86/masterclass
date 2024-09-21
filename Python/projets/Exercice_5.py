#Objectif
#écrire un jeu de morpion entre deux joueurs qui joueront à travers le terminal

#code de départ

def finished(plateau:list)->bool:
    pass

def victoire(plateau:list)->bool:
    pass

def play(j:int,plateau:list)->None:
    pass


plateau = [[0,0,0],
           [0,0,0],
           [0,0,0]]

j1 = 1
j2 = 2

turn = 1

while finished(plateau):
    if turn == 1:
        play(j1,plateau)
        turn = 2
        if victoire(plateau):
            pass

    elif turn == 2:
        play(j2,plateau)
        turn = 1
        if victoire(plateau):
            pass
    
