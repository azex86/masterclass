#ici commence le travail
#vous êtes libre de consulter les cours au sections lagage modules_natifs modules_utiles
#Cepandant pour vous éviter des migraine inutile sacher que la majorité de ce cours sont inutiles
#les cours à consulter seront indiquer lorsque nécessaire à un exercice
#on entend par consulter une lecture rapide avec une execution du programme
#le but est de voir et de faire uin parallèle entre le code écrite et le résultat
#inutile de connaître par coeur le code en question il vous suffit de savoir que 
# "ha, je veux obtenir ce résulat, dans ce cours on obtenait à peu près ce que je veux, et si
# j'allais le reconsulter un peu mieux"
#Si les cours ne suffisait pas, ChatGPT ou un de ses concurents seras probablement capable de vous aider
#en dernier recours vous avez la recherche google et MOI votre serviteur.


#Bien, maintenant attaquons
#Avant tout, il nous faut apprivoiser les bases
#du langage python, pour cela :
# langage/variable.py
#  ''    /condition.py 
#  ''    /boucle.py

#consigne :
#un nombre entier est choisi aléatoirement par le jeu
#le joueur se voit demander des tentatives pour trouver ce nombre
#à chaque tentative, le jeu indique si le nombre est supérieur ou inférieur à la tentative
#et si je joueur se rapproche ou s'éloigne du nombre cherché
#quand le joueur trouve le nombre, un message de réussite est affiché
#ainsi que le nombre de tentative utilisé par le joueur


#nombre aléatoire entre 0 et MAX
MAX = 1000
from random import randint
n = randint(0,MAX)


#CORRECTION

#le nombre choisi par le joueur, on lui donne une valeur impossible au début
x = MAX+1

#le nombre de tentatives
turn = 1




#on récupère une valeur depuis le terminal en s'assurant que c'est un entier
trying = ""
while not (trying.isdigit() and 0>int(trying)<MAX):
    trying = input(f"Entrer un nombre entre 0 et {MAX} >>")
x = int(trying)

last_delta = abs(x-n) #nécessaire pour comparer le delta d'une tentative avec le delta de la tentative précédente

while x!=n: #tant que le joueur n'a pas réussi

    #on compare n et x
    if x > n:
        print(f"Le nombre magique est inférieur à {x} !")
    else:
        print(f"Le nombre magique est supérieur à {x} !")
    
    #on calcule la différence
    current_delta = abs(x-n)

    if current_delta > last_delta :
        print("Vous vous éloignez de votre objectif !")
    elif current_delta < last_delta :
        print("Vous vous rapprochez de votre obectif !")

    last_delta = current_delta #la tentaive acuelle étant maintenant passé on actualise les deltas

    trying = ""
    while not (trying.isdigit() and 0>int(trying)<MAX):
        trying = input(f"Entrer un nombre entre 0 et {MAX} >>")
    x = int(trying)

    turn= turn + 1

print(f"Bravo vous avez réussi à trouver le nombre {n} au bout de {turn} tentatives !")
